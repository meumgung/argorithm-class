def travle_jym():
    items = [
        ("노트북", 3, 12),
        ("옷", 1, 10),
        ("카메라", 2, 6),
        ("책", 2, 7),
        ("휴대용 충전기", 1, 4)
    ]
    
    wt = [item[1] for item in items]
    val = [item[2] for item in items]
    n = len(items)
    while True:
        try:
            W = int(input("배낭 용량을 입력 하세요: "))
            if W >= 0:
                break
            else:
                print("배낭 용량은 0 이상의 정수여야 합니다.")
        except ValueError:
            print("잘못된 입력입니다. 정수를 입력해주세요.")

    A = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1): 
        current_wt = wt[i-1]
        current_val = val[i-1]
        for w in range(1, W + 1): 
            if w < current_wt:
                A[i][w] = A[i-1][w]
            else:
                valWithout = A[i-1][w]
                valWith = current_val + A[i-1][w - current_wt]
                A[i][w] = max(valWith, valWithout) 

    max_value = A[n][W]
    
    print("\n<프로그램 실행 예시>")
    print(f"최대 만족도: {max_value}")

    selected_items = []
    w = W
    
    for i in range(n, 0, -1):
        if A[i][w] != A[i-1][w]:
            name, current_wt, _ = items[i-1]
            selected_items.append(name) 
            w -= current_wt 

    selected_items.reverse()
    print(f"선택된 물건: {selected_items}")
    
travle_jym()