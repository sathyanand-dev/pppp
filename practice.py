
''' a=[]
key=0
n=int(input("Enter the no of values "))
for i in range(0,n):
    b=int(input("Enter the elements "))
    a.append(b)
print(a)

k=int(input("Enter the elements to be searched "))
for i in range(0,n):
    if k==a[i]:
        print("key found")
        key+=1
        print(key)
        print("key is found in",i,"index")
    else:
        print("Key not found") '''
        
'''def bsearch(l,x,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)/2
        mid=int(mid)
        if x==l[mid]:
            return mid
        elif x>l[mid]:
            return bsearch(l,x,mid+1,high)
        else:
            return bsearch(l,x,low,mid-1)

n=int(input("Enter number of elements in list:"))
l=[]
for i in range(n):
    a=int(input("Enter an integer value:"))
    l.append(a)

print("The list is:\n",l)
print("\n\n\nBINARY SEARCH\n")
x=int(input("Enter value to be searched:"))

result=bsearch(l,x,0,len(l)-1)

if result!=-1:
    print("Element is present at index:" + str(result))
else:
    print("Not found.")'''
    
    
def full(pq,n,front,rear):
    if((front==0 and rear==n-1)or(rear==front-1)):
        print("The slot is full!!")
        return 0
    else:
        print("The slot is not full!!")
        return 1
def empty(pq,n,front,rear):
    if(front==-1 and rear==-1):
        print("The slot is empty!!")
        return 0
    else:
        print("The slot is not empty!!")
        return 1
n,pq,i,front,rear=int(input("Enter the total no of slots:")),[],0,-1,-1
for m in range(n):
    pq.append([0,0])
print(pq)
print("Insert the car - 1\nRemove a car - 2\nExit - 3")
while True:
    c=int(input("Enter your choice:"))
    if c==1:
        if full(pq,n,front,rear)==1:
            ele=input("Enter the car number you want to insert:")
            i=int(input("Enter priority:"))
            if(front==-1 and rear==-1):
                front,rear=front+1,rear+1
            elif(rear==n-1 and front!=-1):
                rear=0
            else:
                rear=rear+1
            pq[rear]=[i,ele]
            print("The car",ele,"is inserted successfully!!")
    elif c==2:
        if empty(pq,n,front,rear)==1:
            temp=0
            for i in range(front,rear+1):
                if pq[i][0]>=pq[temp][0]:
                    temp=i
            print("The car",pq[temp][1],"is removed successfully!!")
            pq[temp]=[0,0]
            for i in range(temp,len(pq)-1):
                pq[i]=pq[i+1]
                pq[i+1]=[0,0]
            if(front==rear):
                front=rear=-1
            else:
                if(front==n-1):
                    front=0
                else:
                    rear-=1
    elif c==3:
        break
    else:
        print("Wrong choice!!")
    print(pq)
    print("front:",front,"rear:",rear)
    
''' circular q
def enqueue(front,rear,q):
    if(front==rear):
        print("The circular queue is empty   ")
        k=int(input("Enter the element to be inserted:"))
        rear=rear+1
        q.append(k)
        return k
    elif(rear>front):
        k=int(input("Enter the element to be inserted:"))
        q.append(k)
    elif((rear+1)%len(q)==0):
        print("The circular queue is full")

def dequeue(front,rear,q):
    if(front==rear):
        print("The circular queue is empty")
    else:
        temp=q[front]
        print("The element deleted:",temp)
        return temp
maxsize=int(input("Enter the length of the queue:"))
q=[]
front=rear=0
for i in range(maxsize):
    a=int(input("Enter the operation to be done:\n1.Insertion\n2.Deletion\n3.Exit"))
    if(a==1):
        x=enqueue(front,rear,q)
        rear+=1
        print(q)
    if(a==2):
        e=dequeue(front,rear,q)
        front=-1
        rear=-1
        q.remove(e)
        print(q)
    if(a==3):
        exit '''
