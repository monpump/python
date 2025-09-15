# 사용자로부터 점수를 입력받아서 A B C D F 학점을 출력
score =int(input('총점을 입력하세요'))
print(f'score = {score}')
if score>80:
    print('A')
elif score>60:
    print('B')
elif score>40:
    print('C')
elif score>20:
    print('D')
else:
    print('F')
