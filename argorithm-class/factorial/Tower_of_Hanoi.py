def hanoi_tower(n, start, tmp, target):
    if n == 1:
        print(f"원반 {n}: {start} -> {target}")
        return
    
    hanoi_tower(n-1, start, target, tmp) #위의 n-1개를 start -> tmp로 옮김(target을 임시 보조 사용)
    print(f"원반 {n}: {start} -> {target}")
    hanoi_tower(n-1, tmp, start, target)

if __name__ == "__main__":
    hanoi_tower(3, "A", "B", "C")