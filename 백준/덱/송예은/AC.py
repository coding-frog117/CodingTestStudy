from collections import deque
T = int(input())

for i in range(T):
  p = list(input().split())
  n =int(input())
  arr = deque(input())

  for i in p:
    if i == 'R':
      arr.reverse()
    elif i == 'D':
      if len(arr) > 0 :
        print('error')
        break
      else:
        arr.popleft()
  print(arr)