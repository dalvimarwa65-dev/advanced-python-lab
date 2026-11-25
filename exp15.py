import gc
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None


def create_cycles():
    for i in range(10000):
        a = Node(i)
        b = Node(i + 1)
        a.ref = b
        b.ref = a


gc.disable()
create_cycles()

before_objects = len(gc.get_objects())
before_ref_count = sys.getrefcount(gc.get_objects())
collected = gc.collect()
after_objects = len(gc.get_objects())

print(f"Objects before gc.collect(): {before_objects}")
print(f"Unreachable objects collected: {collected}")
print(f"Objects after gc.collect(): {after_objects}")
print(f"Tracked object count difference: {before_objects - after_objects}")