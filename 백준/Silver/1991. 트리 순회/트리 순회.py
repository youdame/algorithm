import sys
from io import StringIO


input = sys.stdin.readline

    
n = int(input())
record = {}

for _ in range(n):
    parent, left, right = input().split()
    record[parent] = (left, right)

pre = []
ino = []
post = []
def preorder(node):
    if node == ".":
        return
    left, right = record[node]
    pre.append(node)
    preorder(left)
    preorder(right)

def inorder(node):
    if node == ".":
        return
    left, right = record[node]
    inorder(left)    
    ino.append(node)
    inorder(right)

def postorder(node):
    if node == ".":
        return
    left, right = record[node]
    postorder(left)    
    postorder(right)
    post.append(node)
    

preorder("A")
inorder("A")
postorder("A")

print("".join(pre))
print("".join(ino))
print("".join(post))
    
    