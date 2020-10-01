class Node:
    left, right, value = None, None, ''
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data
    def isLeaf(self):
        if(self.left is None and self.right is None):
            return True
        else:
            return False
            
class PrefixCodeTree:
    root = None

    def __init__(self):
        self.root = Node('')

    def insert(self, codeword, symbol):
        node = self.root
        for str in codeword:
            if(str == 0):
                if (node.left is None):
                    node.left = Node('')
                    node = node.left
                else:
                    node = node.left
            else:
                if (node.right is None):
                    node.right = Node('')
                    node = node.right
                else:
                    node = node.right   
        node.value = symbol   

    def decode(self, encodedData, dataLen):
        data = ''
        message = ''
        node = self.root
        for byte in encodedData:
            data += f'{byte:0>8b}'
        for i in range(dataLen):
            if (data[i] == '0'):
                node = node.left
            else:
                node = node.right
            if (node.isLeaf()):
                message += node.value
                node = self.root
        return message

# test.py
codebook = {
    'x1': [0],
    'x2': [1,0,0],
    'x3': [1,0,1],
    'x4': [1,1]
}
'''
codeTree = PrefixCodeTree() # create a prefix code tree `codeTree`

# Initialize codeTree with codebook
for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

message = codeTree.decode(b'\xd2\x9f\x20', 21)
print(message)
'''