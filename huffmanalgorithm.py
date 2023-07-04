'''Imports heap.'''
import heapq


class Node:
    '''Starts node.'''

    def __init__(self, f_y, symbol, l_t=None, r_t=None):
        # frequency of symbol
        self.freq = f_y
        # symbol name(character)
        self.symbol = symbol
        # node left of current node
        self.left = l_t
        # node right of current node
        self.right = r_t
        # tree direction(0/1)
        self.huff = ' '

    def __lt__(self, nxt):
        return self.freq < nxt.freq
# utility function.


def print_nodes(node, val=''):
    '''Printz.'''
    newval = val + str(node.huff)
    if node.left:
        print_nodes(node.left, newval)
    if node.right:
        print_nodes(node.right, newval)
    if not node.left and not node.right:
        print(f"{node.symbol}->{newval}")

n=int(input("Enter the no of characters: "))
chars = [n]
freq = [n]
nodes = []
for x in range(n):
    C=str(input("Enter the character: "))
    chars.append(C)
for x in range(n):
    f=int(input("Enter the frequencies: "))
    freq.append(f)
for x in range(n):
    heapq.heappush(nodes, Node(freq[x], chars[x]))
    print("###")
while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    print("#")
    left.huff = 0
    right.huff = 1
    print("##")
    SY=(left.symbol+right.symbol)
    print(left.symbol)
    print(right.symbol)
    print("SY: ",SY)
    FR=left.freq+right.freq
    print(left.freq)
    print(right.freq)
    print("FR:",FR)
    newNode = Node(FR, SY, left, right)
    print("##$#")
    heapq.heappush(nodes, newNode)
print_nodes(nodes[0])
