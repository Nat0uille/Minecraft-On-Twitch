import tailer
import requests
import re
from rich import print

# Chemin d'accès complet du fichier de logs de Lunar Client.
log_file_path = 'C:/Users/Natanaël/.lunarclient/offline/multiver/logs/latest.log'

# ID d'utilisateur et jeton d'API Wizebot.
api_token = 'bc284eb4e8ebc389772cd118ef7d6a77c805503aaca67eb97aaefc9da09fca45'

# Nom de la variable Wizebot à mettre à jour.
variable_name = 'ipserver'

# Adresse IP du serveur précédent.
previous_server = ''
print("[#144453]███╗   ██╗ █████╗ ████████╗ ██████╗ ██╗   ██╗██╗██╗     ██╗     ███████╗")
print("[#144453]████╗  ██║██╔══██╗╚══██╔══╝██╔═████╗██║   ██║██║██║     ██║     ██╔════╝")
print("[#144453]██╔██╗ ██║███████║   ██║   ██║██╔██║██║   ██║██║██║     ██║     █████╗  ")
print("[#144453]██║╚██╗██║██╔══██║   ██║   ████╔╝██║██║   ██║██║██║     ██║     ██╔══╝  ")
print("[#144453]██║ ╚████║██║  ██║   ██║   ╚██████╔╝╚██████╔╝██║███████╗███████╗███████╗")
print("[#144453]╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝")
print("[#144453]Version : 0.1 ALPHA")
print("[#0d2b35]En attente d'une IP (Si vous êtes déja connecté a un serveur, déco/reco.)")
# Fonction pour mettre à jour la variable Wizebot.
def update_wizebot_variable(server_ip):
    url = f'https://wapi.wizebot.tv/api/custom-data/{api_token}/set/{variable_name}/{server_ip}'
    response = requests.get(url)
    if response.status_code == 200:
        print(f"[#008080]L'ip est maintenant définie pour : {server_ip}")
    else:
        print(f"[#008080]Erreur lors de la mise à jour de l'IP pour {server_ip}")

# Surveillance du fichier de logs de Lunar Client.
for line in tailer.follow(open(log_file_path)):
    # Recherche de la ligne indiquant que le joueur s'est connecté à un nouveau serveur.
    if 'Connecting to' in line:
        # Obtention de l'adresse IP du serveur à partir de la ligne.
        server_ip = line.split('Connecting to ')[1].split('...')[0]
        server_ip = re.search(r"([\w\.-]+),\s*\d+", server_ip)
        server_ip = server_ip.group(1)
        server_ip = re.sub(r"(?u)\s+$", "", server_ip)
        if server_ip[-1] == ".":
            server_ip = server_ip[:-1]
        # Vérification que le serveur a changé.
        if server_ip != previous_server:
            # Mise à jour de la variable Wizebot.
            update_wizebot_variable(server_ip)
            # Enregistrement du nouveau serveur.
            previous_server = server_ip
