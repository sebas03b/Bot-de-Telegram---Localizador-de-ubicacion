import json
import os
from datetime import datetime
from config import DATA_PATH

def save_location(user_id, lat, lon):
    # Crear archivo si no existe
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump([], f)
    
    # Cargar ubicaciones existentes
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    
    # Agregar nueva ubicación
    new_entry = {
        "user_id": user_id,
        "latitude": lat,
        "longitude": lon,
        "timestamp": datetime.now().isoformat()
    }
    data.append(new_entry)
    
    # Guardar
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)

def get_user_locations(user_id):
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        data = json.load(f)
    return [d for d in data if d["user_id"] == user_id]
