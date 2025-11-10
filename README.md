
# 📍 Telegram Location Bot

Un bot de Telegram desarrollado en Python que solicita el permiso del usuario para compartir su ubicación actual y la almacena localmente en un archivo JSON.

---

## 🚀 Características

- Flujo de consentimiento: el usuario decide si compartir su ubicación.
- Guarda latitud, longitud y timestamp.
- Almacenamiento local sin base de datos externa.
- Implementado con `python-telegram-bot v20.7`.

---

## 🗂️ Estructura del proyecto

```

telegram-location-bot/
│
├── bot.py                  # Punto de entrada principal
├── config.py               # Token y rutas de configuración
│
├── handlers/
│   ├── start_handler.py    # Maneja el comando /start
│   └── location_handler.py # Guarda y responde a ubicaciones
│
├── services/
│   └── database.py         # Lógica de guardado en JSON
│
├── data/
│   └── locations.json      # Archivo de datos locales
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Instalación y ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/telegram-location-bot.git
   cd telegram-location-bot
``

2. Instala dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Configura tu token de Telegram en `config.py`:

   ```python
   TELEGRAM_TOKEN = "TU_TOKEN_DE_BOT"
   DATA_PATH = "data/locations.json"
   ```

4. Ejecuta el bot:

   ```bash
   python bot.py
   ```

---

## 🧠 Funcionamiento básico

* El usuario envía `/start` al bot.
* El bot responde con un botón para compartir la ubicación.
* Al aceptar, los datos se guardan en `data/locations.json`.
* El bot confirma el registro con las coordenadas recibidas.

---

## 🧰 Tecnologías utilizadas

* Python 3.12
* [python-telegram-bot](https://docs.python-telegram-bot.org/)
* JSON para almacenamiento local




