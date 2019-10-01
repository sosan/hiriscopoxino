
import os
from flask import Flask, render_template, make_response, abort, redirect, url_for, request
from wtforms import StringField, validators

from moduloTemplateFormularioHoroscopo import TemplateFormularioHoroscopo
from horoscopo import


# instancias
app = Flask(__name__)
app.config["SECRET_KEY"] = "ssscetiro"


HOROSCOPO = {
    1: (("Rata", "rata.svg"), ("Compatibilidad1", "imagen.svg"), ("Compatibliidad2", "imagen.svg")),
    2: (("Buey", "buey.svg"), ("Compatibilidad1", "imagen.svg"), ("Compatibilidad2", "imagen.svg")),
    2: (("Caballo", "caballo.svg"), ("Compatibilidad1", "imagen.svg"), ("Compatibilidad2", "imagen.svg")),


}

# shift + alt + f



@app.route("/", methods=["GET", "POST"])
def home():

    formulario = TemplateFormularioHoroscopo(request.form)
    if request.method == "POST":

        try:
            anyoInt = int(calcularHoroscopo(request.form.anyo))

            context = {}
            return "POST"
            return render_template("bicho.html", datos=context)
        except ValueError:
            abort(404)

    else:
        print("else")
        return render_template("index.html", dataForm=formulario)


@app.route("/signo", methods=["POST"])
def signo():
    return render_template("signo.html")


def calcularHoroscopo(anyo):
    calculo = 0
    error = False

    return (error, calculo)


if __name__ == '__main__':
    app.run("127.0.0.1", 5000, debug=True)
