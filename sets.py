# Creating a set
my_set = {1, 2, 3, 4}

print(my_set)

# Adding an element
my_set.add(5)
print(my_set)

# Remove an element
my_set.remove(2)
print(my_set)

# Membership testing
print(2 in my_set)
print(3 in my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("----------")
# Union
union_value = set_a.union(set_b) 
union_value = set_b.union(set_a) 
print(union_value)

# Intersection
intersection_value = set_a.intersection(set_b)
intersection_value = set_b.intersection(set_a)
print(intersection_value)

# Difference
difference_value_a = set_a.difference(set_b)
difference_value_b = set_b.difference(set_a)
print(difference_value_a)
print(difference_value_b)