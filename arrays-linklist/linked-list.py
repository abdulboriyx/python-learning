class Node:
      def __init__(self, data):
            self.data = data
            self.next = None

      def __repr__(self):
            return self.data
      
class Linkedlist:
      def __init__(self, nodes=None):
            self.head = None
            if nodes is not None:
                  node = Node(data=nodes.pop(0))
                  self.head = node
                  for elem in nodes:
                        node.next = Node(data=elem)
                        node = node.next

      # def __repr__(self):
      #       node = self.head
      #       nodes = []
      #       while node is not None:
      #             nodes.append(node.data)
      #             node = node.next
      #       nodes.append('None')
      #       return " -> ".join(nodes)
      def __iter__(self):
            node = self.head
            while node is not None:
                  yield node
                  node = node.next

allist = Linkedlist(['We', 'need', 'to', 'open', 'coffeeshop', 'no', 'matter', 'what'])
# print(allist)

for node in allist:
      print(node)

# first_node = Node('A')
# allist.head = first_node

# second_node = Node('Hello')
# first_node.next = second_node

# third_node = Node('Coffee')
# second_node.next = third_node






# iteration or aka traversing

