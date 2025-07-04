# Sistema de votación

Este es un sistema de votación desarrollado con FastAPI como backend, PostgreSQL como base de datos, y Jinja2 para renderizar plantillas HTML. Permite registrar votantes, candidatos y emitir votos únicos.

Para configurar la base de datos debemos dirigirnos al archivo   `.env`   el cual tiene una línea de código que es la siguiente:
```env
DATABASE_URL=postgresql://postgres:CONTRASEÑA@localhost:5432/voting_system
```

Debemos asignar la contraseña que creamos en el motor de base de datos de postgresql en la parte que dice CONTRASEÑA para que se conecte correctamente e internamente cree la base de datos dentro de postgresql

Para la ejecucion del proyecto localmente debemos crear un entorno virtual, así que nos dirigimos a la terminal y copiamos el siguiente comando:
  `python -m venv env`

Luego debemos activar el entorno virtual de la siguiente manera:
  `env\Scripts\activate`

Una vez ejecutado debemos instalar los paquetes y dependencias necesarias para la ejecucion y realizacion de pruebas del proyecto copiando el siguiente comando:
  `pip install -r requirements.txt`

Debemos ejecutar el siguiente comando para realizar las pruebas desde Swagger UI:
  `uvicorn app.main:app --reload`

Este nos debera arrojar este resultado una vez ejecutado el comando:
  `INFO:     Application startup complete.`

Nos dirigimos al navegador y copiamos el link que arroja el comando anterior en las primeras lineas dentro la terminal, en mi caso es el: 
  `http://127.0.0.1:8000`

Se redirige a la pagina de Swagger UI para ver los endpoints del proyecto. 

A continuación adjunto imagenes donde se agrega informacion y los resultados que este arroja junto con las estadisticas de votación:

Vista general de los Endpoints:

![Swagger UI](https://github.com/user-attachments/assets/1f8de3d1-658c-47f6-9234-4c5ac92dd941)


## Creacion de Votantes

![Create Voter](https://github.com/user-attachments/assets/abfc24c8-6dbf-467c-b805-5b1902f095e7)

![Result Voter](https://github.com/user-attachments/assets/de70da93-33d5-4914-a962-90131f7f0dc9)


## Creación de Candidatos

![Create Candidate](https://github.com/user-attachments/assets/73895e0b-0d8c-437d-952f-2476e1679d6b)

![Result Candidate](https://github.com/user-attachments/assets/a8f037c4-831a-4fc8-9959-3b7042b5578b)


## Procedimiento de votación

![Submit Votes](https://github.com/user-attachments/assets/5da01996-fc65-497b-8440-82ff134ed74b)

![Statistics Votes](https://github.com/user-attachments/assets/819d1c3e-e440-4dd3-b2d6-eecc494255bd)


## Vista de Estadisticas

![View Statistics](https://github.com/user-attachments/assets/dc18afa3-901c-4897-909f-efc6bc471fef)
