# 논리 연산자 사용
# 나이가 18이상(성인) 이면서 주민번호를 가진사람은 "입장가는"  "입장불가"
# 논리 연산자 사용
# 나이가 18세(성인) 이상이면서 신분증이 있는 경우에만 "입장 가능"
# 그 외에는 "입장 불가"

age = int(input("나이를 입력하세요: "))
id_input = input("신분증이 있습니까? (y/n): ")

# 입력값을 True/False 로 변환
if id_input.lower() == "y":
    has_id = True
else:
    has_id = False

if age >= 18 and has_id:
    print("입장 가능")
else:
    print("입장 불가")
