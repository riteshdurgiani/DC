class Node:
    def __init__(self, id, parent = None):
        self.id = id
        self.holder = parent
        self.request_q = []

    def __repr__(self):
        return f"Node {self.id}"

def print_request_queue():
    print('Request Queue :-')
    for i, node in enumerate(nodes):
        print(f'Node {i} : {node.request_q}')
    print()

def print_holder():
    print('Holder Variables :-')
    for i,node in enumerate(nodes):
        print(f'Node {i} -> Node {node.holder.id}')

def release_cs(current_node):
    print(f'**** Node {current_node.id} is releasing CS ****')

    if len(current_node.request_q) != 0 :
        requesting_node_id = current_node.request_q[0]
        current_node.request_q.pop(0)
        print(f'Node {current_node.id} sends TOKEN to Node {requesting_node_id}')
        current_node.holder = nodes[requesting_node_id]
        print_request_queue()
        send_token(current_node.holder)

        if len(current_node.request_q) != 0 :
            print(f'Node {current_node.id} sends REQUEST message to Node {current_node.holder.id}')
            request_cs(current_node.holder, current_node)

    else:
        print(f'Node {current_node.id} has released CS and currently holds the TOKEN...')
        print_holder()
        print_request_queue()

def send_token(current_node):
    requesting_node_id = current_node.request_q[0]
    current_node.request_q.pop(0)

    if requesting_node_id == current_node.id:
        print(f'**** Node {current_node.id} is executing CS ****')
        current_node.holder = current_node
        print_request_queue()
        release_cs(current_node)
        return

    print(f'**** Node {current_node.id} sends TOKEN to Node {requesting_node_id} ****')
    current_node.holder = nodes[requesting_node_id]
    print_request_queue()
    send_token(current_node.holder)

def request_cs(current_node, requesting_node):
    if current_node.id != root_id:
        current_node.request_q.append(requesting_node.id)
        print_request_queue()
        print(f'**** Node {current_node.id} sends REQUEST message to Node {current_node.holder.id} ****')
        request_cs(current_node.holder, current_node)

    else:
        if current_node == requesting_node:
            print(f'**** Node {current_node.id} already has the token and so it can execute CS ****')
            return
        current_node.request_q.append(requesting_node.id)
        print_request_queue()
        current_node.request_q.pop()
        print(f'**** Node {current_node.id} sends TOKEN to Node {requesting_node.id} ****')
        current_node.holder = requesting_node
        print_request_queue()
        send_token(current_node.holder)


n = int(input('Enter number of processes : '))
nodes = []
root_id = 0
node_0 = Node(0)
node_0.holder = node_0
nodes.append(node_0)

for i in range(1, n):
    parent_id = int(input(f'Enter parent id for node {i} : '))
    node = Node(i, nodes[parent_id])
    nodes.append(node)

request_id = int(input('Enter id of node requesting CS : '))
print()
print(f'**** Node {request_id} wants to enter CS ****')
print_holder()
request_cs(nodes[request_id], nodes[request_id])
