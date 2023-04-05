class TreeEmptyError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info=value
        self.lchild=None
        self.rchild=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def is_empty(self):
        return self.root==None

    def insert(self,x):
        self.root==self._insert(self.root,x)

    def _insert(self,p,x):
        if p is None:
            p=Node(x)
        elif  x<p.info:
            p.lchild=self._insert(p.lchild,x)
        elif x>p.info:
            p.rchild=self._insert(p.rchild,x)
        else:
            print(x," already present in the tree")
        return 
    
    def insert1(self,x):
        p=self.root
        par=None
        while p is not None:
            par=p
            if x<p.info:
                p=p.lchild
            elif x>p.info:
                p=p.rchild
            else:
                print(x + " already present in the tree")
                return
        temp=Node(x)

        if par==None:
            self.root=temp
        elif x<par.info:
            par.lchild=temp
        else:
            par.rchild=temp

    def search(self,x):
        return self._search(self.root,x) is not None

    def _search(self,p,x):
        if p is None:
            return None
        if x<p.info:
            return self._search(p.lchild,x)
        if x>p.info:
            return self._search(p.rchild,x)

    def search1(self,x):
        p=self.root
        while p is not None:
            if x<p.info:
                p=p.lchild
            elif x>p.info:
                p=p.rchild
            else:
                return True
        return False

    def delete(self,x):
        self.root=self._delete(self.root,x)

    def _delete(self,p,x):
        if p is None:
            print(x," not found")
            return p
        if x<p.info:
            p.lchild=self._delete(p.lchild,x)
        elif x>p.info:
            p.rchild=self._delete(p.rchild,x)
        else:
            if p.lchild is not None and p.rchild is not None:
                s=p.rchild
                while s.lchild is not None:
                    s=s.lchild
                p.info=s.info
                p.rchild=self._delete(p.rchild,s.info)

            else:
                if p.lchild is not None:
                    ch=p.lchild
                else:
                    ch=p.rchild
                p=ch
        return p
    
    def delete1(self,x):
        p=self.root
        par=None

        while p is not None:
            if x==p.info:
                break
            par=p
            if x<p.info:
                p=p.lchild
            else:
                p=p.rchild
            
            if p==None:
                print(x, " not found")

            if p.lchild is not None and p.rchild is not None:
                ps=p
                s=p.rchild

                while s.lchild is not None:
                    ps=s
                    s=s.lchild
                p.info=s.info
                p=s
                par=ps

            if p.lchild is not None:
                ch=p.lchild
            else:
                ch=p.rchild
            
            if par==None:
                self.root=ch
            elif p==par.lchild:
                par.lchild=ch
            else:
                par.rchild=ch

    def min1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is Empty")
        p=self.root
        while p.lchild is not None:
            p=p.lchild
        return p.info
    
    def max1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is Empty")
        p=self.root
        while p.rchild is not None:
            p=p.rchild
        return p.info

    def min2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is Empty")
        return self._min(self.root).info

    def _min(self,p):
        if p.lchild is None:
            return p
        return self._min(p.lchild)
    
    def max2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is Empty")
        return self._max(self.root).info

    def _max(self,p):
        if p.rchild is None:
            return p
        return self._max(p.rchild)
    
    
    def display(self):
        self._display(self.root,0)
        print()

    def _display(self,p,level):
        if p is None:
            return
        self._display(p.rchild,level+1)
        print()

        for i in range(level):
            print("\t",end=' ')
        print(p.info)
        self._display(p.lchild,level+1)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self,p):
        if p is None:
            return
        print(p.info," ",end=' ')
        self._preorder(p.lchild)
        self._preorder(p.rchild)
    
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self,p):
        if p is None:
            return

        self._inorder(p.lchild)
        print(p.info," ",end=' ')
        self._inorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self,p):
        if p is None:
            return

        self._preorder(p.lchild)
        self._preorder(p.rchild)
        print(p.info," ",end=' ')

    def height(self):
        return self._height(self.root)

    def _height(self,p):
        if p is None:
            return 0
        hl=self._height(p.lchild)
        hr=self._height(p.rchild)

        if hl>hr:
            return hl+1
        else:
            return hr+1


bst=BinarySearchTree()

while True:
    print("1. Display Tree")
    print("2. Search(iterative)")
    print("3. Search(recurssive)")
    print("4. Insert a new node (Iterative)")
    print("5. Insert a new node (recursive)")
    print("6. Deleta node(Iterative)")
    print("7. Deleta node(recursive)")
    print("8. Find minimum key(Iterative)")
    print("9. Find minimum key(recursive)")
    print("10. Find maximum key(iterative)")
    print("11. Find maximum key(recursive)")
    print("12. Preorder Traversal")
    print("13. Inorder Traversal")
    print("14. Postorder Traversal")
    print("15. Height of the tree")
    print("16. Quit")

    choice=int(input("Enter your choice : "))

    if choice==1:
        bst.display()

    elif choice==2:
        x=int(input("Enter the key to be searched : "))
        if bst.search1(x):
            print("Key Found")
        else:
            print("Key Not Found")

    elif choice==3:
        x=int(input("Enter the key to be searched : "))
        if bst.search(x):
            print("Key Found")
        else:
            print("Key Not Found")

    elif choice==4:
        x=int(input("Enter the key to be inserted : "))
        bst.insert1(x)

    elif choice==5:
        x=int(input("Enter the key to be inserted : "))
        bst.insert(x)

    elif choice==6:
        x=int(input("Enter the key to be deleted : "))
        bst.delete1(x)

    elif choice==7:
        x=int(input("Enter the key to be deleted : "))
        bst.delete(x)

    elif choice==8:
        print("Minimum key is ",bst.min1())

    elif choice==9:
        print("Minimum key is ",bst.min2())

    elif choice==10:
        print("Maximum key is ",bst.max1())

    elif choice==11:
        print("Maximum key is ",bst.max2())

    elif choice==12:
        bst.preorder()

    elif choice==13:
        bst.inorder()
    
    elif choice==14:
        bst.postorder()

    elif choice==15:
        print("Height of tree is ",bst.height())

    elif choice==16:
        break

    else:
        print("Wrong Choice")

    print()
