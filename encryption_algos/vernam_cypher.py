import secrets
import string
import base64
import sqlite3



'''
----------------------------------------------------------------
    Функции для БД
----------------------------------------------------------------
'''

# создание БД и таблицы если ее нет 
def creating_database():
    db = sqlite3.connect('key_storage.db')
    cursor = db.cursor()
    cursor.execute('''

    CREATE TABLE IF NOT EXISTS Keys (
        id INTEGER PRIMARY KEY,   
        key TEXT NOT NULL,    
        value TEXT NOT NULL
    )

    ''')
    db.commit()
    db.close()

    return print('БД готова к работе!')


#  запись параметов 
def set_params(key, value):
    db = sqlite3.connect('key_storage.db')
    cursor = db.cursor()

    cursor.execute('INSERT INTO Keys (key, value) VALUES (?, ?)', (key, value))
    db.commit()
    db.close()

    return print('Ключик на базе!')

# получение значений (пока значения ключа)
def get_params(key):
    db = sqlite3.connect('key_storage.db')
    cursor = db.cursor()

    cursor.execute('SELECT value FROM Keys WHERE key = ?', (key,))
    value = cursor.fetchone()
    db.close()

    return value[0] 


'''
----------------------------------------------------------------
    Функции шифрования
----------------------------------------------------------------
'''

def message_symbols_from_ASCII(message):

    symbols_from_ASCII = []
    message_symbols_arr = list(message)

    for symbol in message_symbols_arr:
        position_symbols_form_ASCII = ord(symbol)
        symbols_from_ASCII.append(position_symbols_form_ASCII)

    return symbols_from_ASCII


def vernam_encryption(message, key):
    
    creating_database()

    message_symbols = message_symbols_from_ASCII(message)
    message_symbols_count = len(message_symbols)


    symbols_for_key = string.ascii_letters + string.digits + string.punctuation
    
    key_value = ''.join(secrets.choice(symbols_for_key) for _ in range(message_symbols_count))
    set_params(key=key, value=key_value)


    key_symbols = message_symbols_from_ASCII(key_value)

    encrypted_message = ""
    for i in range(message_symbols_count):
        encrypted_message += chr(message_symbols[i] ^ key_symbols[i])

    encrypted_message_base64 = base64.b64encode(encrypted_message.encode()).decode()
    return encrypted_message_base64


def vernam_decryption(encrypted_message_base64, key):

    creating_database()

    key_value = get_params(key)
    encrypted_message = base64.b64decode(encrypted_message_base64).decode()

    key_symbols = message_symbols_from_ASCII(key_value)
    message_symbols = message_symbols_from_ASCII(encrypted_message)

    decrypted_message = ""
    for i in range(len(message_symbols)):
        decrypted_message += chr(message_symbols[i] ^ key_symbols[i])

    return decrypted_message

