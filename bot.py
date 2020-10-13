#!/usr/bin/env python
# -*- coding: utf-8 -*-

from morse import MorseCodeTranslator
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown

import os
from dotenv import load_dotenv
load_dotenv()

morse_code_translator = MorseCodeTranslator()


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def make_description(text):
    return text[:16] + '...'


def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query
    if not query:
        results = [
            InlineQueryResultArticle(
                id=uuid4(), title="Waiting for input", description="Begin entering your message or begin with m/ to decode morse code",
                input_message_content=InputTextMessageContent(
                    "Hungry for Morse?"),
                thumb_url="https://dragonflytraining.files.wordpress.com/2013/10/man-with-question-01.png?w=600&h=600")
        ]
    elif "m/" in query[:2]:
        r = morse_code_translator.translate_morse(query[2:])
        results = [
            InlineQueryResultArticle(
                id=uuid4(), title="Result", description=make_description(r),
                input_message_content=InputTextMessageContent(r),
                thumb_url="https://i.pinimg.com/originals/f7/86/44/f7864403f01d75ac2d24944ac836ae1f.png")
        ]
    else:
        r = morse_code_translator.translate_text(query)
        results = [
            InlineQueryResultArticle(
                id=uuid4(), title="Morse code", description=make_description(r),
                input_message_content=InputTextMessageContent(r),
                thumb_url="https://camo.githubusercontent.com/3494de09199b6b16fce39dfce8b20ccd1b2f8be0/687474703a2f2f7777772e636f64656275672e6f72672e756b2f6173736574732f73746570732f3534302f696d6167655f312e706e67")
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
