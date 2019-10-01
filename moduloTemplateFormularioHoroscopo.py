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


def calcularHoroscopo():
    pass
