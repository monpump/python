# 가위 바위 보 게임  (컴퓨터 VS 휴먼)
# 가위 : 1 바위 : 2 보 : 3
# 규칙 : 컴퓨터가 임의로 숫자를 선택     : Ramdon
# 인간이 숫자를 입력                     : input
# 승패를 기록
# 3번마다 계속할 지 물어본다.            : for

import random
com_choice = random.randint(1,3)
# 사용자의 값
human_choice = int(input("입력('1: 가위 2: 바위 3: 보') :"))
# 승패 확인
count = 0
for i in range(100):
rule = ['가위','바위','보']
print(f'당신이 선택한 것은 {rule[human_choice - 1]}입니다.')
print(f'컴퓨터의 선택은{rule[com_choice - 1]}입니다.')
if com_choice == human_choice:
    print('비겼습니다')
else:
    if (com_choice == 1 and human_choice ==2) or\
       (com_choice ==2 and human_choice ==3)or\
       (com_choice ==3 and human_choice ==1):
        print("당신이 이겼습니다.")
    else:
        print("당신이 졌습니다.")