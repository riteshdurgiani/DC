import datetime

n = int(input('Enter the number of nodes in n/w : '))
current_time = []

for i in range(n):
    time = input(f"Enter time in hh:mm format of node {i} in n/w : ")
    time = datetime.datetime.strptime(time, "%H:%M")  # convert string time to datetime object
    current_time.append((i, time))

agreed_time = input("Enter agreed upon time for resync in hh:mm format : ")
agreed_time = datetime.datetime.strptime(agreed_time, "%H:%M")
current_time = sorted(current_time, key=lambda node_time: node_time[1],
                      reverse=True)  # sort nodes in descending order of time

def print_time(current_time):
    for i in range(len(current_time)):
        print(f'Node {current_time[i][0]} = {current_time[i][1].time()}')

def print_skews(current_skews):
    for i in range(len(current_skews)):
        print(f'Node {current_skews[i][0]} = {current_skews[i][1]} seconds')

def adjust_time(current_time, skews):
    print('Skews :-')
    for node, skew in skews.items():
        print(f'Node {node} : {skew}')

    avg_skews = {node: sum(skew)/len(skew) for node, skew in skews.items()}
    print()
    print('Average Skews Computed :-')
    for node, avg in avg_skews.items():
        print(f'Node {node} : {avg} ', end='')
        status = 'ahead' if avg >= 0 else 'behind'
        print(f'(Node {node} is {abs(avg)} seconds {status})')
        print()

    print('Final Adjusted Time : ')
    current_time = [(node_time[0], node_time[1] - datetime.timedelta(seconds=avg_skews[node_time[0]]))
                       for node_time in current_time]
    print_time(current_time)

def DGA(current_time):
    skews = dict()
    for j in range(len(current_time)):
        skews[j] = []

    for i in range(len(current_time)):
        current_sender = current_time[i][0]
        time_to_resync = agreed_time - current_time[i][1]
        current_time = [(node_time[0], time_to_resync + node_time[1]) for node_time in current_time]
        print()

        print(f'--- After {time_to_resync} ---')
        current_skews = [(node_time[0], int((node_time[1] - agreed_time).total_seconds()))
                         for node_time in current_time]

        print('Current Time :-')
        print_time(current_time)

        print('Current Skews :-')
        print_skews(current_skews)

        print('Current Sender who broadcast resync : ', 'Node', current_sender)
        for node, skew in current_skews:
            skews[node].append(skew)

    print()
    adjust_time(current_time, skews)

print()
print('--- Initial Time ---')
print_time(current_time)
print(f'Agreed upon time for resync = {agreed_time.time()}')
DGA(current_time)
