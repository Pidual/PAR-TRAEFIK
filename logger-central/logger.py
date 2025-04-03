from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

# Diccionario para almacenar el conteo de solicitudes por cliente
registro = defaultdict(int)

@app.route("/logs", methods=["GET"])
def obtener_registro(): #Metodo copiado desde el servicio de analiticas
    # La autenticación es manejada por Traefik
    return jsonify(dict(registro))

@app.route("/logs", methods=["POST"])
def registrar_cliente():
    # Obtener el identificador del cliente desde el header
    service_id = request.headers.get("X-Service-ID")
    if not service_id:
        return jsonify({"error": "Missing X-Service-ID header"}), 400
    # Incrementar el contador para el cliente
    registro[service_id] += 1
    return "registro actualizado", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)