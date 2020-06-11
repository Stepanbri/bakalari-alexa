# Projekt, který má umožnit interakci se systémem "Bakaláře" přes chytrého asistenta od Amazonu který se jmenu Alexa.
# testovací program.
# Štěpán Bříza - 30.05.2020
# https://mot-spsd.bakalari.cz/login.aspx

import bakalari_token
import ssl
import getpass
import urllib.request


def generate_token(url_address, username, password):    #generuje token pro BakalařiAPI
    url = bakalari_token.process_url(url_address)
    token = bakalari_token.generate_token(url, username, password)
    return token

def get_module(url_address, token, module):     #získavá data a dekoduje je do utf-8
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    respond = urllib.request.urlopen(url_address + "?hx=" + token + "&pm=" + module).read()
    full_string = respond.decode("utf-8")
    return full_string

def again_ask(url_address, token):      #položí znovu otázku (vytvaří smyčku co se týče otázek)
    print(" ")
    ask(url_address, token)

def ask(url_address, token):    #pokladá otázku a zpracovává příkazy
    target = input("MODUL:")
    if target == "konec":    #ukončí program
        print(" ")
        print("Ukončuji...")
        exit()
    else:
        print(" ")
        print("Načítám...")
        data = get_module(url_address, token, a)
        print("Ukládám...")
        file = open(target + ".xml", "w", encoding="utf-8") #uloží soubor
        file.write(data)
        file.close()
        print("Hotovo! Informace jsou uloženy v složce projektu!")
        again_ask(url_address, token)



#hned po spuštění programu:
print("Dobrý den. Toto je jeden z testu tohoto projektu.")
print("Hlavní učelem projektu je vytvořit skill pro chytreho asistenta Alexa. Tento skill by umožnoval interakci mezi Bakalařemi a Alexou")
print(" ")
print("Prosím. Přihlaste se.")

url_address = input("ADRESA ŠKOLY:  ") #webová adressa školy pro přihlašení do bakalářu (v budoucnu udělám seznam škol)
username = input("PRIHLASOVACI JMENO: ") #přihlašovací jmeno
password = input('HESLO: ') #heslo (je potřeba zbezpečnit manipulaci. určitě v nepoužívat input a implementovat SHA-3)

if url_address == "spsd-motol": #zjednodušení pro uživatele u inputu url_address
    url_address = "https://mot-spsd.bakalari.cz/login.aspx"

print(" ")
print("Získavám připojení...")
print("Generuje se token...")
token = generate_token(url_address, username, password)
print("Token vygenerován! Uspěšně přihlašeno!")
print(" ")

ask(url_address, token)

