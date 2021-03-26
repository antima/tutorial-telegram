# *Tutorial bot telegram con Python*

Questa repository contiene gli esempi presentati nell'articolo di antima.it 
[Telegram Bot API - Interfacciarsi con i Bot Telegram tramite Python](https://antima.it/telegram-bot-api-interfacciarsi-con-i-bot-telegram-tramite-python/).


## Contenuti

- [Setup](#setup)
- [Esempi](#esempi)
    - [basic_ex.py](#basic_ex)
    - [simple_command.py](#simple_command)
    - [webpage_check.py](#webpage_check)

## Setup

Per installare tutte le librerie utilizzate, eseguire:

```bash
pip install -r requirements.txt
```

## Esempi

### basic_ex

Un semplice applicativo che inizializza un bot e stampa delle informazioni sulla sua identità.

### simple_command

In questa applicazione introduciamo i concetti di updater, dispatcher ed handler. 
La cattura dei comandi avviene registrando una callback relativa al singolo comando tramite un handler.

```python
updater = Updater(token)
updater.dispatcher.add_handler(CommandHandler("comando", callback))
```

### webpage_check

Ultimo esempio, dove andiamo a utilizzare i concetti discussi per creare un'applicazione tramite cui 
il bot manda notifiche all'utente che inizia una conversazione tramite una /start, ogni volta che una pagina
web riporta cambiamenti. 

Le chat id che avviano il servizio sono tenute da parte in un set, e la funzione che effettua il controllo 
sfrutta questa struttura dati per notificare a tutti gli utenti della ricezione di un update della pagina:

```python
def page_updated():
    interval = 5
    older = requests.get(target_url).text

    while True:
        page_data = requests.get(target_url).text
        if page_data != older:
            older = page_data
            for chat_id in chat_ids:
                updater.bot.send_message(chat_id=chat_id, text="Pagina aggiornata!")
        time.sleep(interval)
```