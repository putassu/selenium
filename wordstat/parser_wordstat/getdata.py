import os
import js2py
import requests
import time

from Parser.settings import *
from wordstat.parser_wordstat.decoder import Decoder
from wordstat.parser_wordstat.parse import Parser
from wordstat.parser_wordstat.sessions import SessionObject



def get_history_data(data):
    parse = Parser(SessionObject())
    auth = parse.auth_yandex()
    print(auth)
    data_result = parse.search(data)
    data_result = []
    return data_result
