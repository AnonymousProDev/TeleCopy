from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, length

class New(FlaskForm):
    tg_token = StringField("Telegram Bot Token", validators=[DataRequired(message="Telegram token messing")], render_kw={"placeholder": "5702266381:AAFu5yvNKE....."})
    username = StringField("Telegram Username", validators=[DataRequired(message="Telegram username messing")], render_kw={"placeholder": "@I01270"})
    iid = IntegerField("Telegram Id", validators=[DataRequired(message="Telegram id messing")], render_kw={"placeholder": "5778579..."})
    captcha = RecaptchaField()
    submit = SubmitField("Submit")
    
class Send(FlaskForm):
    data = TextAreaField("Your Message", validators=[DataRequired(), length(max=200)], render_kw={"placeholder": "How are you!"})
    captcha = RecaptchaField()
    submit = SubmitField("Submit")