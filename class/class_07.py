# 클래스 변수와 인스턴스 변수의 차이를 보여주는 예제
class BankAccount:
    # 클래스 변수 - 모든 계좌가 공유하는 변수
    bank_name = "파이썬 은행"  # 은행 이름
    interest_rate = 0.05    # 이자율
    total_accounts = 0      # 전체 계좌 수

    def __init__(self, owner, balance):
        # 인스턴스 변수 - 각 계좌마다 다른 값을 가짐
        self.owner = owner      # 계좌 주인
        self.balance = balance  # 계좌 잔액
        BankAccount.total_accounts += 1  # 계좌가 생성될 때마다 전체 계좌 수 증가

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}님의 계좌에 {amount}원이 입금되었습니다.")
        print(f"현재 잔액: {self.balance}원")

# 계좌 생성
account1 = BankAccount("홍길동", 10000)
account2 = BankAccount("김철수", 20000)
account3 = BankAccount("이영희", 30000)

print("\n=== 인스턴스 변수 확인 ===")
print(f"홍길동님 계좌 잔액: {account1.balance}원")
print(f"김철수님 계좌 잔액: {account2.balance}원")
print(f"이영희님 계좌 잔액: {account3.balance}원")

print("\n=== 클래스 변수 확인 ===")
print(f"은행 이름: {BankAccount.bank_name}")
print(f"기본 이자율: {BankAccount.interest_rate * 100}%")
print(f"총 계좌 수: {BankAccount.total_accounts}개")

print("\n=== 클래스 변수 변경 후 ===")
BankAccount.interest_rate = 0.06  # 이자율 변경
print(f"변경된 이자율: {BankAccount.interest_rate * 100}%")
print(f"account1의 이자율: {account1.interest_rate * 100}%")
print(f"account2의 이자율: {account2.interest_rate * 100}%")
print(f"account3의 이자율: {account3.interest_rate * 100}%")

print("\n=== 인스턴스 변수 변경 (입금) ===")
account1.deposit(5000)  # 홍길동님 계좌에 입금
print(f"다른 계좌 잔액 (변동 없음)")
print(f"김철수님 계좌: {account2.balance}원")
print(f"이영희님 계좌: {account3.balance}원")