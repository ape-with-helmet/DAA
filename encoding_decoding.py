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

def encoding(ele,freq,code):
    '''Encoding part.'''
    print("encoding begins...")
    for i in range (len(code)):
        for j in range (len(freq)):
            if code[i:j]==freq[j]:


def decoding():
    '''Decoding part.'''
    print("decoding begins...")

#n=int(input("Enter the no of characters: "))
ch=int(input("1.CodeFinder\n2.Encoder\n3.Decoder\nChoose: "))
if ch==1:
    nodes=[]
    chars=input('').split(" ")
    freq=[int(i) for i in input('').split(" ")]
    for x in range(len(chars)):
        heapq.heappush(nodes, Node(freq[x], chars[x]))
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = 0
        right.huff = 1
        SY=str(left.symbol+right.symbol)
        FR=left.freq+right.freq
        newNode = Node(FR, SY, left, right)
        heapq.heappush(nodes, newNode)
    print_nodes(nodes[0])
elif ch==2:
    elements=input('').split(" ")
    freq=[int(i) for i in input('').split(" ")]
    code=input('').split(" ")
    encoding(elements,freq,code)
elif ch==3:
    m
else:
    print("EXITING PROGRAM...")


