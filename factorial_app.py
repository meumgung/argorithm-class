import time

# -------------------------------
# 팩토리얼 구현
# -------------------------------

def fact_loop(n: int) -> int:
    """반복문으로 팩토리얼 계산"""
    if n < 0:
        raise ValueError("음수는 안 됩니다.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fact_rec(n: int) -> int:
    """재귀로 팩토리얼 계산"""
    if n < 0:
        raise ValueError("음수는 안 됩니다.")
    if n == 0 or n == 1:
        return 1
    return n * fact_rec(n - 1)


# -------------------------------
# 실행 시간 재기
# -------------------------------
def run_timer(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return result, elapsed


# -------------------------------
# 준비된 숫자들
# -------------------------------
TEST_NUMBERS = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]


# -------------------------------
# 큰 숫자 줄여서 보기
# -------------------------------
def shorten_number(val: int, max_digits: int = 20) -> str:
    s = str(val)
    if len(s) <= max_digits:
        return f"{val:,}"
    return f"{s[:10]}...{s[-10:]} (총 {len(s)}자리)"


def show_result(n, loop_result, loop_time, rec_result, rec_time):
    same = (loop_result == rec_result)
    status = "같음" if same else "다름"
    print(f"n = {n:3d} | {status:6s} | 반복={loop_time:.8f}s | 재귀={rec_time:.8f}s")
    print(f"   [반복] {shorten_number(loop_result)}")
    print(f"   [재귀] {shorten_number(rec_result)}")
    print("-" * 60)


# -------------------------------
# 메뉴
# -------------------------------
def menu():
    last_results = []

    while True:
        print("\n=== 팩토리얼 계산기 ===")
        print("1. 반복문으로 계산")
        print("2. 재귀로 계산")
        print("3. 두 방법 비교")
        print("4. 준비된 숫자들 전부 실행")
        print("s. 최근 결과 저장하기")
        print("q. 종료")
        choice = input("선택: ").strip()

        if choice == "q":
            print("프로그램을 종료합니다.")
            break

        elif choice == "1":
            try:
                n = int(input("n 입력: "))
                result, elapsed = run_timer(fact_loop, n)
                print(f"[반복] {n}! = {shorten_number(result)} (걸린 시간: {elapsed:.8f}s)")
                last_results = [(n, result, elapsed, None, None)]
            except ValueError as e:
                print("오류:", e)

        elif choice == "2":
            try:
                n = int(input("n 입력: "))
                result, elapsed = run_timer(fact_rec, n)
                print(f"[재귀] {n}! = {shorten_number(result)} (걸린 시간: {elapsed:.8f}s)")
                last_results = [(n, None, None, result, elapsed)]
            except ValueError as e:
                print("오류:", e)
            except RecursionError as e:
                print("재귀가 너무 깊습니다:", e)

        elif choice == "3":
            try:
                n = int(input("n 입력: "))
                loop_result, loop_time = run_timer(fact_loop, n)
                rec_result, rec_time = run_timer(fact_rec, n)
                show_result(n, loop_result, loop_time, rec_result, rec_time)
                last_results = [(n, loop_result, loop_time, rec_result, rec_time)]
            except ValueError as e:
                print("오류:", e)
            except RecursionError as e:
                print("재귀가 너무 깊습니다:", e)

        elif choice == "4":
            last_results = []
            print("\n[테스트 숫자 실행]")
            for n in TEST_NUMBERS:
                try:
                    loop_result, loop_time = run_timer(fact_loop, n)
                    rec_result, rec_time = run_timer(fact_rec, n)
                    show_result(n, loop_result, loop_time, rec_result, rec_time)
                    last_results.append((n, loop_result, loop_time, rec_result, rec_time))
                except RecursionError as e:
                    print(f"n={n} 재귀 너무 깊음: {e}")

        elif choice == "s":
            if not last_results:
                print("저장할 실행 결과가 없습니다.")
                continue
            filename = input("저장할 파일명 입력 (예: result.txt): ").strip()
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    for r in last_results:
                        n, lres, ltime, rres, rtime = r
                        f.write(f"n={n}, 반복={lres}, 시간={ltime}, 재귀={rres}, 시간={rtime}\n")
                print(f"결과가 '{filename}' 파일로 저장되었습니다.")
            except Exception as e:
                print("파일 저장 오류:", e)

        else:
            print("잘못된 선택입니다. 다시 입력하세요.")


# -------------------------------
# 시작점
# -------------------------------
if __name__ == "__main__":
    menu()
