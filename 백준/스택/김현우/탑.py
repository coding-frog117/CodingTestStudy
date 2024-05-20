import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
li = list(map(int, input().split()))

# 왼쪽에 있는 빌딩들과 높이비교 -> stack의 pop 연산으로 이해가능
# s : (빌딩 인덱스, 빌딩 높이) 형태로 저장
s = []
ans = [0 for _ in range(n)]

for i in range(n):
    # 왼쪽에 있는 빌딩 높이가 현재 높이보다 높아질때까지 pop
    while s and s[-1][1] <= li[i]:
        s.pop()

    # 더 높은 빌딩이 있다면 ans에 해당 빌딩위치(인덱스) 갱신
    if s:
        ans[i] = s[-1][0]

    # 현재 빌딩정보 stack에 push
    s.append((i+1, li[i]))

print(*ans)