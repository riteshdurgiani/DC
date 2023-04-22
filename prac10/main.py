import threading

lock = threading.Lock()
next_odd = threading.Event()
next_even = threading.Event()

def print_odd(n):
    for num in range(1, n+1, 2):
        with lock:
            print(f'Odd Thread ({threading.current_thread().name}) prints : {num}')
            next_even.set()
            next_odd.clear()
        if num != n:
            next_odd.wait()


def print_even(n):
    for num in range(2, n+1, 2):
        with lock:
            print(f'Even Thread ({threading.current_thread().name}) prints : {num}')
            next_odd.set()
            next_even.clear()
        if num != n:
            next_even.wait()

n = int(input('Enter upper limit : '))

odd_thread = threading.Thread(target=print_odd, args=(n,))
even_thread = threading.Thread(target=print_even, args=(n,))

odd_thread.start()
even_thread.start()

odd_thread.join()
even_thread.join()

print('Done Printing !!')
