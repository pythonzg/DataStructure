"""
单向循环链表的实现
"""

class Node(object):

    def __init__(self,item):
        self.elem = item
        self.next = None


class CricleLinkList(object):

    def __init__(self,node=None):
        self.__head = node

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return self.__head == None

    def length(self):
        """
        获取链表的长度
        :return:
        """
        cur = self.__head
        count = 1
        if self.is_empty():
            return 0
        else:
            while cur.next is not self.__head:
                cur = cur.next
                count += 1

            return count

    def travel(self):
        """
        遍历循环链表
        :return:
        """
        cur = self.__head
        if self.is_empty():
            print(cur)
        else:
            while cur.next is not self.__head:
                print(cur.elem,end=' ')
                cur = cur.next
            print(cur.elem)

    def append(self,item):
        """
        尾插法
        :param item:
        :return:
        """
        cur = self.__head
        node = Node(item)
        if self.is_empty():
            node.next = node
            self.__head = node
        else:
            while cur.next is not self.__head:
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def add(self,item):
        """
        头插法
        :param item:
        :return:
        """
        cur = self.__head
        node = Node(item)

        if self.is_empty():
            node.next = node
            self.__head = node
        else:
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head


    def insert(self,pos,item):
        """
        指定位置插入
        :param pos:
        :param item:
        :return:
        """
        node = Node(item)
        pre = self.__head
        if pos <= 0 :
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            for i in range(pos-1):
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def search(self,item):
        """
        查找元素是否存在
        :param item:
        :return:
        """
        cur = self.__head
        if self.is_empty():
            return False
        else:
            if cur.elem == item:
                return True
            else:
                while cur.next is not self.__head:
                    cur = cur.next
                    if cur.elem == item:
                        return True
                return False


    def remove(self,item):
        """
        删除指定元素
        :param item:
        :return:
        """
        cur = self.__head
        pre = None
        if self.is_empty():
            return False
        else:
            if cur.elem == item:
                while cur.next is not self.__head:
                    cur = cur.next
                self.__head = self.__head.next
                cur.next = self.__head
                return
            else:
                while cur.next is not self.__head:
                    pre = cur
                    cur = cur.next
                    if cur.elem == item:
                        pre.next = cur.next
                        return

                if cur.elem == item:
                    pre.next = cur.next
                    return



if __name__ == '__main__':

    # node = Node(1)
    cll = CricleLinkList()
    print(cll.is_empty())
    print(cll.length())
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.add(4)
    cll.insert(2,5)
    cll.insert(-1,6)
    cll.insert(6,7)
    cll.travel()
    print(cll.search(5))
    print(cll.search(1))
    print(cll.search(7))
    print(cll.search(8))
    print(cll.length())
    cll.remove(6)
    cll.travel()
    cll.remove(7)
    cll.travel()
    cll.remove(5)
    cll.travel()
    cll.remove(4)
    cll.travel()
    print(cll.is_empty())
