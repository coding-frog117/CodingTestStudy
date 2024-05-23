string = list(input())
stack = []
answer = 0
isValid = True

def checkValidString(stack,openChar,number):
  answer = 0
  if stack[-1] == openChar:
      stack.pop()
      stack.append(number)
      return True
  elif stack[-1].isdigit():
    appendNum = 0
    while stack:
      if stack[-1].isdigit():
        appendNum += stack.pop()
      elif stack[-1] == openChar:
        stack.pop()
        answer += appendNum
      else:
        return False
    return answer
  else :
    return False
  
for i in string:
  if i == '(' or i == '[':
    stack.append(i)
  elif i == ')' :
    returnValue = checkValidString(stack,'(',2)
    if returnValue == False:
      isValid = False
      break
    else:
      answer += returnValue
      
    # ']' 일 때 체크해야함