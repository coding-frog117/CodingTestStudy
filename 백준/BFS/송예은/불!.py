from collections import deque

R,C = map(int,input().split())
maps = []
initqueue = deque()
firequeue = deque()

for i in range(R):
  inp = list(input().split())
  maps.append(inp)

  for j in range(C):
    if inp[j] == 'J':
      initqueue.append([i,j])
      maps[i][j] = 0
    elif inp[j] == 'F':
      firequeue.append([i,j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while initqueue:
  y,x = initqueue.popleft()
  if y == R-1 or x == C-1 :
    print(maps[y][x]+1)
    break

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
  
    if nx<0 or nx >= C or ny < 0 or ny >= R:
      continue
    
    if maps[ny][nx] == '.':
      initqueue.append([ny,nx])
      maps[ny][nx] = maps[ny][nx] + 1