#
# checkpassword.py - check for most common 1000 passwords
# 
#
import sys
from trie import Node, Trie 

usage = \
"""
checkpasswordtrie.py - Check if password is 1000 most common

Usage:
    python checkpasswordtrie.py
    checkpassword: [enter password to check]
    press [enter] with no password to quit
Returns:
    "[word] is not a common password" or
    "[word is a common password"
"""

def ReadPasswords():
    pwFile = "1000-most-common-passwords.txt" 
    with open(pwFile, "r") as f:      
        passwords = f.read().splitlines()
    return passwords

print("Building common password trie...")
trie = Trie()
passwords = ReadPasswords()
for password in passwords:
    trie.insert(password)

testword = 'dummy'
while testword != '':
    testword = input('checkpassword: ')
    if trie.find(testword) is None:
        print(testword, ' is not a common password')
    else:
        print(testword, ' is a common password')





        

    
    