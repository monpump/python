# 클래스 콜백함수
#  __eq__ : ==
#  __ne__ : !=
#  __lt__ : <  A less than B
#  __gt__ : >  A greater than B
#  __le__ : <= A less than or equal to B
#  __ge__ : >= A greater than or equal to B
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return f"이름: {self.name}, 점수: {self.score}"    

    def __eq__(self, other):
        print("__eq__ 호출")
s1 = Student("홍길동", 90)
s2 = Student("홍길동", 90)
s1 == s2
print(s1) 