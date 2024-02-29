import random

def up_down_game():
    # 랜덤 숫자 생성을 위한 random 모듈
    random_number = random.randint(1, 100)
    attempts = 0


    while True:
        try:
            guess = int(input("숫자를 입력하세요: "))
            if guess < 1 or guess > 100:
                print("1부터 100 사이의 숫자를 입력하세요.")
                continue
        except ValueError:
            print("유효한 범위내 숫자를 입력하세요.")
            continue
        attempts += 1

        if guess < random_number:
            print("업!")
        elif guess > random_number:
            print("다운!")
        else:
            print(f"맞았습니다. 시도한 횟수: {attempts}")
            break
       
    while True:  # 게임을 다시 시작할지 묻는 루프
        play_again = input("다시 하시겠습니까? (y/n): ")
        if play_again.lower() == 'y':
            up_down_game()  # 게임 재시작
        elif play_again.lower() == 'n':
            print("게임을 종료합니다.")
            break
   
up_down_game()
