# morse_inline_bot

Simple Telegram Inline bot for encoding and decoding Morse code.
You can just try it out here [@morse_inline_bot](https://t.me/morse_inline_bot)

## Running the bot legacy

1. `pip install -r requirements.txt`
2. Fill token in `TG_BOT_API_TOKEN` variable at `.env`
3. `python bot.py`

## Running the bot in Docker

1. Fill token in `TG_BOT_API_TOKEN` variable at `.env`
2. `docker build . -t morse_inline_bot:whatever`
3. `docker run morse_inline_bot:whatever`
