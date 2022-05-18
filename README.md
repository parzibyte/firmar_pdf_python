# firmar_pdf_python
 Firmar un PDF con Python y Flask usando certificado P12

# Cómo usar
- Instalar Python y PIP, agregando a la PATH al instalar: https://parzibyte.me/blog/2019/10/08/instalar-python-pip-64-bits-windows/
- Abrir una terminal o CMD y navegar hasta la carpeta que contiene este proyecto
- Ahí ejecutar:
    - `pip install Flask`
    - `pip install endesive`
- Luego ahí mismo ejecutar:
    - `python server.py`
    - Debe decir algo como:
    - ``` * Serving Flask app 'server' (lazy loading)
            * Environment: production
            WARNING: This is a development server. Do not use it in a production deployment.
            Use a production WSGI server instead.
            * Debug mode: off
            * Running on all addresses (0.0.0.0)
            WARNING: This is a development server. Do not use it in a production deployment.
            * Running on http://127.0.0.1:81
            * Running on http://192.168.100.6:81 (Press CTRL+C to quit) ```
- Navegar a http://localhost:81/ y usar la webapp

Si aparece algo como "python no se reconoce como un comando externo" o cosas así, revisar que se haya agregado correctamente a la PATH. 

