# 직원 Employee - 아이디, 이름, 기본급
class Employee:
    def __init__(self,id,name,base_salary):
        self.id = id
        self.name = name
        self._base_salary = base_salary # private의 의미로 사용
    @property
    def base_salary(self):
        return self._base_salary
    @base_salary.setter
    def base_salaty(self, money):
        if money > 0:
            self._base_salary = money
        else:
            raise ValueError('금액은 양수입니다.  마이너스 불가')
    def emp(self):
        print('직원클래스')    

    def __str__(self):
        return f'{self.name} : {self.id},{self.base_salary}'

# 정규직 FullTimeEmployee - 보너스
class FullTimeEmployee(Employee):
    def __init__(self,id,name,base_salary,bonus):
        super().__init__(id,name,base_salary)
        self.bonus = bonus
    # bonus도 마이너스 입력 불가
    def __str__(self):
        return super().__str__() + f', {self.bonus}'
    def show_class(self):
        print('정규직 클래스')
# 계약직 PartTimeEmployee - 시간당 급여
class PartTimeEmployee(Employee):
    def __init__(self,id,name,hourly_rate,hours):
        super().__init__(id,name,0)
        self.hourly_rate = hourly_rate
        self.hours = hours
# hourly_rate  hours : getter setter
    def __str__(self):
        return f'{self.name} {self.id} {self.hourly.rate} {self.hours}'
    def show_class(self):
        print('계약직 클래스')
# 인턴 Intern - 고정수당
class Intern(Employee):
    def __init__(self,id,name,fixed_salary):
        super().__init__(id,name,0)
        self.fixed_salary = fixed_salary
    def __str__(self):
        return f'{self.name}{self.id}{self.fixed_salary}'
    def show_class(self):
        print('인턴클래스')


# 정규직 직원, 계약직, 인턴을 모두 리스트에 섞어서 객체를 저장
emp = [
    FullTimeEmployee(1,'철수',100,50),
    PartTimeEmployee(2,'영수',8,8),
    Intern(3,'걸수',50),
    FullTimeEmployee(4,'경수',150,40),
    PartTimeEmployee(5,'함수',8,10),
    Intern(6,'상수',40),
    ]
# for e in emp:
#     if isinstance(e, FullTimeEmployee):
#         e.fte()
#     elif isinstance(e, PartTimeEmployee):
#         e.pte()
#     elif isinstance(e, Intern):
#         e.int()
#     else:
#         e.emp()
        
# emp에 들어있는 직원이 각각 어떤클래스인지 순환문을 이용해서 각 클래스의 int, pte 메소드 호출해서 출력
for e in emp:
    e.show_class() # emp리스트의 각각의 객체에 해당하는 메소드를 호출 다형성