from queues import BoundedQueue
from queues import CircularQueue
import time

def calculateTime(num,method):
    # for loop to calculate time
    # method is the queue method, i.e. Bounded and circular queue.
    for i in range(num):
        method.enqueue(i)
    begin = time.time()
    for j in range(num):
        method.dequeue()
    end = time.time()
    duration = end - begin
    return duration

def main():
    capacity = 50000
    bq = BoundedQueue(capacity)  # the big-O time efficiency of the dequeue for bq is O(n) since we remove the first one and then fills up the position
    cq = CircularQueue(capacity) # the big-O time efficiency of the dequeue for bq is O(1) because we remove the first item without changing the remaining items' position.
    print('For Bounded Queue, the total runtime of dequeuing ' + str(capacity) + ' items is: ' + str(calculateTime(capacity,bq)) + ' seconds.') 
    print('For Circular Queue, the total runtime of dequeuing ' + str(capacity) + ' items is:' + str(calculateTime(capacity,cq)) + ' seconds.')

main()