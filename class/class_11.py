# isinstance() 함수
# 객체가 특정 클래스의 인스턴스(객체)인지 확인하는 함수
# 사용하는 이유
# 1. 타입 확인: 삼수나 메서드가 특정 클래스의 인스턴스인지 확인할 때 사용
# 2. 다형성 지원: 상속 관계에 있는 클래스들 간에 공통된 인터페이스를 제공할 때 유용
class student:
    def study(self):
        return "공부 중입니다."
class teacher:
    def teach(self):
        return "가르치고 있습니다."

# 리스트에 어떤 객체가 있는지 모를때 특정 인스턴스만 기대할 수 없다.
peoples = [student(), teacher(), student()]
del  peoples[0]
if isinstance(peoples[0], student):
    print(peoples[0].study())
else:
    print(peoples[0].teach())