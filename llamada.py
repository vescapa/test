import requests
import json

# Función para realizar la solicitud POST
def enviar_peticion(numero_telefono):
    # URL de la API
    url = "https://3x13vszwd7.execute-api.eu-west-1.amazonaws.com/prod/twilio-user"

    # Datos que deseas enviar (ajustados al formato JSON)
    data = {
        "Phone": numero_telefono,  # Número de teléfono que proporcionas como parámetro
        "ConfigurationId": 1,
        "DesignatorTypeName": "Digital",
        "CustomerId": "N/A"
    }

    # Encabezados HTTP
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Origin": "https://te-llamamos.genesis.es",
        "Referer": "https://te-llamamos.genesis.es/",
        "Connection": "close",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site"
    }

    # Realizar la solicitud POST
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        print("Solicitud enviada correctamente.")
    else:
        print(f"Error {response.status_code}: No se pudo enviar la solicitud.")

# Solicitar al usuario el número de teléfono
numero_telefono = input("Introduce el número de teléfono (incluye el código de país): ")

# Llamar a la función con el número de teléfono proporcionado
enviar_peticion(numero_telefono)
