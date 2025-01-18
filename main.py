from encryption_algos.vernam_cypher import vernam_encryption, vernam_decryption

def main():
    message = input('Введите текст: ')
    key = input('Введите ключ: ')

    result_encoded = vernam_encryption(message, key)
    print([result_encoded], '\n')

    encrypted_message = input('Введите зашифрованное сообщение: ')
    key = input('Введите ключ: ')
    
    result_decoded = vernam_decryption(encrypted_message, key)
    return print([result_decoded], '\n')





if __name__ == "__main__":
    
    main()
    print('Все здорово')

else:
    print('Ниче не здорово...')