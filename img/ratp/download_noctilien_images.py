import os
import requests
from bs4 import BeautifulSoup

# Crée le dossier img s'il n'existe pas déjà
os.makedirs('bus', exist_ok=True)

# Fonction pour télécharger l'image
def download_bus_image(bus_number):
    url = f"https://commons.wikimedia.org/wiki/File:Logo_Ligne_Bus_Noctilien_N{bus_number}.svg"
    
    # Envoi de la requête pour obtenir la page HTML
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP
        
        # Analyser la page HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Trouver toutes les occurrences de l'image
        img_tags = soup.find_all('a', {'class': 'mw-thumbnail-link', 'href': True})
        
        # Vérifier s'il existe des occurrences et récupérer la dernière
        if img_tags:
            img_tag = img_tags[-1]  # Dernière occurrence
            img_url = img_tag['href']
            print(f"URL de l'image pour la ligne N{bus_number}: {img_url}")
            
            # Télécharger l'image
            img_response = requests.get(img_url, headers=headers)
            img_response.raise_for_status()  # Lève une exception pour les erreurs HTTP
            
            # Sauvegarde l'image sous le nom du numéro de bus
            file_path = f"bus/N{bus_number}.png"
            with open(file_path, 'wb') as f:
                f.write(img_response.content)
            print(f"Image pour la ligne N{bus_number} téléchargée avec succès.")
        else:
            print(f"Image pour la ligne N{bus_number} non trouvée.")
    
    except requests.exceptions.RequestException as e:
        # En cas d'erreur, affiche un message et passe à la ligne suivante
        print(f"Erreur pour la ligne {bus_number}: {e}")

# Télécharger les images pour les lignes de bus 1 à 999
for bus_number in range(1, 1000):
    download_bus_image(bus_number)
