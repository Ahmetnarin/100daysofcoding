from collections import Counter

my_list = [1, 2, 3, 2, 4, 1, 5, 6, 5]
value_counts = Counter(my_list)

for value, count in value_counts.items():
    print(f"{value}: {count} occurrences")