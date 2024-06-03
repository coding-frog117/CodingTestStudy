string = list(input())
stack = []
answer = 0

for i in range(len(string)):
  if string[i] == '(':
    stack.append('(')
  else :
    if stack and string[i-1] == '(':
      stack.pop()
      answer += len(stack)
    else :
      stack.pop()
      answer += 1
print(answer)