FROM python:3.8

ADD . /bot
WORKDIR /bot

RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]