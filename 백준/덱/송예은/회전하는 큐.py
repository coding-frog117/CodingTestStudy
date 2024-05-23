from collections import deque

N,M = map(int,input().split())
location = list(map(int,input().split()))
ans = 0

indexArr = deque()
for i in range(1,N+1):
  indexArr.append(i)

def leftMove(arr):
  num = arr.popleft()
  arr.append(num)
  return arr

def rightMove(arr):
  num = arr.pop()
  arr.appendleft(num)
  return arr

def compareToIdx(arr,i):
  if arr.index(i) > (len(arr) // 2):
    return 'right'
  return 'left'
  
for i in location:
  if i == indexArr[0]:
    indexArr.popleft()
  else:
    # 현재 뽑아야 하는 위치의 index비교
    if compareToIdx(indexArr,i) =='right':
      while True:
        rightMove(indexArr)
        ans += 1

        if indexArr[0] == i:
          indexArr.popleft()
          break
    else:
      while True:
        leftMove(indexArr)
        ans += 1

        if indexArr[0] == i:
          indexArr.popleft()
          break

print(ans)