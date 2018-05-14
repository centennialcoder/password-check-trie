
class Node():
    def __init__(self):
        #children is a dictionary of the next char as key
        #   value of dictionary is the node object
        self.children = {}
        #isLeaf is True if this prefix is a valid complete word
        self.isLeaf = False
        #value contains full string if this is a leaf node
        self.value = ''

class Trie():
    # string is stored in nodes, there are no edge objects
    # this is simple trie with single char per node
    # this uses a dictionary for children which simplifies the logic
    # but makes this trie less useful for sorting
    # https://en.wikipedia.orgwiki/Trie    
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        node = self.root
        index_last_char = None
        # try to find child nodes for each character in the string
        for index_char, char in enumerate(string):
            if char in node.children:
                #found a pre-existing child node
                node = node.children[char]
            else:
                #need to create a new node
                index_last_char = index_char
                break    
        
        if index_last_char is not None:
            #append new nodes for remaining unique chars
            for char in string[index_last_char:]:
                node.children[char] = Node()
                node = node.children[char]
            node.value = string
            node.isLeaf = True
            #print('Created new node ', node.value)

        else:
            #word is already in trie
            #print('Found node ',node.value, 'isLeaf was ',node.isLeaf)
            node.isLeaf = True
            node.value = string

    def find(self, string):
        node = self.root
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                #print('Node not found')
                return None
        #check that is a leaf
        #print('found node ',node.value,' isLeaf=', node.isLeaf)
        if node.isLeaf:
            return node.value
        else:
            return None

    def delete(self, string):
        # not implemented for this project
        print('delete not implemented')
