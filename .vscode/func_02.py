# 매개변수 O, 반환값 O
# 매개변수 O, 반환값 X
# 매개변수 X, 반환값 O
# 매개변수 X, 반환값 X

# 만들고 사용해 보기
def one(a, b, c):
    return a+b+c
print(one(8,7,6))

def two(d,e,f):
    print('def입력받음')

two(3,4,'v')

def three():
    return 8

print(three())

def four():
    print()

four()

def say_hello():
    print('안녕')

print(say_hello)

print(say_hello()) # say_hello 만으로도 안녕이되고 print는 출력값이 없어서 none이 나온다
say_hello()