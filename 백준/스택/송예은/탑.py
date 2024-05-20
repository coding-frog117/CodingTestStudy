N = int(input())
arr = []
topStack =[]
currStack =[]
ans = []

for i in range(1,N+1):
    num = int(input())
    ans.append(num)

for idx in range(len(arr)):
  print(topStack)
  print(currStack)
  if len(topStack) == 0 and len(currStack) == 0:
    ans.append(0)
    topStack.append([arr[idx],idx+1])
    currStack.append([arr[idx],idx+1])

  elif arr[idx] < currStack[-1][0] :
    ans.append(currStack[-1][1])
    currStack.append([arr[idx], idx + 1])

  elif arr[idx] > currStack[-1][0] and arr[idx] < topStack[-1][0]:
    ans.append(topStack[-1][1])
    currStack.append([arr[idx], idx + 1])

  elif arr[idx] > topStack[-1][0] :
    ans.append(idx+1)
    topStack.append([arr[idx],idx+1])


print(ans)