# 명령어는 모드 실행
# 조건문을 이용하면 특정 명령문은 실행되지 않게 할 수 있다.
# 조건문은 if 조건 : 반드시 : 있어야된다.
# 들여쓰기를 해서 if에 하위 명령어로 만든다. --> 이걸 블럭이라고 부른다
age = int(input()"나이가 몇이냐"})
if age >= 18:
    print('성인입니다.')
    print('조건문은 True 입니다.')

#
#
#
print('if와 상관 없는 명령어')

# 조건에 맞으면 합격 그렇지 않으면 불합격
socre = 30

if score >= 60:
    print('합격')
else:    
    print('불합격')

temperatur = 25
if temperatur > 30:
    print('덥다')
elif temperatur > 20:
    print('따뜻하다')
else:
    print('춥다')