from urllib.parse import unquote
import json


class Decoder:
    def decode(data, key, user_agent, fuid01):
        rkey = user_agent + fuid01 + key
        result = ""
        for i in range(len(data)):
            result = result + chr(ord(data[i]) ^ ord(rkey[i % len(rkey)]))
        result = unquote(unquote(result))
        return json.loads(result)
