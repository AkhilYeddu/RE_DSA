class node:
    def __init__(self,data):
        self.data = data
        self.next = None
# n1 = node(25)
# n2 = node(30)
# n1.next = n2
# print(n2)
# print(n1.next)
n1 = node(10)
n2 = n1

n2.next = node(30)
n2 = n2.next
print(n2.data)