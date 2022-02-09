"""
請寫3段程式碼(語言不拘)回覆下列3個問題，並將程式碼上傳到github後分享鏈接給我們。
"""


"""
建立函式 fibonacci 代入參數 position，position 表示的是想要得到 fibonacci sequence 中的第幾個數字的值。

 fibonacci(0) // 0
 fibonacci(1) // 1
 fibonacci(2) // 1
 fibonacci(3) // 2
 fibonacci(4) // 3
"""

FIB_LOOKUP = dict()


def fibonaccci(position):
    """
    fibonacci(0) // 0
    fibonacci(1) // 1
    fibonacci(2) // 1
    fibonacci(3) // 2
    fibonacci(4) // 3
    fibonacci[n] = fibonacci[n-1] + fibonacci[n-2], while n >= 2
    """
    if position == 0:
        return 0
    elif position in {1, 2}:
        return 1
    elif FIB_LOOKUP.get(position):
        return FIB_LOOKUP[position]
    else:
        FIB_LOOKUP[position] = fibonaccci(position-1) + fibonaccci(position-2)
        return FIB_LOOKUP[position]


"""
使用 Linked List 實作 Stack ，實作需包含以下方法。
push() : 添加新元素。 pop():移除元素並返回被移除的元素。 size():返回所有元素數量。

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop() // 3
stack.size() // 2

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.cur = None
        self.length = 0

    def push(self, data):
        node = Node(data)
        self.length += 1

        if self.head is None:
            self.head = node
            self.cur = node
        else:
            self.cur.next = node
            self.cur = self.cur.next

    def pop(self):
        if self.length <= 0:
            raise IndexError("Stack is empty")

        prev_node = cur_node = self.head
        self.length -= 1

        while cur_node.next is not None:
            prev_node = cur_node
            cur_node = cur_node.next

        if self.length == 0:
            self.head = self.cur = None
        else:
            self.cur = prev_node
        prev_node.next = None
        return cur_node.data

    def size(self):
        return self.length


""" TEST
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()  # 3
stack.size()  # 2
"""


"""
將下列輸入資料整合成期望的輸出結果。
輸入資料:
const userIds = ['U01', 'U02', 'U03']
const orderIds = ['T01', 'T02', 'T03, 'T04']
const userOrders = [
    { userId: 'U01', orderIds: ['T01', 'T02'] },
    { userId: 'U02', orderIds: [] },
    { userId: 'U03', orderIds: ['T03'] },
]
const userData = { 'U01': 'Tom', 'U02': 'Sam', 'U03': 'John' }
const orderData = {
    'T01': { name: 'A', price: 499 },
    'T02': { name: 'B', price: 599 },
    'T03': { name: 'C', price: 699 },
    'T04': { name: 'D', price: 799 }
}
輸出結果:
const result = [{
    user: { id: 'U01', name: 'Tom' },
    orders: [
        { id: 'T01', name: 'A', price: 499 },
        { id: 'T02', name: 'B', price: 599 },
    ],
},
…,
]

"""


userIds = ['U01', 'U02', 'U03']
orderIds = ['T01', 'T02', 'T03', 'T04']
userOrders = [
    {'userId': 'U01', 'orderIds': ['T01', 'T02']},
    {'userId': 'U02', 'orderIds': []},
    {'userId': 'U03', 'orderIds': ['T03']}
]
userData = {'U01': 'Tom', 'U02': 'Sam', 'U03': 'John'}
orderData = {
    'T01': {'name': 'A', 'price': 499},
    'T02': {'name': 'B', 'price': 599},
    'T03': {'name': 'C', 'price': 699},
    'T04': {'name': 'D', 'price': 799}
}
result = [
    {
        'user': {'id': 'U01', 'name': 'Tom'},
        'orders': [
            {'id': 'T01', 'name': 'A', 'price': 499},
            {'id': 'T02', 'name': 'B', 'price': 599}
        ]
    }
]

result = []
userOrdersLookup = {}

for userOrder in userOrders:
    userOrdersLookup[userOrder['userId']] = userOrder['orderIds']

for userCode in userData:
    data = {
        'user': {'id': userCode, 'name': userData[userCode]},
        'orders': []
    }
    orderIds = userOrdersLookup[userCode]

    for orderId in orderIds:
        orderData[orderId].update({'id': orderId})
        data['orders'].append(orderData[orderId])

    result.append(data)
