import sys

input = lambda : sys.stdin.readline().rstrip()

s = []
result = []
count = 0
is_possible = True

# 수열은 무조건 오름차순으로 push하므로, 현재 숫자를 파악하기 위해 count 변수 선언
for _ in range(int(input())):
    num = int(input())

    # 일단 입력받은 숫자가 나올때까지 push
    while count < num:
        count += 1
        s.append(count)
        result.append("+")

    # 해당 숫자가 나올 시 pop
    if s[-1] == num:
        s.pop()
        result.append("-")
    # 해당 숫자가 안 나오면 순서가 꼬인 것 -> push, pop 연산으로 만들기 불가능한 수열
    else:
        is_possible = False
        break

print("\n".join(result) if is_possible else "NO")