# Call Center Queue

queue = []

# Add a call
def addCall(customerID, callTime):
    queue.append([customerID, callTime])
    print("Call added successfully")


# Answer a call
def answerCall():
    for i in range(0 ,len(queue)):
     if len(queue) == 0:
        print("Queue is empty")
     else:
        call = queue.pop(0)
        print("Answered call:", call)


# View queue
def viewQueue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Calls in queue:")
        for call in queue:
            print("Customer ID:", call[0], "Call Time:", call[1])


# Check if queue is empty
def isQueueEmpty():
    return len(queue) == 0


# Main program
addCall("C101", 5)
addCall("C102", 10)
addCall("C103", 15)

viewQueue()

answerCall()

viewQueue()

print("Queue empty:", isQueueEmpty())