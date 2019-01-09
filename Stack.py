class Stack(object):

    def __init__(self):
        self.__stack = []

    def push(self,item):
        """
        压栈
        :param item:
        :return:
        """
        self.__stack.append(item)

    def pop(self):
        """
        弹栈
        :return:
        """
        self.__stack.pop()

    def peek(self):
        """
        获取栈顶数据
        :return:
        """
        if self.__stack:
            return self.__stack[-1]
        else:
            return None


    def is_empty(self):
        """
        栈是否为空
        :return:
        """
        return self.__stack == []


    def size(self):
        """
        栈的大小
        :return:
        """
        return len(self.__stack)

if __name__ == '__main__':
    sta = Stack()
    sta.push(1)
    sta.push(2)
    sta.push(3)
    print(sta.is_empty())
    print(sta.peek())
    sta.pop()
    print(sta.peek())