from flask import *
from server import *

app = Flask(__name__)
app.secret_key = 'trivia_game'

@app.route('/')
def main_root():
    return render_template('promo.html', num=get_random_questions())

@app.route('/start')
def start_root():
    q = int(request.args.get('q'))
    diff = request.args.get('difficulty')
    res = get_trivia(q, diff)
    session['trivia'], session['number'], session['counter'], session['len'] = res, 1, 0, q
    session['answers'] = []
    return redirect('/trivia')

@app.route('/trivia')
def trivia_root():
    tr, num, len = session['trivia'], session['number'], session['len']
    question, answers, correct = get_trivia_question(tr, num)
    session['correct'] = correct
    return render_template('index.html', question=question, num=num, answers=answers, len=len)

@app.route('/check', methods=['POST'])
def trivia_check():
    answer = request.form.get('answer')
    if answer == session['correct']:
        session['counter'] += 1
        session['answers'].append({"text": answer, "correct": True})
    else:
        session['answers'].append({"text": answer, "correct": False})
    session['number'] += 1
    if session['number'] == session['len'] + 1:
        return render_template('final.html', score=session['counter'], len=session['len'], answers=session['answers'])
    return redirect('/trivia')

app.run(port=5090)