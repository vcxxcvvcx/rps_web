#가위바위보 웹

from flask import Flask, render_template, request
import random

app = Flask(__name__)

def rock_paper_scissors(user_choice):
    # 컴퓨터의 선택
    computer_choice = random.choice(['가위', '바위', '보'])
    # 승, 패, 무승부 횟수를 기록하기 위한 변수
    win = 0
    lose = 0
    draw = 0

    # 승부 결정
    if user_choice == computer_choice:
        result = "무승부!"
        draw += 1
    elif (user_choice == '가위' and computer_choice == '보') or \
            (user_choice == '바위' and computer_choice == '가위') or \
            (user_choice == '보' and computer_choice == '바위'):
        result = "사용자 승리!"
        win += 1
    else:
        result = "컴퓨터 승리!"
        lose += 1

    return computer_choice, result, win, lose, draw

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice, result, win, lose, draw = rock_paper_scissors(user_choice)
        return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result, win=win, lose=lose, draw=draw)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
