from trie import Node, Trie 

testTrie = Trie()

#test cannot find string in empty Trie
fail = testTrie.find('anything')
print('expect None for empty match =', fail)

#test add da, dad
testTrie.insert('da')
testTrie.insert('dad')

print('expect None for d: ', testTrie.find('d'))
print('expect da for da: ', testTrie.find('da'))
print('expect dad for dad: ', testTrie.find('dad'))
print('expect None for sad: ', testTrie.find('sad'))

#test adding inner letter as valid word (single d)
testTrie.insert('d')
print('expect d for d: ', testTrie.find('d'))
