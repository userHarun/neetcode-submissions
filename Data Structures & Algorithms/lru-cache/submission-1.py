# doubly linked list Node
class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val
class LRUCache:

    def __init__(self, capacity: int):
        # dummy nodes and link them

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # init cache
        self.cap = capacity
        self.cache = {}

    # helper func for insert 
    def insert(self, node):
        # head->NodeA->tail
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        node.prev = prev
        #update dummy node tail prev
        self.tail.prev = node


    def remove(self, node):
        # head->prv->node->nxt->tail
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

        

        

    def get(self, key: int) -> int:
        # return the val and update mru or otherwise return -1

        if key in self.cache:
            # update mru by just removing and adding it
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        cache = self.cache
        # check if key in cache and remove it and add it and update value
        if key in cache:
            self.remove(cache[key])
        cache[key] = Node(key, value)
        self.insert(cache[key])
        if len(cache) > self.cap:
            # remove lru
            lru = self.head.next
            self.remove(lru)
            del cache[lru.key]
            
            
        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''

the data structure that makes sense is a doubly linked list

So the key is the actual cache key, and the value is a pointer/reference to the node in linkedList

we can use  2 dummy node and the dummy node will lead us to lru and mru
so when we do put we are changing 5 ptrs in total since its a doubly lnked list

we also could use helper funcs for inserting and removign a node


'''