from functions import format_update_dt
from datetime import datetime

# Utilité de cette fonction à revoir 
def current_time():
    current_timestamp = int(datetime.now().timestamp())
    current_time_str = format_update_dt(current_timestamp)
    
    return current_time_str