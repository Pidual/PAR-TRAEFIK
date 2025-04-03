FROM python:3.9-slim

WORKDIR /app

COPY servicio-cliente-x.py .

RUN pip install flask requests

CMD ["python", "servicio-cliente-x.py"]