from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form for adding a new pet to the db"""

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('dog', 'Dog'), ('cat', 'Cat'), ('prc', 'Porcupine')], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age (Years)", validators=[InputRequired(), NumberRange(min=0, max=30, message="Age must be between 0 and 30 years")])
    notes = StringField("Notes", validators=[Optional()])