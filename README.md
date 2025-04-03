# PAR-TRAEFIK
1. Primer paso clonar el repositorio
   ![image](https://github.com/user-attachments/assets/06eaf906-96a5-4a8b-9add-54a5b15b0d27)
2. En la misma linea de comandos escribir 'docker compose up -d --build'
![image](https://github.com/user-attachments/assets/9599945e-abb1-4c61-8b18-d05a69284c05)
Deberia responder
![image](https://github.com/user-attachments/assets/898c615e-3ad9-45f2-b17b-433268d06574)

4. Probar los endpoints en el parcial se solicitaron 4 servicios

     4.1 Servicio-Cliente-X:
  CLIENTE API 1
   ![image](https://github.com/user-attachments/assets/cd5f0d8f-6f6d-4a30-a3de-c45cd1614a4f)

   CLIENTE API 2
  ![image](https://github.com/user-attachments/assets/25450070-fd78-4a01-b2a0-9f277bad3d38)

    4.2 Servicio Analisis Servicio que recibe peticiones de los clientes, Debe registrar cuántas solicitudes ha recibido de cada cliente.
    http://localhost/reporte   Usuario: admin Clave: 123
   ![image](https://github.com/user-attachments/assets/6580a5fc-260e-4565-8021-52e7f1e71862)

  4.3 Panel Visual
  ![image](https://github.com/user-attachments/assets/944730c5-7fac-4565-ae69-1ce97d5b2b54)
  Panel donde uno ve cosas (?) imprime cosas esta hecho con nginx y html

  4.4 logger-central:
  ![image](https://github.com/user-attachments/assets/b572ede6-8f7f-4237-854e-abbfb4485918)
  ■ El logger-central debe responder con un simple "registro recibido" por cada entrada.
  Asi se veria la peticion get
  ![image](https://github.com/user-attachments/assets/69273974-5b74-4294-9063-0ba2343e1787)
  El '5' que aparece todo random fue por que le puse que el header era X cuando hice el post en la imagen anterior

### BASIC AUTH
![image](https://github.com/user-attachments/assets/20e1d0bd-add9-419c-ab5e-b786edae4599)
Se aprecia que se tiene autorizacion 🤑🤑🤑
