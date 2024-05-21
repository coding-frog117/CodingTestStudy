N = int(input())
ans =[]
topStack =[]
currStack =[]

arr = list(map(int,input().split()))

for idx in range(len(arr)):
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
    ans.append(0)
    topStack.append([arr[idx],idx+1])
    currStack.append([arr[idx], idx + 1])

print(' '.join(map(str,ans)))