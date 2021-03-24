from telegram.ext import Updater
import requests

target_url = ""
older = ""


def page_updated():
    """
    Controlla che la pagina sia cambiata dalla scorso volta
    :return: True se la pagina sotto controllo ha avuto modifiche, altrimenti False
    """
    global older
    if not older:
        older = requests.get(target_url).text
        return False

    page_data = requests.get(target_url).text
    if page_data != older:
        return True
    return False

def main():
    updater = Updater(token)