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
get_data(1,10, '정수')