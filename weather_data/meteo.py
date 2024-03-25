from meteofrance_api import MeteoFranceClient

def get_weather_forecasts(postCode: str):
    try:
        client = MeteoFranceClient()

        list_places = client.search_places(postCode)
        my_place = list_places[0]
        fc = client.get_forecast_for_place(my_place)
        daily_fc = fc.forecast
        return daily_fc

    except Exception as e:
        print(e)
        return {"error": str(e)}
    
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

def delete_data_mf(cur, conn):
    cur.execute("DELETE FROM meteo_france")
    conn.commit()
    conn.close()
    
def delete_columns_mf(cur, conn):
    cur.execute("ALTER TABLE meteo_france DROP COLUMN longitude, DROP COLUMN latitude")
    conn.commit()
    conn.close()

# Créer une fonction qui va créer une table qui reprend la date, la température minimum, la température maximum, le lever et le coucher du soleil