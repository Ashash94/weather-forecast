import requests
import pyttsx3

from config_nlp import URL, HEARDERS

weather_data = "Les informations météorologiques indiquent un temps nuageux avec une température minimale de 10,1°C, une température maximale de 20°C, une humidité relative de 45 à 85%, une précipitation de 0 mm au cours des 24 dernières heures, un indice UV de 3, un ciel voilé et une durée de soleil de 14 heures et 41 minutes."

def generate_text_forecast(weather_data):
    context = """ Parle comme Catherine Laborde, l'ancienne présentatrice du bulletin météo sur TF1 (chaîne de télévision française)
    """
    # Contenu de la requete API
    body = {
    "model": "amazon_model_identifier",
    "prompt": context + weather_data,
    "max_tokens": 100,
    "temperature": 0.7,
    "providers" : "amazon",
    "text" : "Donne moi la météo du 10 janvier 2022 à Paris"
    }

    # Appel API
    response = requests.post(URL, headers=HEARDERS, json=body)

    # voyons si le texte est bien ramassé 
    text_forecast = response.json().get('amazon', {}).get('generated_text', '')
    return text_forecast

# Créer une fonction qui renomme le fichier audio en "audio+timestamp.mp3"

# Créer l'audio 
def generate_audio_forecast(text_forecast):
    text_forecast = generate_text_forecast(weather_data)
    engine = pyttsx3.init() # object creation

    engine.setProperty('rate', 150)     # paramètre du taux de mots par minute

    engine.setProperty('language', 'fr')    # paramètre de la langue
    
    engine.setProperty('volume',1.0)    # paramètre du volume entre 0 et 1

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) # choix de la voix

    engine.say(text_forecast) # Cite le bulletin météo
    engine.runAndWait()
    engine.stop()
    
    # # On linux make sure that 'espeak' and 'ffmpeg' are installed
    # engine.save_to_file('Hello World', 'test.mp3') # télécharger l'audio
    # engine.runAndWait()

    
text_forecast = generate_text_forecast(weather_data)
print(text_forecast)
generate_audio_forecast(text_forecast)
