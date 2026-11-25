import threading


def count_numbers():
    for i in range(1, 6):
        print(f"Count: {i}")


def calculate_squares():
    for i in range(1, 6):
        print(f"Square of {i}: {i ** 2}")


def calculate_cubes():
    for i in range(1, 6):
        print(f"Cube of {i}: {i ** 3}")


t1 = threading.Thread(target=count_numbers)
t2 = threading.Thread(target=calculate_squares)
t3 = threading.Thread(target=calculate_cubes)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()