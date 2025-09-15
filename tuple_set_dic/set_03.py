import random
list_a = random.sample(range(11), 7) # 0~10 중복되지 않은 임의이 7개
list_b = random.sample(range(11), 7)

# 중복을 허용하면서 0 ~ 10 임의의 7개 추출
# random.randint(0,10)
list_c = []
for i in range(7):
    list_c.append(random.randint(0,10))
    print(list_c)
# 교집합
    # 연산자 | (파이프 연산자) --> or
set_a = {1,2,3,}
set_b = {3,4,5}
union_set = set_a | set_b
print(union_set)
    # 메서드 .union()
union_set = set_a.union(set_b)
# 교집합
set_a, set_b = {1,2,3,4},{2,3,5}
    # 연산자 &   --> and
print(set_a  & set_b)    
    # 메서드 .intersection()
print(set_a.intersection(set_b))
# 차집합
    # 연산자 -
print(set_a - set_b)
    # 메서드 