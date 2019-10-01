"""
MODULO HORSCOPOS
"""


from wtforms import StringField, validators
from wtforms import Form


class TemplateFormularioHoroscopo(Form):
    anyo = StringField("Año:", validators=[
        validators.data_required(
            message="Estas obligado a rellenar este campo"),
        validators.length(
            min=4, max=5, message="Año no permitido"),
        validators.optional(strip_whitespace=True)
    ], description="Introduce Año:")


class HoroscopoChino():
    ANIMALES_HOROSCOPO_CHINO = {

        1: (("Rata", "rata.svg"), ("Dragon", "dragon.svg"), ("Mono", "mono.svg")),
        2: (("Buey", "buey.svg"), ("Serpiente", "serpiente.svg"), ("Gallo", "gallo.svg")),
        3: (("Tigre", "tigre.svg"), ("Caballo", "caballo.svg"), ("Perro", "perro.svg")),
        4: (("Conejo", "conejo.svg"), ("Cerdo", "cerdo.svg"), ("Cabra", "cabra.svg")),
        5: (("Dragon", "dragon.svg"), ("Rata", "rata.svg"), ("Mono", "mono.svg")),
        6: (("Serpiente", "serpiente.svg"), ("Buey", "buey.svg"), ("Gallo", "gallo.svg")),
        7: (("Caballo", "caballo.svg"), ("Tigre", "tigre.svg"), ("Perro", "perro.svg")),
        8: (("Cabra", "cabra.svg"), ("Conejo", "conejo.svg"), ("Cerdo", "cerdo.svg")),
        9: (("Mono", "mono.svg"), ("Rata", "rata.svg"), ("Dragon", "dragon.svg")),
        10: (("Gallo", "gallo.svg"), ("Buey", "buey.svg"), ("Serpiente", "serpiente.svg")),
        11: (("Perro", "perro.svg"), ("Tigre", "tigre.svg"), ("Caballo", "caballo.svg")),
        12: (("Cerdo", "cerdo.svg"), ("Conejo", "conejo.svg"), ("Cabra", "cabra.svg"))

    }

    def __init__(self, anyo_usuario):
        self.anyo_usuario = anyo_usuario

    def calcularSigno(self):
        try:
            for i in range(0, 12):
                if self.anyo_usuario % 12 == i:
                    return self.ANIMALES_HOROSCOPO_CHINO[i]

        except ValueError:
            return "Error al introducir el año"
