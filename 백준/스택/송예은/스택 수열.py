n = int(input())
arr = []
stack =[]
currIdx = 0
stackNum = 1
ans = []
isPossible = True

for i in range(1,n+1):
  num = int(input())
  arr.append(num)

while  currIdx < n:
  if arr[currIdx] > stackNum:
    stack.append(stackNum)
    ans.append('+')
    stackNum+= 1
  elif arr[currIdx] == stackNum:
    stack.append(stackNum)
    ans.append('+')
    stack.pop()
    ans.append('-')
    currIdx += 1
    stackNum+=1
  else:
    checkNum = stack.pop()
    ans.append('-')
    if checkNum > arr[currIdx]:
      isPossible = False
      break
    currIdx+= 1

if isPossible == True:
    for i in ans:
        print(i)
else:
    print('NO')