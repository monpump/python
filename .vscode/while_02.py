import time

count = 0
while True:
    print(f'{count}초')
    time.sleep(0.5) # 1초간 지연
    count +=1
    if count % 5 == 0:
        is_cotinue = input('To be continue(Y/y) : ')
        if is_cotinue != "Y" and is_cotinue !="y":
            print('program exit')
            break