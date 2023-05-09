#####################################################################
#  OPTION  OPTION  OPTION  OPTION  OPTION  OPTION  OPTION  OPTION   #
#####################################################################

# Chemin d'accès vers les logs de ton Minecraft
logs = ""
# Exemple : 
# Lunar = C:/Users/Natanaël/.lunarclient/offline/multiver/logs/latest.log
# Badlion = C:/Users/Natanaël/AppData/Roaming/.minecraft/logs/blclient/minecraft/latest.log
# Minecraft/Feather = C:/Users/Natanaël/AppData/Roaming/.minecraft/logs/latest.log

tokenwzbot = ""
# Lien pour trouver son token Wizebot : 
# https://panel.wizebot.tv/development_api_management
# Et veiller utiliser la "Clé d'authentification API [RW] (Lecture / Écriture)"
alias_file = "alias.txt"

#####################################################################
#  OPTION  OPTION  OPTION  OPTION  OPTION  OPTION  OPTION  OPTION   #
#####################################################################
import requests
import tailer
import re
import time
import os
from rich import print

def ascii():
    print("[#008080]███╗   ███╗ ██████╗ ██████╗ ███╗   ██╗████████╗████████╗██╗   ██╗")
    print("[#008080]████╗ ████║██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝╚══██╔══╝██║   ██║")
    print("[#008080]██╔████╔██║██║     ██║   ██║██╔██╗ ██║   ██║      ██║   ██║   ██║")
    print("[#008080]██║╚██╔╝██║██║     ██║   ██║██║╚██╗██║   ██║      ██║   ╚██╗ ██╔╝")
    print("[#008080]██║ ╚═╝ ██║╚██████╗╚██████╔╝██║ ╚████║   ██║      ██║    ╚████╔╝ ")
    print("[#008080]╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝      ╚═╝     ╚═══╝  ")

os.system('cls' if os.name == 'nt' else 'clear')
if not tokenwzbot:
    print("[#DC0909][Erreur] [#FFFFFF]Désolé, mais tu n'as pas defini ton token WizeBot !")
    print("[#008080][Info] [#FFFFFF]Lien pour trouver son token Wizebot : [#334CB2]https://panel.wizebot.tv/development_api_management")
    print("[#008080][Info] [#FFFFFF]Et veiller utiliser la [#D87F33]Clé d'authentification API [RW] (Lecture / Écriture)")
else:
    if not logs:
        print("[#DC0909][Erreur] [#FFFFFF]Désolé, mais tu n'as pas defini les logs Minecraft !")
        print("[#008080][Info] [#FFFFFF]Il faut changer dans les options du code !")
    else:
        ascii()
        print("[#008080]Version 0.2 ALPHA")
        print("[#008080]Par Nat0uille")
        print("[#008080][Info] [#FFFFFF]En attente d'une IP (Si vous êtes déja connecté a un serveur, déco/reco.)")
        print('[#008080][Info] [#FFFFFF]Variable [#334CB2]WizeBot [#FFFFFF]à mettre dans votre commande "[#D87F33]$custom_data(get, serverip)[#FFFFFF]"')
        def updatewizebot(serverip):
            url = f'https://wapi.wizebot.tv/api/custom-data/{tokenwzbot}/set/serverip/{serverip}'
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[#008080]L'ip définie est maintenant [#FFFFFF]{serverip}")
            else:
                print(f"[#DC0909]Erreur de mise à jour de l'IP {serverip}")
                
        def check_alias(serverip):
            with open(alias_file, 'r') as file:
                for line in file:
                    if len(line.split()) > 1:
                        if line.split()[0] == serverip:
                            result = line.split()[1:]
                            result_str = ' '.join(map(str, result))
                            result_clean = re.sub(r'[\[\],\']', '', result_str)
                            return result_clean
            return None
        
        for line in tailer.follow(open(logs)):
            if 'Connecting to' in line:
                serverip = line.split('Connecting to ')[1].split(',')[0].strip()
                serverip = re.sub(r'\.$', '', serverip)
                alias = check_alias(serverip)
                if alias:
                    serverip = alias
                updatewizebot(serverip)
