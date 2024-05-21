#풀이 방법이 같은데 틀린 이유 모르겠음

N = int(input())
stack =[]
ans = []

numbers = list(map(int,input().split()))

for i in range(len(numbers)-1,-1,-1):
    print(stack,ans)
    if len(stack) == 0:
        stack.append([numbers[i],i+1])
        ans.append(-1)
    else :
        while len(stack) > 0:
            if stack[-1][0] < numbers[i]:
                stack.pop()
            else :
                break

        stack.append([numbers[i],i+1])

        if len(stack) == 1:
            ans.append(-1)
        else:
            ans.append(stack[-2][0])
print(*ans[::-1])