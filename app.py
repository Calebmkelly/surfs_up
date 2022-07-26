from flask import Flask

app = Flask(__name__)

@app.route('/')
def skill_drill():
    numbers = [1, 2, 3, 4]
    multiply_two = [number*2 for number in numbers]
    return f'{multiply_two}'