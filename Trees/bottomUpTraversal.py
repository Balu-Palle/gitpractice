from collections import deque
def bottomUpTraversal(root):
    if not root:
        return []
    res=[]
    q=deque([root])
    while q:
        l=[]
        for i in range(len(q)):
            ele=q.popleft()
            l.append(ele.val)
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
            
        res.append(l)
    return res[::-1] #this is for bootom up traversal of binary tree
    return res #this is for top down traversal of binary tree


