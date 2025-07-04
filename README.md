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

## Vista general de los Endpoints:

![Swagger UI](https://github.com/JaimeH68/prueba-tecnica-JaimeH68/blob/9b4fac8bcdb33525d2d111991a125ba3facfede3/assets/Swagger%20UI.png)


## Creacion de Votantes

![Create Voter](https://github.com/JaimeH68/prueba-tecnica-JaimeH68/blob/9b4fac8bcdb33525d2d111991a125ba3facfede3/assets/Create%20Voter.png)

![Result Voter](https://github.com/JaimeH68/prueba-tecnica-JaimeH68/blob/9b4fac8bcdb33525d2d111991a125ba3facfede3/assets/Result%20Voter.png)


## Creación de Candidatos

![Create Candidate](https://github.com/JaimeH68/prueba-tecnica-JaimeH68/blob/9b4fac8bcdb33525d2d111991a125ba3facfede3/assets/Create%20Candidate.png)

![Result Candidate](https://github.com/JaimeH68/prueba-tecnica-JaimeH68/blob/9b4fac8bcdb33525d2d111991a125ba3facfede3/assets/Result%20Candidate.png)


## Procedimiento de votación

![Submit Votes](https://github.com/JaimeH68/prueba-tecnica-JaimeH68/blob/9b4fac8bcdb33525d2d111991a125ba3facfede3/assets/Submit%20Votes.png)

![Statistics Votes](https://github.com/JaimeH68/prueba-tecnica-JaimeH68/blob/9b4fac8bcdb33525d2d111991a125ba3facfede3/assets/Statistics%20Votes.png)


## Vista de Estadisticas

![View Statistics](https://github.com/JaimeH68/prueba-tecnica-JaimeH68/blob/9b4fac8bcdb33525d2d111991a125ba3facfede3/assets/View%20Statistics.png)
