import sys

input = lambda : sys.stdin.readline().rstrip()

w = input()
s = []     # 스택
ans = 0    # 괄호값 총합
count = 1  # 괄호값 중간계산용 카운트

for i in range(len(w)):
    # '('일 때
    if w[i] == '(':
        s.append('(')
        count *= 2
    # '['일 때
    elif w[i] == '[':
        s.append('[')
        count *= 3
    # ')'일 때 -> 괄호값 갱신
    elif w[i] == ')':
        # 올바른 괄호열이 아니면 0 출력후 프로그램 종료
        if not s or s[-1] != '(':
            print(0)
            exit(0)
        if w[i-1] == '(':
            ans += count
        s.pop()
        count //= 2
    # ']'일 때 -> 괄호값 갱신
    elif w[i] == ']':
        # 올바른 괄호열이 아니면 0 출력후 프로그램 종료
        if not s or s[-1] != '[':
            print(0)
            exit(0)
        if w[i-1] == '[':
            ans += count
        s.pop()
        count //= 3

# 올바른 괄호열이 아니면 0 출력후 프로그램 종료
print(0 if s else ans)