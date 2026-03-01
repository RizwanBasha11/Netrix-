import json

def encode_message(msg):
    return json.dumps(msg).encode()

def decode_message(data):
    return json.loads(data.decode())
