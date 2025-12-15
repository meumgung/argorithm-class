def stairs():
    while True:
        try:
            n = int(input("계단의 개수를 입력하시오: "))
            if n >= 0:
                break
            else:
                print("계단의 개수는 0 이상의 정수여야 합니다.")
        except ValueError:
            print("잘못된 입력입니다. 정수를 입력해주세요.")

    if n == 0:
        result = 1
    elif n == 1:
        result = 1
    elif n == 2:
        result = 2
    else:
        table = [0] * (n + 1)
        table[1] = 1 
        table[2] = 2 

        for i in range(3, n + 1):
            table[i] = table[i-1] + table[i-2]
            
        result = table[n]

    print(f"{n}개의 계단을 오르는 방법의 수는 {result}입니다.")

stairs()