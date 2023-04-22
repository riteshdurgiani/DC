def print_load(load):
    print()
    print('***** Current Load of System *****')
    for i in range(len(load)):
        print(f'Server {i+1} load : {load[i]} processes')
    print()

def balance_load(n,p):
    load = [0]*n
    for i in range(p):
        load[i%len(load)] += 1
    return load

n = int(input('Enter number of servers : '))
p = int(input('Enter number of processes : '))

while True:
    load = balance_load(n,p)
    print_load(load)
    print('1. Add Servers')
    print('2. Add Processes')
    print('3. Remove Servers')
    print('4. Remove Processes')
    print('5. Exit')
    opt = int(input('Select an option : '))

    if opt == 1:
        change = int(input('Enter number of servers to add : '))
        n += change
    if opt == 2:
        change = int(input('Enter number of processes to add : '))
        p += change
    if opt == 3:
        change = int(input('Enter number of servers to remove : '))
        n -= change
    if opt == 4:
        change = int(input('Enter number of processes to remove : '))
        p -= change
    if opt == 5:
        break
