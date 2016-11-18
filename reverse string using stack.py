to reverse the string using stack

a = 'shrijan'
b = []
for each in a:
	b.append(each)

class Stack:
	def __init__(self,items):
		self.items = []
	def push(self,item):
		self.items.append(item)
	def pop(self):
		self.items.pop()
	def size(self):
		return len(self.items)
a = 'shrijan'
b = []
for each in a:
	b.append(each)

obj = Stack([])

for each in b:
	obj.push(each)
size = obj.size()
reversed = ''
for i in range(0,size):
	reversed += obj.items.pop()
print(reversed)