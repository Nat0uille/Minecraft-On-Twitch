import requests
import tailer
import time
import re
import os
import json

# COULEUR COULEUR COULEUR #
cyan = "\033[0;36m"
rouge = "\033[0;31m"
vert = "\033[0;32m"
blanc = "\033[0m"
bleu = "\033[0;34m"
vert= "\033[0;32m"
# COULEUR COULEUR COULEUR #
def ascii():
    print(cyan +"███╗   ███╗ ██████╗    ██████╗ ███╗   ██╗   ████████╗████████╗██╗   ██╗")
    print(cyan +"████╗ ████║██╔════╝   ██╔═══██╗████╗  ██║   ╚══██╔══╝╚══██╔══╝██║   ██║")
    print(cyan +"██╔████╔██║██║        ██║   ██║██╔██╗ ██║      ██║      ██║   ██║   ██║")
    print(cyan +"██║╚██╔╝██║██║        ██║   ██║██║╚██╗██║      ██║      ██║   ╚██╗ ██╔╝")
    print(cyan +"██║ ╚═╝ ██║╚██████╗   ╚██████╔╝██║ ╚████║      ██║      ██║    ╚████╔╝ ")
    print(cyan +"╚═╝     ╚═╝ ╚═════╝    ╚═════╝ ╚═╝  ╚═══╝      ╚═╝      ╚═╝     ╚═══╝  ")

def updatewizebot(serverip):
    url = f'https://wapi.wizebot.tv/api/custom-data/{tokenwzbot}/set/serverip/{serverip}'
    response = requests.get(url)
    if response.status_code == 200:
        print(vert +"[Succès] " + blanc +"L'ip définie est maintenant " + bleu + serverip)
    else:
        print(rouge +"[Erreur] " + blanc +"Erreur de mise à jour de l'ip" + bleu + serverip)
        
def check_alias(serverip):
    with open('alias.txt', 'r', ) as file:
        for line in file:
            if len(line.split()) > 1:
                if line.split()[0] == serverip:
                    result = line.split()[1:]
                    result_str = ' '.join(map(str, result))
                    result_clean = re.sub(r'[\[\],\']', '', result_str)
                    return result_clean
    return None

aliastexte = [
    "# Les Alias permettent de remplacer le texte par un autre texte.\n",
    "# Utiles pour ne pas leak l'IP d'un serveur privé\n",
    "# Ou si l'IP d'un serveur ne correspond pas à celle rentrée dans le menu multijoueur\n",
    "\n",
    "# Exemple en dessous\n",
    "tcpshield.craftok.fr craftok.fr\n",
    "ip.tropbeau Serveur Privé\n",
    "ip.tropbeau ip.tropbeau (De la 1.8 à la 1.19 Crack Autorisé)\n",
    "\n",
    "# Custom"
]

optiontexte = [
    "{\n"
        '"logs_path": "LOGS",\n',
        '"token_wizebot": "TOKEN WIZEBOT"\n',
      "}"
]


os.system('cls' if os.name == 'nt' else 'clear')
if not os.path.exists('alias.txt'):
    fichier = open('alias.txt', 'w')
    fichier.writelines(aliastexte)
    fichier.close()
    print(vert +"[Succès] " + blanc +"Fichier " + bleu + "alias.txt " + blanc + "a bien été crée !")
if not os.path.exists('options.json'):
    fichier = open('options.json', 'w')
    fichier.writelines(optiontexte)
    fichier.close()
    print(vert +"[Succès] " + blanc +"Fichier " + bleu + "options.json " + blanc +"a bien été crée !")
with open("options.json", encoding="utf-8") as json_file:
    data = json.load(json_file)
    tokenwzbot = data["token_wizebot"]
    logs = data["logs_path"]
if len(tokenwzbot) <= 60:
    print(rouge +"[Erreur] " + blanc +"Désolé, mais tu n'as pas defini ton token WizeBot !")
    print(rouge +"[Erreur] " + blanc +"Lien pour trouver son token Wizebot : " + bleu +"https://panel.wizebot.tv/development_api_management")
    print(rouge +"[Erreur] " + blanc +"Et veiller utiliser la " + vert +"Clé d'authentification API [RW] (Lecture / Écriture)")
    time.sleep(5)
else:
    if not logs:
        print(rouge +"[Erreur] " + blanc + "Désolé, mais tu n'as pas defini les logs Minecraft !")
        print(rouge +"[Erreur] " + blanc +"Il faut changer dans le options.json !")
        time.sleep(5)
    else:
        ascii()
        print(cyan +"Version 0.2.1")
        print(cyan +"Par Nat0uille")
        print(cyan +"[Info] " + blanc +"En attente d'une IP (Si vous êtes déja connecté a un serveur, déco/reco.)")
        print(cyan +"[Info] "+ blanc +"Variable " + bleu +"WizeBot " + blanc + 'à mettre dans votre commande "' + vert + "$custom_data(get, serverip)" + blanc + '"')
        for line in tailer.follow(open(logs)):
            if 'Connecting to' in line:
                serverip = line.split('Connecting to ')[1].split(',')[0].strip()
                serverip = re.sub(r'\.$', '', serverip)
                alias = check_alias(serverip)
                if alias:
                    serverip = alias
                updatewizebot(serverip)
