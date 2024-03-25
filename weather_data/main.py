from functions import connect_bdd, create_table_forecasts
from city_list import create_table_cities, fetch_data_table_cities
# Elements nécessaire à la connexion à la base de donnée (BDD)
cur, conn = connect_bdd()

# Créer la table des prévisions
create_table_forecasts(cur, conn)

# Créer la table des villes
create_table_cities(cur, conn)

# Ajout des villes dans la table cities
fetch_data_table_cities()