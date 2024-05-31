from collections import deque

M,N = map(int,input().split())
box = []
emptyCount = 0
queue = deque()
seen = []
answer = 0

for i in range(N):
  tomato = list(map(int,input().split()))

  box.append(tomato)

isZero = False
isOne = False

for i in range(N):
  for j in range(M):
    if box[i][j] == 1:
      isOne = True
      queue.append([i,j,0])
    elif box[i][j] == 0 :
      isZero = True
    elif box[i][j] == -1:
      emptyCount += 1

if isZero == False :
  print(0)
  exit()
if isOne == False:
  print(-1)
  exit()

dx = [1,-1,0,0]
dy = [0,0,1,-1]
reachCount = len(queue)

while queue:
  [y,x,day] = queue.popleft()
  seen.append([y,x])
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]

    if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue

    if box[ny][nx]== -1 and [ny,nx] not in seen:
        seen.append([ny,nx])
        continue

    if box[ny][nx] == 0 and [ny,nx] not in seen:
        queue.append([ny,nx,day+1])
        reachCount+=1
        box[ny][nx] = 1

  if len(queue) ==0 :
      answer = max(answer,day)
      print(reachCount,emptyCount)

if (reachCount+emptyCount) == M*N:
    print(answer)
else:
    print(-1)