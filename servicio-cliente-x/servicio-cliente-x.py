import os
import time
import requests
from flask import Flask, jsonify

app = Flask(__name__)

SERVICE_ID = os.environ.get('SERVICE_ID', 'unknown')
API_REGISTRO_URL = "http://servicio-analiticas:5000/reporte" # Envia a reportes
API_LOGERS_URL = "http://logger:5000/logs" # Envia a logs para registrar (entiendo que es una forma chambona pero XD)

def registrar_servicio():
    headers = {"X-Service-ID": SERVICE_ID} 
    try:
        response = requests.post(API_REGISTRO_URL, headers=headers)
        print(f"[{SERVICE_ID}] Registro: {response.json()}")
        return response.json()
    except Exception as e:
        print(f"[{SERVICE_ID}] Error: {e}")
        return {"error": str(e)}
    
# Envia a logs para registrar (entiendo que es una forma chambona pero XD)
# Envia a logs para registrar (entiendo que es una forma chambona pero XD)  
def registrar_logs():
    headers = {"X-Service-ID": SERVICE_ID}
    try:
        response = requests.post(API_LOGERS_URL, headers=headers)
        print(f"[{SERVICE_ID}] Registro: {response.json()}")
        return response.json()
    except Exception as e:
        print(f"[{SERVICE_ID}] Error: {e}")
        return {"error": str(e)}

@app.route('/')
def index():
    result = registrar_servicio()
    return jsonify({
        "service": SERVICE_ID,
        "registered": result
    })

if __name__ == "__main__": # Simulan clientes que hacen solicitudes periódicas a un backend.
    # Registrar periódicamente en segundo plano
    import threading
    def periodic_register():
        while True:
            registrar_servicio()
            registrar_logs()
            time.sleep(10)  # Cada 10 segundos
    
    threading.Thread(target=periodic_register, daemon=True).start()
    
    # Iniciar servidor web
    app.run(host="0.0.0.0", port=5000)