import io
from flask import Flask, render_template, request, send_file
from firmador import firmar

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template("formulario.html")


@app.route('/procesar',  methods=['POST'])
def procesar():
    pdf = request.files.get("pdf")
    firma = request.files.get("firma")
    contraseña = request.form.get("palabra_secreta")
    archivo_pdf_para_enviar_al_cliente = io.BytesIO()
    try:
        datau, datas = firmar(contraseña, firma, pdf)
        archivo_pdf_para_enviar_al_cliente.write(datau)
        archivo_pdf_para_enviar_al_cliente.write(datas)
        archivo_pdf_para_enviar_al_cliente.seek(0)
        return send_file(archivo_pdf_para_enviar_al_cliente, mimetype="application/pdf",
                         download_name="firmado" + ".pdf",
                         as_attachment=True)
    except ValueError as e:
        return "Error firmando: " + str(e) + " . Se recomienda revisar la contraseña y el certificado"


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=81)
