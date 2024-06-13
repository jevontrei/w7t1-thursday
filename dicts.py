# Creating a dictionary
my_dict = {
    # key: value,
    # key: value,
    "name": "Alice",
    "age": 25,
    "city": "Sydney"
}

# Access the values with keys, just index them same as lists (and tuples?!), but keys instead of indices
print(my_dict["city"])
print(my_dict["age"])

# Add new key-value pair
my_dict["email"] = "alice@example.com"
print(my_dict)

# Overwriting
# my_dict["city"] = "Melbourne"
# check what happens with duplicates:
my_dict["city"] = "Alice"
print(my_dict)

# Remove a key-value pair
del my_dict["age"]
print("-----------")
print(my_dict)

# Alternatively, you can use .pop()
print("*********")
my_dict.pop("email")
print(my_dict)

# Checking for key existence
print("email" in my_dict)
print("name" in my_dict)

# Mostofa Q: Question. In a large dictionary. If we know only the stored value, how would I retrieve associated key value? Assume printing the entire dictionary would be too large.
# https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/

list_of_keys = list(my_dict.keys())
list_of_values = list(my_dict.values())

print(list_of_values.index("Alice"))
print(list_of_values[0])

# Iterate through dictionary
for key, value in my_dict.items():
    print(f"{key}, {value}")

# Nested dictionaries
nest = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

print(nest["person2"]["name"])

# Merging dicts
merged = my_dict | nest
print(merged)
