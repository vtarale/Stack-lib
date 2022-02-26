import stack_lib.stack as s

# test
new_s = s.Stack()
print(f"Is the stack empty {new_s.isempty()}")
new_s.add(1)
new_s.add(2)
new_s.add(3)
new_s.add(4)
print(f"Is the stack empty {new_s.isempty()}")
new_s.display()
item = new_s.get()
print(f"Item recived: {item}")
new_s.display()