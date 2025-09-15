# 다양한 매개변수
    #기본매개변수 default parameter

def  myadd(num1, num2 = "안녕"):
    return num1 + num2

result = myadd("그래")
print(f'result = {result}')