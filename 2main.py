import random

def rock_paper_scissors():
    # 컴퓨터의 선택 (랜덤이라는 모듈에서 초이스 함수 가져옴)
    computer_choice = random.choice(['가위', '바위', '보'])
    # 사용자의 승, 패, 무승부 횟수를 기록하기 위한 변수
    win = 0
    lose = 0
    draw = 0
   
    while True:        
        # 사용자 입력 받기
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")
       
        # 사용자가 유효한 입력을 했는지 확인
        if user_choice in ['가위', '바위', '보']:
                   
            # 사용자와 컴퓨터의 선택 출력
            print(f"사용자: {user_choice}, 컴퓨터: {computer_choice}")
           
            # 승부 결정
            if user_choice == computer_choice: #무승부출력
                print("무승부!")
                draw += 1
            elif (user_choice == '가위' and computer_choice == '보') or \
                (user_choice == '바위' and computer_choice == '가위') or \
                (user_choice == '보' and computer_choice == '바위'):
                print("사용자 승리!")
                win += 1 #사용자가 이겼을 경우
            else:
                print("컴퓨터 승리!")
                lose += 1 #나머지는 컴퓨터가 이기는경우로
           
            # 게임을 다시 시작할지 묻는 루프
            play_again = input("다시 하시겠습니까? (y/n): ")
            if play_again.lower() == 'y':
                rock_paper_scissors() #continue 로 대체해도되는것 같음
            elif play_again.lower() == 'n':
                print("게임을 종료합니다.")
                break
           
        else:
            print("유효한 입력이 아닙니다.")
            continue
    # 게임 통계 출력 - f string사용
    print(f"승: {win} 패: {lose} 무승부: {draw}")    
   
rock_paper_scissors()
