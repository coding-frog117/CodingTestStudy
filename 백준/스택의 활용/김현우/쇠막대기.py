import sys

input = lambda : sys.stdin.readline().rstrip()

w = input()

count = 0 # 잘려진 쇠막대기 개수
depth = 0 # 현재 괄호 깊이

for i in range(len(w)):
    # 괄호가 열릴 때
    if w[i] == '(':
        if w[i-1] == '(':
            depth += 1
    # 괄호가 닫힐 때 -> 잘린 쇠막대기 카운트 갱신
    else:
        # 바로 직전에 괄호 열렸을 때 -> 현재 depth만큼 쇠막대기 생김
        if w[i-1] == '(':
            count += depth
        # 바로 직전에 괄호 닫혔을 때 -> 쇠막대기는 딱 하나 더 생김, depth는 갱신
        else:
            depth -= 1
            count += 1

print(count)