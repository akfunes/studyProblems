class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def append(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        
        self.tail.prev.next = node # set the old tail node to point to the new tail
        self.tail.prev = node # set pseudo tail to point to new tail
        
        return node
    
    def removeNode(self,node):
        tempNext = node.next
        tempPrev = node.prev
        
        tempPrev.next = tempNext
        tempNext.prev = tempPrev
            
        return node
    
    def pop(self):
        node = self.head.next
        self.removeNode(node)
        return node
    
class cacheObj:
    def __init__(self,value,key):
        self.val = value
        self.key = key
        
class LRUCache:

    def __init__(self, capacity: int):
        self.currSize = 0
        self.maxSize = capacity
        self.cacheMap = {} # store index of keys in list
        self.cacheList = DoublyLinkedList()
        

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            # retrieve the value
            itemNode = self.cacheMap[key]
            self.cacheList.removeNode(itemNode)
            
            # update internal data structures
            self.cacheList.append(itemNode)
            self.cacheMap[key] = itemNode
            
            return itemNode.data.val
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            node = self.cacheMap[key]
            node.data.val = value
            self.cacheList.removeNode(node)
            self.cacheList.append(node)

        else:
            if self.currSize >= self.maxSize:
                evictedItem = self.cacheList.pop().data
                self.currSize -= 1
                del self.cacheMap[evictedItem.key]
            
            
            node = self.cacheList.append(Node(cacheObj(value,key)))
            self.cacheMap[key] = node
            self.currSize += 1
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
