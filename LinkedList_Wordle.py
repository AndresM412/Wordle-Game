from termcolor import colored
class Node:                             
  def __init__(self, value):
    self.value = value
    self.next = None
    self.color = "white"
    self.pos = 0
    self.used = False
    

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def add_head2(self, value):
    node = Node(value)
    if(self.head == None):
      self.head = node
    else:
      node.next = self.head
      self.head = node
  
  def add_tail(self, value):
    node = Node(value)
    if(self.head == None):
      self.head = node
    else:
      current_node = self.head
      while(current_node.next is not None):
        current_node = current_node.next
      node.pos = current_node.pos + 1
      current_node.next = node
      
  def traverse(self):
    current_node = self.head
    while(current_node is not None):
      print(current_node.value)
      current_node = current_node.next

  def rec_traverse(self, current):
    current_node = current
    if(current_node is not None):
      print(current_node.value)
      self.rec_traverse(current_node.next)
  
  def get_size(self):
    current_node = self.head
    size = 0
    if(current_node is None):
      return size
    else:
      while(current_node is not None):
        current_node = current_node.next
        size += 1
    return size

  def delete_at_pos(self, pos):
    if(0 > pos >= self.get_size()):
      return "No es posible..."
    else:
      if(pos == 0):
        aux_node = self.head
        self.head = self.head.next
        aux_node.next = None
      else:
        current_node = self.head
        for i in range(0, pos-1):
          current_node = current_node.next
        aux_node = current_node.next
        current_node.next = current_node.next.next
        aux_node.next = None

  
  def add_at_pos(self,value, pos):
    node = Node(value)
    if(pos < 0 or pos > self.get_size()):
      return "No es posible agregar..."
    else:
      if(pos == 0):
        aux_node = self.head
        self.head = node
        pos.next = aux_node
        self.size += 1
      else:
        current_node = self.head
        for i in range(0, pos-1):
          current_node = current_node.next
        aux_node = current_node.next
        current_node.next = node
        node.next = aux_node
        self.size += 1

  def print_LinkedList(self):  #Imprime cada nodo en orden y sin espacios
    current_node = self.head
    while current_node != None:
      value = colored(current_node.value, current_node.color)
      if(current_node.next == None):
        print(value)
      else:
        print(value, end="")
      current_node = current_node.next
      
  def delete_all_nodes(self):
    while(self.head != None):
      node = self.head
      self.head = self.head.next
      node = None