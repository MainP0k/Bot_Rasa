# discord_connector.py

import discord
from rasa.core.channels.channel import InputChannel, UserMessage, OutputChannel
from rasa.core.channels.channel import CollectingOutputChannel
from rasa.utils.endpoints import EndpointConfig
from typing import Text, List, Dict, Any, Optional, Callable, Awaitable
import inspect

class DiscordOutput(OutputChannel):
    @classmethod
    def name(cls) -> Text:
        return "discord"

    def __init__(self, client: discord.Client, channel: discord.TextChannel):
        self.client = client
        self.channel = channel

    async def send_text_message(self, recipient_id: Text, message: Text) -> None:
        await self.channel.send(message)

class DiscordInput(InputChannel):
    @classmethod
    def name(cls) -> Text:
        return "discord"

    def __init__(self, token: Text):
        self.token = token

    async def _message(self, on_new_message: Callable[[UserMessage], Awaitable[None]], message: discord.Message) -> None:
        user_message = UserMessage(
            text=message.content,
            output_channel=DiscordOutput(self.client, message.channel),
            sender_id=message.author.id,
            input_channel=self.name(),
        )
        await on_new_message(user_message)

    def blueprint(self, on_new_message: Callable[[UserMessage], Awaitable[None]]):
        from flask import Blueprint, request, jsonify

        discord_webhook = Blueprint("discord_webhook", __name__)

        @discord_webhook.route("/", methods=["GET"])
        def health():
            return jsonify({"status": "ok"})

        @discord_webhook.route("/webhook", methods=["POST"])
        async def receive():
            payload = request.json
            message = discord.Message(**payload)
            await self._message(on_new_message, message)
            return jsonify({"status": "ok"})

        return discord_webhook

    def register(self, app: Text, on_new_message: Callable[[UserMessage], Awaitable[None]]):
        blueprint = self.blueprint(on_new_message)
        app.blueprint(blueprint)

    async def run(self, on_new_message: Callable[[UserMessage], Awaitable[None]]) -> None:
        intents = discord.Intents.default()
        intents.messages = True

        client = discord.Client(intents=intents)
        self.client = client

        @client.event
        async def on_ready():
            print(f"We have logged in as {client.user}")

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return
            await self._message(on_new_message, message)

        await client.start(self.token)
