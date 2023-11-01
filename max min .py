def Max(T):
    max=T[0]
    for i in range(len(T)):
        if max < T[i]:
            max = T[i]
    return max

def Min(T):
    min=T[0]
    for i in range(len(T)):
        if min > T[i]:
            min = T[i]
    return min

def reverse(T):
    x=[]
    for i in range(len(T)-1,-1,-1):
     x.append(T[i])
    return x

T=[]

n=int(input("enter the lenght of the list:  "))

for i in range(n):
    T.append(int(input(f"enter the value of case number {i+1}  ")))

print(f"the max is {Max(T)}  and the min is {Min(T)}, and the reverse of the list is {reverse(T)}")    