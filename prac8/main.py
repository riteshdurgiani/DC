n = int(input("Enter number of processes : "))
r = int(input("Enter number of resources : "))
alloc = [[0] * r for _ in range(n)]
mx = [[0] * r for _ in range(n)]
need = [[0] * r for _ in range(n)]
avail = [0] * r
safe = []

for i in range(r):
    avail[i] = int(input(f"Enter total number of available instances of resource {i+1} : "))
print()

for i in range(n):
    print(f"Enter information for Process {i+1} : ")
    for j in range(r):
        mx[i][j] = int(input(f"Enter max demand of instances of resource {j+1} for Process {i+1} : "))
        need[i][j] = mx[i][j]
        alloc[i][j] = int(input(f"Enter number of instances of resource {j+1} allocated to Process {i+1} : "))
        need[i][j] -= alloc[i][j]
        avail[j] -= alloc[i][j]
    print()

def display(mx, alloc, need, avail):
    print('Available Resources : ',avail)
    print('Allocated Matrix :- ')
    print(alloc)
    print()
    print('Max Matrix :- ')
    print(mx)
    print()
    print('Need Matrix :- ')
    print(need)
    print()

def bankers(n,r,mx,alloc,need,avail):
    print('***** Initially *****')
    display(mx,alloc,need,avail)

    while True:
        mark = True

        for i in range(n):
            if i+1 in safe:
                continue

            mark = True
            for j in range(r):
                if need[i][j] > avail[j]:
                    mark = False
                    break

            if mark:
                safe.append(i+1)
                for j in range(r):
                    avail[j] += alloc[i][j]
                    alloc[i][j] = 0
                    need[i][j] = '-'

                print(f'***** After allocating resources to P{i+1} *****')
                print(f'P{i + 1} can be allocated resources for execution..')
                display(mx,alloc,need,avail)
                print()
                break

        if not mark:
            print("System is NOT in safe state !!")
            break
        if len(safe) == n:
            print("System is in safe state !!")
            print("Safe Sequence is : ", end=" ")
            for i in safe:
                print(f"P{i}", end=" ")
            print()
            break

bankers(n,r,mx,alloc,need,avail)
