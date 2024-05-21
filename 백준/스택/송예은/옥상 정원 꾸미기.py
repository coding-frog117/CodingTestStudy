N = int(input())
buildings = []
stack =[]
ans = 0

for i in range(N):
    building = int(input())
    buildings.append(building)

for i in range(len(buildings)-1,-1,-1):
    if len(stack) == 0:
        stack.append([buildings[i],i+1])
    else :
        while len(stack) > 0:
            if stack[-1][0] < buildings[i]:
                stack.pop()
            else :
                break

        stack.append([buildings[i],i+1])

        if len(stack) == 1:
            ans += len(buildings) -i-1
        else:
            ans += stack[-2][1] - i-1-1
print(ans)