import requests
import os

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL_translate = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
URL_detect = 'https://translate.yandex.net/api/v1.5/tr.json/detect'


#  расширенная функция перевода. Перевод по умолчанию в ru.
def translate(txt_from_file, file_for_write, from_lang, to_lang='ru'):
    params = {
        'key': API_KEY,
        'text': txt_from_file,
        'lang': "{}-{}".format(from_lang, to_lang)
    }
    response = requests.get(URL_translate, params)
    json_translate = response.json()
    for text in json_translate["text"]:
        writing_translated_text(file_for_write, text, to_lang)


#  запись переведенного текста в созданный ранее файл
def writing_translated_text(file_for_write, text, to_lang):
    with open(file_for_write, "w", encoding="utf-8") as f_ru:
        f_ru.write(text)
    print(f"Текст перевода (на язык {to_lang}) сохранен в файле: {file_for_write}")


#  текст из файла (для перевода)
def from_file():
    fullname = r"txt\FR.txt"
    with open(fullname, "r", encoding="utf-8") as f:
        txt_from_file = f.read().strip("\n")
    return txt_from_file


#  создание файла, куда в дальнейшем будем записывать перевод текста
def to_file():
    name = r"txt\translated_text.txt"
    with open(name, "w", encoding="utf-8") as file:
        pass
    file_for_write = os.path.join(os.getcwd(), name)
    return file_for_write


#  определеяем язык, который будем переводить
def lang_detect(text_for_analys):
    param = {
        'key': API_KEY,
        'text': text_for_analys[0:75],  #  сделал срез - для определения языка этого достаточно
        'hint': 'de,fr,es'
    }
    response = requests.post(URL_detect, param)
    detect_json = response.json()
    from_lang = detect_json["lang"]
    print(f"Перевод будет произведен с языка: {from_lang}")
    return from_lang


# MAin
translate(from_file(), to_file(), lang_detect(from_file()))
