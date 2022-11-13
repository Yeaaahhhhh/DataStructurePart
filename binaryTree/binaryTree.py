class BinaryTree:
    def __init__(self, rootElement):
        self.key = rootElement
        self.left = None
        self.right = None
        
    '''getters'''
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getKey(self):
        return self.key
    
    '''setters'''
    def setKey(self,key):
        self.key=key
        
    def setLeft(self,left):
        self.left=left        
  
    def setRight(self,right):
        self.right = right
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
  
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
            
    def _strHelper(self):
        """Returns list of strings,  total width of the tree, position of the middle node and the height"""
        # Base case, no child.
        if self.getLeft() == None and self.getRight() == None:
            row = '%s' % self.key
            width = len(row)
            middle = width // 2
            height = 1
            return [row], width, middle, height 

        keyStr = '%s' % self.key
        keyStrLength = len(keyStr)
        # Case 1: only have left child
        if self.getLeft() != None and self.getRight() == None:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength) * ' '
            shiftedRows = [row + keyStrLength * ' ' for row in leftRows]
            return [firstRow, secondRow] + shiftedRows, leftWidth + keyStrLength,leftWidth + keyStrLength // 2, leftHeight + 2

        # Case 2: only have right child
        elif self.getLeft() == None and self.getRight() != None:
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper()
            firstRow = keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = (keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            shiftedRows = [keyStrLength * ' ' + row for row in rightRows]
            return [firstRow, secondRow] + shiftedRows, rightWidth + keyStrLength,keyStrLength // 2, rightHeight + 2, 

        # Two children.
        else:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper() 
          
    
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            #append a few rows to fill in the blanks in the bottom, so that left and right lists are of the length
            if leftHeight < rightHeight:
                leftRows += [leftWidth * ' '] * (rightHeight - leftHeight)
            else:
                rightRows += [rightWidth * ' '] * (leftHeight - rightHeight)
            pairedRows = zip(leftRows, rightRows)
            rows = [firstRow, secondRow] + [i + keyStrLength * ' ' + j for i, j in pairedRows]
            return rows, leftWidth + rightWidth + keyStrLength,  leftWidth + keyStrLength // 2,max(leftHeight, rightHeight) + 2
    
    
    def __str__(self):
        rows, _, _, _ = self._strHelper()
        result = ''
        for row in rows:
            result += row + "\n"
        return result
    


################################################################################
##  EXERCISE 1
################################################################################    

def preorder(tree):
    '''
    print the value of a tree in a Preorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''  
    #TODO delete pass and write your code
    if tree is not None:
        print(tree.getKey(),end = ",")
        preorder(tree.getLeft())
        preorder(tree.getRight())
    else:
        return None
        
def inorder(tree):
    '''
    print the value of a tree in an Inorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''  
    #TODO delete pass and write your code
    if tree is not None:
        inorder(tree.getLeft())
        print(tree.getKey(),end = ",")
        inorder(tree.getRight())        
        
    else:
        return None


def postorder(tree):
    '''
    print the value of a tree in a postorder manner  
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None
    '''       
    #TODO delete pass and write your code
    if tree is not None:
        postorder(tree.getLeft())
        postorder(tree.getRight())
        print(tree.getKey(),end=",")
    else:
        return None
        
################################################################################
##  EXERCISE 2
################################################################################ 

def findMinKey(tree):
    '''
    find the minimum element in the tree
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None if tree is None, otherwise a number
    '''       
    #TODO delete pass and write your code
    if tree is not None:
        minKey = tree.getKey()
        if tree.left == None:
            pass
        else:
            minKey = min(minKey,findMinKey(tree.left))
        if tree.right is not None:
            minKey = min(minKey,findMinKey(tree.right))
        return minKey
    else:
        return None

def findMaxKey(tree):
    '''
    find the maximum element in the tree
    Parameters:
        - tree (a BinaryTree object)
 
    Returns: None if tree is None, otherwise a number
    '''       
    if tree is not None:
        maxKey = tree.getKey()
        if tree.left is not None:
            maxKey = max(maxKey,findMaxKey(tree.left))
        if tree.right is not None:
            maxKey = max(maxKey,findMaxKey(tree.right))
        return maxKey       
        
    else:
        return None

################################################################################
##  EXERCISE 3
################################################################################ 

def buildTree(inOrder, preOrder): 
    '''
    Build a binary tree based on given Inorder and PreOrder traversals
    
    Parameters:
        - inOrder,preOrder (list of numbers)
    
    Returns: a BinaryTree object
    '''  
    #TODO delete pass and write your code
    start = 0
    margin = 1
    end = len(inOrder)-1 
    if start > end:
        return None
    newNode = BinaryTree(preOrder[0])
    if start == end:
        return newNode
    pos = inOrder.index(newNode.getKey())
    lenOfIn = len(inOrder[:pos])
    newNode.right = buildTree(inOrder[pos+margin:],preOrder[pos+margin:])
    newNode.left = buildTree(inOrder[:pos],preOrder[margin:lenOfIn+2])
    return newNode

################################################################################
##  Test your functions: you are encouraged to add other tests as well
################################################################################ 
def main():
    tree = BinaryTree(1)
    tree.insertLeft(2)
    tree.insertRight(7)
    tree.getLeft().insertLeft(3)
    tree.getLeft().insertRight(6)
    tree.getLeft().getLeft().insertLeft(4)
    tree.getLeft().getLeft().insertRight(5)
    tree.getRight().insertLeft(8)
    tree.getRight().insertRight(9)
    print("the tree:\n")
    print(tree)
    
    print("preorder traversal:")
    preorder(tree)
    print()
    print("inorder traversal:")
    inorder(tree)
    print()
    print("postorder traversal:")
    postorder(tree)
    print()

    print('Max value in tree:', findMaxKey(tree))
    print('Min value in tree:', findMinKey(tree))

    inor = [4,3,5,2,6,1,8,7,9]
    preor = [1,2,3,4,5,6,7,8,9]

    theTree = buildTree(inor,preor)
    
    print(theTree)
    
    inor2 = [3,2,4,1,5]
    preor2 = [1,2,3,4,5]

    theTree2 = buildTree(inor2,preor2)
    
    print(theTree2)  
    
    
if __name__ == "__main__":
    main()