from binarytree import build, bst, Node

input_list = [7, 3, 9, 2, 5, 8, 10]
root = build(input_list)

print('Initial tree:')
print(root)

while True:
  print('Choose an option:')
  print('1. Add a new element.')
  print('2. Delete an element.')
  print('3. Exit.')
  choice = int(input('Option: '))
  
  if choice == 1:
    value = int(input('Enter a value to add: '))
    new_node = Node(value)
    root = bst.insert(root, new_node)
    print('New tree:')
    print(root)
    
  elif choice == 2:
    value = int(input('Enter a value to delete: '))
    root = bst.delete(root, value)
    print('New tree:')
    print(root)
    
  elif choice == 3:
    break
    
  else:
    print('Invalid choice.')