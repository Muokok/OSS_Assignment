def add(x, y, z):
    return x + y + z

def subtract(x, y):
    return x - y

while True:
    print("\n간단한 계산기")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 종료")

    choice = input("원하는 연산을 선택하세요 (1/2/3): ")

    if choice == '3':
        print("프로그램을 종료합니다.")
        break

    if choice not in ('1', '2'):
        print("잘못된 입력입니다. 1, 2, 3 중 하나를 선택해주세요.")
        continue

    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    num3 = float(input("세 번째 숫자를 입력하세요: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2, num3)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")