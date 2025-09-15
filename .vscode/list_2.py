list_a = [1,2,"문자열",True,False]
print(list_a[2][2])
print(list_a[:])  # start_index : end_index-1 # 원본을 복사
print(list_a[:3])
print(list_a[3:])
print(list_a[-2:])
# start index : end index -1 : 1
print(list_a[::2]) # :: 숫자를 쓰면 그 숫자만큼 건너 뛰어서 생성 한다
print(list_a[::-1]) # :: -1을 쓰게 되면 역순으로 나온다.

list_a = [1,2,3]
list_b = [4,5,6]
print(f'list_a + list_b {list_a + list_b})
print(len(list_a))