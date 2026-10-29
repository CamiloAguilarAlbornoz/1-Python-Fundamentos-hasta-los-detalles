from translate import Translator

with open('message.txt', mode='r') as my_message:
    message_text = my_message.read()
    print(f'Mensaje original: {message_text}')
    print('Translating...')
    translator = Translator(to_lang='es')
    translation = translator.translate(message_text)
    print(f'Mensaje traducido: {translation}')
    
    with open('message_translated.txt', mode='w') as my_message_translated:
        my_message_translated.write(translation)