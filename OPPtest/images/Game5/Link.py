class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    def __init__(self,node = None):
        self._head = node

    def is_empty(self):
        return self._head == None


    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        count = 1
        while cur != None:
            print(cur.elem,end=" ")
            count += 1
            cur = cur.next


    def add(self,item):
        node = Node(item)
        node.next = self._head
        self._head = node


    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def insert(self,pos,item):
        '''

        :param pos: 从0开始
        :param item:
        :return:
        '''

        node = Node(item)
        prior = self._head
        count = 0
        if pos<=0:
            self.add(item)
        elif pos > self.length() -1:
            self.append(item)
        else:
            while count < (pos-1):
                prior = prior.next
                count += 1

            node.next = prior.next
            prior.next = node


    def remove(self,item):
        ##删除节点
        cur = self._head
        pre = None

        while cur != None:
            if cur.elem == item:
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next


    def search(self,item):
        cur = self._head
        while cur != None:
            if cur.elem == item :
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.add(8)
    ll.insert(5,20)
    print(ll)
    ll.travel()




