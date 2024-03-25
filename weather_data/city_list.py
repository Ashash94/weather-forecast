import json

from functions import connect_bdd

# Connexion à la BDD
cur, conn = connect_bdd()

#Ouvrir le fichier .json qui permet de créer la liste et la table de villes
def open_cities_json():
    with open('./data/cities.json', 'r') as file:
        city_file = json.load(file)
        return city_file

def get_city_list(city_file):
    cities_list = [] #liste vide
    for city in city_file['cities']: # boucle pour remplr la liste "l" pour chaque city dans la liste "cities"
        city_info = {
            'label': city['label'],
            'zip_code': city['zip_code'],
            'latitude': city['latitude'],
            'longitude': city['longitude']
        }
        cities_list.append(city_info) # ajoute le nom de la ville, le code postal, la latitude et la longitude de chaque ville
        
# Création de la table
def create_table_cities(cur, conn):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS cities (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            postCode VARCHAR(5),
            latitude FLOAT,
            longitude FLOAT
        )
        """
    )
    conn.commit()

# Ajout de ville dans la table cities

def fetch_data_table_cities():
    cur, conn = connect_bdd()
    cities_list = cur.execute("""
        SELECT * FROM cities
        """) # à vérifier avec un print 
    for city in cities_list:
        try:
            # Vérifier si la ville existe déjà dans la table
            cur.execute(
                """
                SELECT COUNT(*) FROM cities WHERE city = %s AND postCode = %s
                """,
                (city['label'], city['zip_code'])
            )
            exists = cur.fetchone()[0]
            
            if exists == 0:
                # Si elle existe la ville sera ajoutée dans la table
                cur.execute(
                    """
                    INSERT INTO cities (city, postCode, latitude, longitude) 
                    VALUES (%s, %s, %s, %s)
                    """,
                    (city['label'], city['zip_code'], city['latitude'], city['longitude'])
                )
                # Commit des modifications dans la base de données
                conn.commit()
                print(f"La ville {city['label']} a été insérée avec succès.")
            else:
                print(f"La ville {city['label']} existe déjà dans la table, pas d'insertion nécessaire.")
        except Exception as e:
            print("Une erreur s'est produite:", e)
            
    conn.close()
    print("Connexion à la base de données fermée.")
    
def delete_data_cities(cur, conn):
    cur.execute("DELETE FROM cities")
    conn.commit()
    conn.close()
