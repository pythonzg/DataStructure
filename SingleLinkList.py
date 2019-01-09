"""
实现单链表的相关操作
"""

class Node(object):
    """
    节点对象
    """
    def __init__(self,item):
        self.elem = item
        self.next = None


class SingleLinkList(object):
    """
    封装单链表的相关方法
    """

    def __init__(self,node=None):
        self.__head = node


    def is_empty(self):
        """
        判断单链表是否为空
        :return:
        """
        return self.__head == None

    def length(self):
        """
        单链表的长度
        :return:
        """
        cur = self.__head
        count = 0
        while cur is not None:
            count +=1
            cur = cur.next

        return count

    def travel(self):
        """
        遍历单链表
        :return:
        """
        cur = self.__head
        if cur is None:
            return None
        else:
            while cur is not None:
                print(cur.elem,end=' ')
                cur = cur.next
            print()

    def append(self,item):
        """
        尾插法
        :param item:
        :return:
        """
        node = Node(item)
        cur = self.__head
        if cur is None :
            self.__head = node
        else:
            while cur.next is not None:
                cur = cur.next

            cur.next = node


    def add(self,item):
        """
        头插法
        :param item:
        :return:
        """
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def insert(self,pos,item):
        """
        指定位置插入
        :param pos:
        :param item:
        :return:
        """
        node = Node(item)
        cur = self.__head
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            for i in range(pos-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search(self,item):
        """
        查询元素是否存在
        :param item:
        :return:
        """
        cur = self.__head
        if self.is_empty():
            return False
        else:
            while cur is not None:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
        return False

    def remove(self,item):
        """
        移除指定元素
        :param item:
        :return:
        """
        """
        cur = self.__head
        pre = None
        while cur is not None:
            if self.__head.elem == item:
                self.__head = self.__head.next
                break
            else:
                if cur.elem == item:
                    pre.next = cur.next
                    break
                else:
                    pre = cur
                    cur = cur.next
        """
        cur = self.__head
        if cur is not None:
            while cur is not None:
                if self.__head.elem == item :
                    self.__head = self.__head.next
                    break
                else:
                    if cur.next is not None:
                        if cur.next.elem == item:
                            cur.next = cur.next.next
                            break
                    cur = cur.next
            if cur is None:
                print("删除失败,单链表中没有{}这个元素!!".format(item))
        else:
            return False







if __name__ == '__main__':

    node = Node(1)
    sll1 = SingleLinkList()
    print(sll1.is_empty())
    print(sll1.length())
    # sll1.append(1)
    # sll1.add(99)
    # sll1.insert(3,1)
    print(sll1.search(1))
    sll1.travel()

    print('-----------------------')
    sll2 = SingleLinkList(node)
    print(sll2.is_empty())
    print(sll2.length())
    sll2.append(2)
    sll2.append(3)
    sll2.append(4)
    sll2.add(5)
    sll2.travel()
    sll2.insert(-2,11)
    sll2.insert(2,8)
    sll2.insert(7,34)
    sll2.travel()
    print(sll2.search(11))
    print(sll2.search(34))
    print(sll2.search(10))
    sll2.remove(5)
    sll2.travel()
    sll2.remove(11)
    sll2.travel()
    sll2.remove(1)
    sll2.travel()
    sll2.remove(34)
    sll2.travel()
    sll2.remove(1)
    sll2.travel()

