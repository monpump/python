def get_data(start, end,input_str='입력'):
    while True:
        try:
            h_num = int(input(f'{input_str}({start}~{end})'))
            if not start <= h_num <= end:
                raise ValueError(f'{start},{end} 범위초과')
        except Exception as e:
            print(f'오류 : {e}')
        else:
           return h_num



# 랜덤 정수 - 컴퓨터가 선택한 값
import random as rd
start, end = 1, 100
computer = rd.randint(start,end)
count = 0
game_history = []
while True:    
    human = get_data(start, end)
    count += 1
    if human > computer:
        print('크다')
        game_history.append( (human,'크다'))
    elif human < computer:
        print('작다')
        game_history.append(  (human, '작다'))
    else:
        print(f' {count}번째만에 정답')
        for i in range(len(game_history)):
            print(f'{i+1}번째 너가 틀린 이유 : 정답은 {computer}, 너의 답은 : {game_history[i]}')
        break

 
 # 랜덤정수 - 컴퓨터가 선택한 값

import random as rd
import game_utils as gu
start, end = 1, 100

computer = rd.randint(start, end)

count = 0
game_history = []
while True:
    count +=1
    human = gu.get_data(start, end)
# 승자선택 로직
    if gu.check_winner(human, computer, game_history):
        break
