# 가위 바위 보 게임
# 사용자로부터 입력을 받아 컴퓨터와 대결하는 간단한 게임입니다.
# 사용자는 '가위', '바위', '보' 중 하나를 입력하고, 컴퓨터는 무작위로 선택합니다.
# 가위는 1, 바위는 2, 보는 3으로 표현합니다.
# 이러한 규칙을 Class로 구현합니다.
# 게임이 끝나면 계속할지 물어본다
import random
class RockPaperScissors:
    choices = {1: '가위', 2: '바위', 3: '보'}

    def __init__(self):
        self.user_choice = None
        self.computer_choice = None

    def get_user_choice(self):
        while True:
            try:
                choice = int(input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요: "))
                if choice in self.choices:
                    self.user_choice = choice
                    break
                else:
                    print("잘못된 입력입니다. 1, 2, 3 중 하나를 선택하세요.")
            except ValueError:
                print("숫자를 입력하세요.")

    def get_computer_choice(self):
        self.computer_choice = random.randint(1, 3)

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return "비겼습니다!"
        elif (self.user_choice == 1 and self.computer_choice == 3) or \
             (self.user_choice == 2 and self.computer_choice == 1) or \
             (self.user_choice == 3 and self.computer_choice == 2):
            return "이겼습니다!"
        else:
            return "졌습니다!"

    def play(self):
        self.get_user_choice()
        self.get_computer_choice()
        print(f"사용자: {self.choices[self.user_choice]}, 컴퓨터: {self.choices[self.computer_choice]}")
        print(self.determine_winner())
        while True:
            again = input("다시 하시겠습니까? (y/n): ").lower()
            if again == 'y':
                self.play()
                break
            elif again == 'n':
                print("게임을 종료합니다.")
                break
            else:
                print("y 또는 n을 입력하세요.")

RockPaperScissors().play()

