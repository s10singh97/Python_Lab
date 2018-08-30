# Queue using List
ll = []
def push(a):
    ll.append(a)

def delete():
    ll.remove(ll[0])
            
t = 'y'
while(t == 'y'):
    b = int(input('Do you want to\n1. Insert elemnt in stack\n2. Delete element from stack\n3. Print the list\n'))
    if b == 1:
        ff = input('Enter the number\n')
        push(ff)
    elif b == 2:
        delete()
    elif b == 3:
        print(ll)
    else:
        t = input('Do you want to try again(y/n)')