import datetime

n = int(input('Enter number of sites : '))
deferred = {i: [] for i in range(n)}
cs_available = True
requesting = {i: [False,'-'] for i in range(n)}
executing = {i: False for i in range(n)}
replies = {i:0 for i in range(n)}

def request_cs(site):
    if replies[site] > 0:
        print(f'Site S{site} has already requested for CS...')
        return

    timestamp = input('Enter timestamp of REQUEST (HH:MM) : ')
    timestamp = datetime.datetime.strptime(timestamp, '%H:%M').time()
    print(f'Site S{site} requests for CS at timestamp : {timestamp}')
    requesting[site] = [True, timestamp]

    for i in range(n):
        if i == site:
            continue

        print(f'S{site} sends REQUEST message to S{i}')

        if executing[i]:
            print(f'S{i} is currently executing CS...')
            print(f'S{i} has DEFERRED S{site} REQUEST')
            deferred[i].append(site)

        elif requesting[i][0]:
            print(f'S{i} has also REQUESTED for CS at timestamp : {requesting[i][1]}')
            if requesting[i][1] > timestamp:
                print(f'S{i} sends REPLY message to S{site}...')
                replies[site] += 1
            else:
                print(f'S{i} has DEFERRED S{site} REQUEST')
                deferred[i].append(site)

        else:
            print(f'S{i} sends REPLY message to S{site}...')
            replies[site] += 1

        print()

def execute_cs(site):
    if executing[site]:
        print(f'S{site} is already executing CS..')
        print()
        return

    if replies[site] != n-1:
        print(f'S{site} received only {replies[site]} replies so cannot execute CS yet...')
        print()
        return

    global cs_available

    if not cs_available:
        print('CS is NOT available...')
        return

    print(f'S{site} received all {replies[site]} replies and can now execute CS !!')
    cs_available = False
    executing[site] = True
    print(f'S{site} is executing CS...')
    print()

def release_cs(site):
    if not executing[site]:
        print(f'Site S{site} cannot release CS because it is not executing CS yet..')
        print()
        return

    global cs_available

    cs_available = True
    executing[site] = False
    replies[site] = 0
    requesting[site] = [False, '-']

    for i in range(len(deferred[site])):
        print(f'S{site} is sending REPLY message to S{deferred[site][i]}..')
        replies[deferred[site][i]] += 1

    deferred[site] = []
    print()

while True:
    site = int(input(f'Select a site (from 0 to {n-1}) :'))
    print(f'What does S{site} want to do ? ')
    print('1. Request CS')
    print('2. Execute CS')
    print('3. Release CS')
    print('4. Quit')
    choice = int(input('Enter choice : '))
    print()

    if choice == 1:
        request_cs(site)
    elif choice == 2:
        execute_cs(site)
    elif choice == 3:
        release_cs(site)
    else:
        break
