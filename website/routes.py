from requests import post as ps
from .forms import New, Send
from flask import Blueprint, render_template, url_for, redirect, flash
from .models import Tele
from . import db

routes = Blueprint("rotes", __name__)


@routes.route("/", methods=['GET', 'POST'])
def home():
  Ffrom = New()
  if Ffrom.validate_on_submit():
    Ffrom.username.data = str(Ffrom.username.data).replace('@', '')
    Ffrom.username.data = Ffrom.username.data.lower()
    user_query = Tele.query.filter_by(user=Ffrom.username.data).first()
    if not user_query:
      db.session.add(
        Tele(user=Ffrom.username.data,
             token=Ffrom.tg_token.data,
             iid=Ffrom.iid.data))
      db.session.commit()
      #flash("New Page Done!")
      return redirect(url_for('rotes.show', tguser=Ffrom.username.data))

    else:
      flash("This Username Is Taken!", category="error")
  return render_template('home.html', form=Ffrom)


@routes.route("/<tguser>/", methods=['GET', 'POST'])
def show(tguser):
  tguser = tguser.lower()
  Ffrom = Send()
  user_query = Tele.query.filter_by(user=tguser).first()
  if not user_query: return render_template('notfound.html')

  if Ffrom.validate_on_submit():
    text = Ffrom.data.data
    if len(text) > 199: flash("This Message is long", category="error")
    else:
      req = send(token=user_query.token, msg=text, _id=user_query.iid)
      if not req: flash("Something went wrong", category="error")
      else: flash("Sent!")

  return render_template('show.html', tguser=user_query, form=Ffrom)


def send(token, _id, msg):
  req = ps(
    f"https://api.telegram.org/bot{token}/sendMessage?chat_id={_id}&text={msg}"
  )
  if req.ok: return True
  return False
