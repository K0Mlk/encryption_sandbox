import secrets
import string
import base64

key_storage = {}

def message_symbols_from_ASCII(message):

    symbols_from_ASCII = []
    message_symbols_arr = list(message)

    for symbol in message_symbols_arr:
        position_symbols_form_ASCII = ord(symbol)
        symbols_from_ASCII.append(position_symbols_form_ASCII)

    return symbols_from_ASCII


def vernam_encryption(message, key):

    global key_storage

    message_symbols = message_symbols_from_ASCII(message)
    message_symbols_count = len(message_symbols)


    if key not in key_storage:
        symbols_for_key = string.ascii_letters + string.digits + string.punctuation
    
        key_value = ''.join(secrets.choice(symbols_for_key) for _ in range(message_symbols_count))
        key_storage[key] = key_value

    else:
        key_value = key_storage[key]


    key_symbols = message_symbols_from_ASCII(key_value)

    encrypted_message = ""
    for i in range(message_symbols_count):
        encrypted_message += chr(message_symbols[i] ^ key_symbols[i])

    encrypted_message_base64 = base64.b64encode(encrypted_message.encode()).decode()
    return 'Зашифрованное сообщение: ' + encrypted_message_base64


def vernam_decryption(encrypted_message_base64, key):

    global key_storage

    key_value = key_storage[key]
    encrypted_message = base64.b64decode(encrypted_message_base64).decode()

    key_symbols = message_symbols_from_ASCII(key_value)
    message_symbols = message_symbols_from_ASCII(encrypted_message)

    decrypted_message = ""
    for i in range(len(message_symbols)):
        decrypted_message += chr(message_symbols[i] ^ key_symbols[i])

    return 'Расшифрованное сообщение: ' + decrypted_message







