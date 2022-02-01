from collections import OrderedDict
class Node:
    def __init__(self,key):
        
        self.left=None
        self.right=None
        self.val=key 
    
    def inorder(self,root):
        
        if root:
            self.inorder(root.left)
            print(root.val,end=" ")
            self.inorder(root.right)
            
    def iterative_inorder(self,root):
        cur=root 
        s=[]
        while (True):
            if cur :
                s.append(cur)
                cur=cur.left
            elif (len(s)!=0):
                cur=s.pop()
                print(cur.val,end=" ")
                cur=cur.right
            else:
                print()
                break
    
    def preorder(self,root):
        if root:
            print(root.val,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def iterative_preorder(self,root):
        if root:
            s=[]
            s.append(root)
            while len(s)!=0:
                root=s.pop()
                print(root.val,end=" ")
                if (root.right):
                    s.append(root.right)
                if (root.left):
                    s.append(root.left)
            print()
    
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val,end=" ")
    
    def iterative_postorder(self,root):
        cur=root
        if root:
            s=[]
            s.append(root)
            k=[]
            while len(s)!=0:
                root=s.pop()
                k.append(root.val)
                if (root.left):
                    s.append(root.left)
                if (root.left):
                    s.append(root.right)
            print(*k[::-1])
            
    def vertical(self,root,hmap,v,l):
        
        if root==None:
            return None 
        if v not in hmap:
            hmap[v]=[]
        hmap[v].append((l,root.val))
        self.vertical(root.left,hmap,v-1,l+1)
        self.vertical(root.right,hmap,v+1,l+1)
        
        
            
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(10)
root.right.left = Node(9)
root.right.right = Node(11)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)

hmap = OrderedDict()
hmap = dict(sorted(hmap.items(),key = lambda item:item[0]))
root.vertical(root,hmap,0,0)
for v,l in hmap.items():
    print(*l)
        
# root.inorder(root) 
# print()
# root.iterative_inorder(root)
# root.preorder(root)
# print()
# root.iterative_preorder(root)
# root.postorder(root)
# print()
# root.iterative_postorder(root)
# print("-----")
# #root=None
# root = Node(27)
# root.left=Node(14)
# root.right=Node(35)
# root.left.left=Node(10)
# root.left.right=Node(19)
# root.right.left=Node(31)
# root.right.right=Node(42)
# root.inorder(root)
# print()
# root.iterative_inorder(root)
# root.preorder(root)
# print()
# root.iterative_preorder(root)
# root.postorder(root)
# print()
# root.iterative_postorder(root)

