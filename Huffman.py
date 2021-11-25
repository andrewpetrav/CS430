
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq=freq #frequency
        self.symbol=symbol #symbol (character) of node
        self.left=left #left child
        self.right=right #right child
        self.huff='' #what it will be encoded to

    def printTree(self):
        lines, *_ = self.print() #*_ to pick up any extraneous args
        for line in lines:
            print(line)

    def print(self):
        pass

def getFreq(data):
    frequency=dict()
    for line in data:
        for char in line: #go thru each char in the data file
            if char in frequency: #if already in dict
                frequency[char]+=1 #increment
            else: #not already in dict
                frequency[char]=1 #initialize
    return frequency

def initNodes(freqTable): #create nodes
    nodes=[]
    for key in freqTable.keys(): 
        nodes.append(Node(freqTable[key], key))
    while len(nodes)>1: #sort in ascending order based on freq
        nodes=sorted(nodes, key=lambda x:x.freq)
        #get two smallest nodes
        r, l=nodes[0], nodes[1]
        r.huff, l.huff= 1, 0
        nNode=Node(l.freq+r.freq, l.symbol+r.symbol, l, r)
        nodes.remove(l)
        nodes.remove(r)
        nodes.append(nNode)
    return nodes[0]

def createCodes(n, h=''):
    huff=h+str(n.huff)
    if(n.left): #if has left child
        createCodes(n.left, huff)
    if(n.right): #if has right child
        createCodes(n.right, huff)
    if(not n.left and not n.right): #if has neither
        code[n.symbol]=huff
    return code

def printDict(codes): #display the encoding dictionary
    for code in codes:
        print(code+'-->'+codes[code])

def encodeData(data, encoding): #encode input data
    encoded_data=''
    for line in data:
        for char in line:
            encoded_data+=encoding[char]
    f=open('encodedOutput.txt', 'w')
    f.write(encoded_data)
    f.close()
 
def encode(data):
    freqTable=getFreq(data)
    node=initNodes(freqTable)
    encoding_dict=createCodes(node)
    printDict(encoding_dict)
    encodeData(data, encoding_dict)
    return node
    
def decode(tree):
    f=open('encodedOutput.txt', 'r')
    encoded_data=f.readlines() #read in encoded file
    f.close()
    head=tree
    decoded_data=''
    for line in encoded_data:
        for char in line:
            if char=='0':
                tree=tree.left
            elif char=='1':
                tree=tree.right
            try:
                if tree.left.symbol == None and tree.right.symbol == None:
                    pass
            except AttributeError:
                decoded_data+=tree.symbol
                tree = head
    f=open('decodedOutput.txt', 'w')
    f.write(decoded_data)
    f.close()


code=dict()
with open ('input.txt') as f:
    data=f.readlines()
huffman_tree=encode(data)
decode(huffman_tree)
huffman_tree.printTree()


