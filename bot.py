#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown

import os
from dotenv import load_dotenv
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query
    if "m/" in query:
        results = [
            InlineQueryResultArticle(
                id=uuid4(), title="Result", description="words...", input_message_content=InputTextMessageContent("words words words"), thumb_url="https://i.pinimg.com/originals/f7/86/44/f7864403f01d75ac2d24944ac836ae1f.png")
        ]
    else:
        results = [
            InlineQueryResultArticle(
                id=uuid4(), title="Morse code", description=".-.. .-- -.-", input_message_content=InputTextMessageContent(".-.. .-- -.-"), thumb_url="https://camo.githubusercontent.com/3494de09199b6b16fce39dfce8b20ccd1b2f8be0/687474703a2f2f7777772e636f64656275672e6f72672e756b2f6173736574732f73746570732f3534302f696d6167655f312e706e67")
        ]

    update.inline_query.answer(results)


def main():
    api_token = os.environ.get("TG_BOT_API_TOKEN", False)
    if not api_token:
        raise RuntimeError("No token provided. Check your .env file")

    updater = Updater(api_token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
