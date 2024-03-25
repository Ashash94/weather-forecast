from datetime import datetime
import psycopg2

from config import BDD_HOST, BDD_PORT, BDD_ID, BDD_MDP

# Connecter la bdd 
def connect_bdd():
    conn = psycopg2.connect(
        dbname = "weather_forecasts",
        user = BDD_ID,
        password = BDD_MDP,
        host = BDD_HOST,
        port = BDD_PORT
    )
    cur = conn.cursor()
    return cur, conn

# Création de la table
def create_table_forecasts(cur, conn):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS meteo_france (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            postCode VARCHAR(5),
            date VARCHAR(22),
            temp FLOAT,
            ressenti FLOAT,
            hum INTEGER,
            nvMer FLOAT,
            vent VARCHAR(70),
            pluie INTEGER,
            neige INTEGER,
            nuage INTEGER,
            descr VARCHAR(70),
            updated_dt VARCHAR(22)
        )
        """
    )
    conn.commit()
    
# Changer le format de la date et l'heure de la mise à jour de la donnée
def format_update_dt(update_dt: str):
    update_dt = datetime.now()
    formatted_dt = update_dt.strftime("%d-%m-%Y %H:%M:%S")
    return formatted_dt

def delete_data_mf(cur, conn):
    cur.execute("DELETE FROM meteo_france")
    conn.commit()
    
def delete_columns_mf(cur, conn):
    cur.execute("ALTER TABLE meteo_france DROP COLUMN longitude, DROP COLUMN latitude")
    conn.commit()

# Créer une fonction qui va créer une table qui reprend la date, la température minimum, la température maximum, le lever et le coucher du soleil