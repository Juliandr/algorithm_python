class DS(object):
    """docstring for DS"""
    def __init__(self):
        self.__id = [i for i in range(26)]

    def connect(self, parent, child):
        if parent != '-':
            self.__id[ord(parent) - ord('A')] = ord(child) - ord('A')

    def is_connected(self, parent, child):
        pid = ord(parent) - ord('A')
        cid = ord(child) - ord('A')

        connected = False
        generation_count = 0
        while not connected:
            generation_count += 1
            pid = self.__id[pid]
            if pid == cid:
                connected = True
            elif pid == self.__id[pid]:
                break
        if connected:
            result = 'child'
            if generation_count > 1:
                result = 'grandchild'
            if generation_count > 2:
                for _ in range(2, generation_count):
                    result = 'great-' + result
            return result
        else:
            return '-'

s = input()
n, m = s.split(' ')
n = int(n)
m = int(m)
ds = DS()
for _ in range(n):
    child, father, mother = input()
    ds.connect(father, child)
    ds.connect(mother, child)
for _ in range(m):
    a, b = input()
    if a == b:
        print('-')
    else:
        result = ds.is_connected(b, a)
        if result == '-':
            result = ds.is_connected(a, b)
            result = result.replace('child', 'parent')
        print(result)
