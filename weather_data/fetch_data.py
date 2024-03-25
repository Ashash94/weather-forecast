from datetime import datetime

from functions import format_update_dt
from city_list import cities_list
from meteo import get_weather_forecasts

def format_forecast_dt(timestamp: int) -> str:
    formatted_dt = datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y %H:%M:%S")
    
    return formatted_dt

def fetch_data_table_mf():
    # cur, conn = connect_bdd()
    for city in cities_list:
        postCode = city["zip_code"]
        weather_forecasts = get_weather_forecasts(postCode)
        
        if weather_forecasts:
            update_time = datetime.now()
            updated_dt = format_update_dt(update_time)
            
            for wf in weather_forecasts:
                timestamp = wf["dt"]
                date = format_forecast_dt(timestamp)
                print(date)
    #         #temp = wf["T"]["value"]
    #         temp = 0.0
    #         #ressenti = wf["T"]["windchill"]
    #         ressenti = 0.0
    #         #hum = wf["humidity"]
    #         hum = 0.0
    #         #nvMer = wf["sea_level"]
    #         nvMer = 0.0
    #         #vent = wf["wind"]["icon"]
    #         vent = 0.0
    #         # pluie = wf["rain"]
    #         pluie = 0.0
    #         # neige = wf["snow"]["1h"]
    #         neige = 0.0
    #         # nuage = wf["clouds"]
    #         nuage = 0.0
    #         # desc = wf["weather"]["desc"]
    #         desc = 0.0
    #         # print(f"Date: {date}, Température: {temp}°C, Ressenti: {ressenti}°C, Humidité: {hum}%, Vent: {vent}")
            
    #         # Insérer les données dans la table
            
    #         cur.execute(
    #             """
    #             INSERT INTO meteo_france (city, postCode, date, temp, ressenti, hum, nvMer, vent, pluie, neige, nuage, descr, updated_dt) 
    #             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    #             """,
    #             (city['label'], postCode, date, temp, ressenti, hum, nvMer, vent, pluie, neige, nuage, desc, updated_dt)
    #         )
            
    #         # Commit des modifications dans la base de données
    #         conn.commit()
    # else:
    #     print(f"Aucune donnée météo disponible pour {city['label']} ({postCode})")
    # conn.close()

fetch_data_table_mf()