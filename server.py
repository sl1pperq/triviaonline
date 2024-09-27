from random import shuffle
import requests, json, random


def get_trivia(q, diff):
    url = f'https://opentdb.com/api.php?amount={q}'
    if diff != None:
        url += f'&difficulty={diff}'
    print(url)
    res = requests.get(url).json()
    return res['results']

def get_trivia_question(trivia, num):
    current = trivia[num - 1]
    incorrect = current['incorrect_answers']
    correct = current['correct_answer']
    answers = connect_questions(correct, incorrect)
    return current, answers, correct

def connect_questions(correct, incorrect):
    new = incorrect
    if correct not in new:
        new.append(correct)
    shuffle(new)
    return new

def get_random_questions():
    return random.randint(3, 20)