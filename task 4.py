# Define the hash function
def hash_key(v, m):
    return v % m

# Define the list of values
value_list = [3, 2, 9, 11, 7]
size = len(value_list)

# Construct the hash table using the hash function
hash_table = {}
for value in value_list:
    key = hash_key(value, size)
    if key in hash_table:
        hash_table[key].append(value)
    else:
        hash_table[key] = [value]

# Ask user for operation choice
while True:
    choice = input("Choose an operation (1: Construct hash table, 2: Add element, 3: Update value, 4: Delete element, 5: Search element, 6: Print table): ")
    if choice == '1':
        print("Hash table constructed: ", hash_table)
    elif choice == '2':
        new_value = int(input("Enter new element to add: "))
        new_key = hash_key(new_value, size)
        if new_key in hash_table:
            hash_table[new_key].append(new_value)
        else:
            hash_table[new_key] = [new_value]
        print(f"Added {new_value} to hash table with key {new_key}")
    elif choice == '3':
        update_key = int(input("Enter key to update value for: "))
        if update_key in hash_table:
            update_index = hash_table[update_key].index(int(input("Enter current value to update: ")))
            new_value = int(input("Enter new value: "))
            hash_table[update_key][update_index] = new_value
            print("Updated value in hash table")
        else:
            print("Key not found in hash table")
    elif choice == '4':
        delete_key = int(input("Enter key to delete element from:

        if delete_key in hash_table:
            delete_value = int(input("Enter value to delete: "))
            if delete_value in hash_table[delete_key]:
                hash_table[delete_key].remove(delete_value)
                print(f"Deleted {delete_value} from key {delete_key}")
            else:
                print("Value not found in key")
        else:
            print("Key not found in hash table")
    elif choice == '5':
        search_value = int(input("Enter value to search for: "))
        search_key = hash_key(search_value, size)
        if search_key in hash_table:
            if search_value in hash_table[search_key]:
                print(f"{search_value} found at key {search_key}")
            else:
                print(f"{search_value} not found in key")
        else:
            print(f"{search_value} not found in hash table")
    elif choice == '6':
        print("Hash table contents: ")
        for key, values in hash_table.items():
            print(f"Key {key}: {values}")
    else:
        print("Invalid input")