from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "something "


@app.route('/')
def index():
    if "gold" not in session:
        session["gold"] = int(0)
    return render_template("index.html")


@app.route('/process_money', methods=["POST"])
def process():
    if "message_list" not in session:
        session["message_list"] = []
    session['process'] = request.form['building']

    if session['process'] == 'farm':
        gold = random.randint(10, 20)
        date = datetime.now()
        dt_string = date.strftime("%H:%M:%S %p - %d/%m/%Y")
        session['gold'] += gold
        session['message_list'].append(
            f"<ul><li class='green'>earned {gold} gold(s) from the farm on {dt_string} </li></ul>")

    elif session['process'] == 'cave':
        gold = random.randint(5, 10)
        date = datetime.now()
        dt_string = date.strftime("%H:%M:%S %p - %d/%m/%Y")
        session['gold'] += gold
        session['message_list'].append(
            f"<ul><li class='green'>earned {gold} gold(s) from the cave on {dt_string} </li></ul>")

    elif session['process'] == 'house':
        gold = random.randint(2, 5)
        date = datetime.now()
        dt_string = date.strftime("%H:%M:%S %p - %d/%m/%Y")
        session['gold'] += gold
        session['message_list'].append(
            f"<ul><li class='green'>earned {gold} gold(s) from the house on {dt_string} </li></ul>")

    elif session['process'] == 'casino':
        gold = random.randint(-50, 50)
        date = datetime.now()
        dt_string = date.strftime("%H:%M:%S %p - %d/%m/%Y")
        if gold < 0:
            session['gold'] += gold
            session['message_list'].append(
                f"<ul><li class='red'>lost {gold * (-1) } gold(s) from the casino on {dt_string} </li></ul>")
        else:
            session['gold'] += gold
            session['message_list'].append(
                f"<ul><li class='green'>earned {gold} gold(s) from the casino on {dt_string} </li></ul>")
    return redirect('/')


@app.route("/reset", methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
