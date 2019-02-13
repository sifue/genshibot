#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess

from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to

from cotoha_nlp.parse import Parser

parser = Parser(os.environ['COTOHA_CLIENT_ID'],
  os.environ['COTOHA_CLIENT_SECRET'],
  "https://api.ce-cotoha.com/api/dev/nlp",
  "https://api.ce-cotoha.com/v1/oauth/accesstokens"
)

@respond_to(r'(.*)')
def translate(message, something):
    s = parser.parse(something)
    genshi = " ".join([token.kana for token in s.tokens if token.pos not in ["格助詞","連用助詞","引用助詞","終助詞"]])
    message.send(genshi)

# main 処理
bot = Bot()
bot.run()
