from collections import deque

def solution(bridge_length, weight, truck_weights):
    crossingQueue = deque()
    truckQueue = deque(truck_weights)
    crossingCount = 0
    time = 1
    truck = truckQueue.popleft()
    crossingQueue.append(truck)
    
    if len(truckQueue) == 0:
        return bridge_length + 1
    
    while crossingQueue:
        print(crossingQueue)
        if len(truckQueue) == 0 :
            if crossingCount == bridge_length:
                crossingQueue.popleft()
                
            else:
                crossingCount += 1
        elif len(crossingQueue) < bridge_length and sum(crossingQueue)+truckQueue[0] <= weight:
            truck = truckQueue.popleft()
            crossingQueue.append(truck)
            
        elif len(crossingQueue) >= bridge_length and sum(crossingQueue)+truckQueue[0] <= weight :
            crossingQueue.popleft()
            truck = truckQueue.popleft()
            crossingQueue.append(truck)
            
        elif sum(crossingQueue)+truckQueue[0] > weight:
            if crossingCount == bridge_length:
                crossingQueue.popleft()
                truck = truckQueue.popleft()
                crossingQueue.append(truck)
                
            else:
                crossingCount += 1
        time +=1

    return time