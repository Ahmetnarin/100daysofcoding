my_list = [1, 2, 3, 2, 4, 1, 5, 6, 5]

# Count occurrences of elements in the list
element_counts = {}
for element in my_list:
    element_counts[element] = my_list.count(element)

# Print the element counts
for element, count in element_counts.items():
    print(f"{element}: {count} occurrences")
