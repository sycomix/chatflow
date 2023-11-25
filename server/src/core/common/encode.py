import base64


def encode_to_base64(input_string):
    bytes_string = input_string.encode('utf-8')
    base64_bytes = base64.b64encode(bytes_string)
    return base64_bytes.decode('utf-8')


def decode_from_base64(base64_string):
    base64_bytes = base64_string.encode('utf-8')
    bytes_string = base64.b64decode(base64_bytes)
    return bytes_string.decode('utf-8')
