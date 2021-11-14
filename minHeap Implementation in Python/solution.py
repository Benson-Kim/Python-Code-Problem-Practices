class MinBinaryHeap:
    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'
    
    __repr__=__str__
    
    def __len__(self):
        return len(self._heap)
    
    @property
    def getMin(self):
        return self._heap[0]
        pass
    
    def _parentIndex(self,index):
        return (index-1)//2
    
    def _parent(self,index):
        try:
            if index<=1:
                return None
            return self._heap[self._parentIndex(index-1)]
        except:
            return None
        pass
    
    def _leftChildIndex(self,index):
        return 2 * index + 1
    
    def _leftChild(self, index):
        try:
            return self._heap[self._leftChildIndex(index-1)]
        except:
            None
    
    def _rightChildIndex(self,index):
        return (2 * index) + 2
        pass

    def _rightChild(self, index):
        try:
            return self._heap[self._rightChildIndex(index-1)]
        except:
            None
            
    def insert(self,item):
    # YOUR CODE STARTS HERE
        size= len(self._heap) 
        self._heap.append(item)
        i = size
        while(i>0 and self._heap[self._parentIndex(i)] >= self._heap[i]):
            self._heap[self._parentIndex(i)],self._heap[i] = self._heap[i],self._heap[self._parentIndex(i)]
            i = self._parentIndex(i)
        pass
    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self)==0:
            return None        
        elif len(self)==1:
            deleted=self._heap[0]
            self._heap=[]
            return deleted
        else:
            # YOUR CODE STARTS HERE
            deleted = self._heap[0]
            size = len(self)-1
            self._heap[0] = self._heap[size]
            i = 0
            while True:
                minIndex = i
                l = self._leftChildIndex(i)
                if(l<=size and self._heap[l]<self._heap[minIndex]):
                    minIndex = l
                r = self._rightChildIndex(i)
                if(r<=size and self._heap[r]<self._heap[minIndex]):
                    minIndex = r
                if(i==minIndex):
                    break
                self._heap[i], self._heap[minIndex] = self._heap[minIndex], self._heap[i]
                i = minIndex
                self._heap.pop()
                
            return deleted
            pass