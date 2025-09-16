# class를 이용해서 단어 맞추기 게임을 할거야
# 기회는 10번이고
# 틀릴 때마다 기회가 1씩 줄어들고
# 기회가 0이 되면 게임이 끝나
# 단어는 랜덤으로 선택할거야
# 기회가 0이 되도 끝나지만 단어를 맞추면 그 즉시 게임이 끝나
# 단어를 맞추면 축하한다고 출력해주고
# 단어를 틀리면 다시 입력하라고 출력해줘
import random
word_list = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift', 'go', 'rust', 'typescript', 'scala']
class WordGuessingGame:
    def __init__ (self, word_list, max_attempts = 10 ):
        self.word_list = word_list
        self.max_attempts = max_attempts
        self.attempts = 0
        self.chosen_word = random.choice(self.word_list)
    def play(self):
        print("단어 맞추기 게임에 오신 것을 환영합니다!")
        
