# 사용자 입력 처리 함수
# 함수이름 get_data()
# 파라메터
    # start : 시작값
    # end   : 종료값
    # input_str : 가이드문구
# return 정수로 변환된 입력값

def get_data():
    while True:
        try:
            h_nmum = int(input('정수를 입력하세요(1~100)'))
            if not 0 <= h_nmum <= 100:
                raise ValueError('1 ~ 100 범위 초과')
        except Exception as e:
            print(f'오류 : {e}')
        else:
            print('수고하셨습니다')
            break
        
number = get_data()

