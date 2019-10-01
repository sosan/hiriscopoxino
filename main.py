
import os
from flask import Flask, render_template, make_response, abort, redirect, url_for, request
from wtforms import StringField, validators

from moduloTemplateFormularioHoroscopo import TemplateFormularioHoroscopo


# instancias
app = Flask(__name__)
app.config["SECRET_KEY"] = "ssscetiro"


HOROSCOPO = {
    1: (("Rata", "rata.svg"), ("Compatibilidad1", "imagen.svg"), ("Compatibliidad2", "imagen.svg")),
    2: (("Buey", "buey.svg"), ("Compatibilidad1", "imagen.svg"), ("Compatibilidad2", "imagen.svg")),
    2: (("Caballo", "caballo.svg"), ("Compatibilidad1", "imagen.svg"), ("Compatibilidad2", "imagen.svg")),


}


@app.route("/", methods=["GET", "POST"])
def home():

    if request.methods == "POST":
        return "POST"
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run("127.0.0.1", 5000, debug=True)
