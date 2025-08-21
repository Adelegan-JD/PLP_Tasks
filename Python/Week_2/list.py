# Create an empty list
my_list = []

# Append 10, 20, 30, 40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Change the figure in the second position to 15
my_list.insert(1, 15)

# Create another list
list1 = [50, 60, 70]

# Extend my_list with the new list
my_list.extend(list1)

# Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
print(my_list.index(30))
