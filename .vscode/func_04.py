# 다양한 매개변수
    #기본매개변수 default parameter

def  myadd(num1, num2 = 0, num3 = 0):
    return num1 + num2 + num3

result = myadd(10,20,10)
print(f'result = {result}')