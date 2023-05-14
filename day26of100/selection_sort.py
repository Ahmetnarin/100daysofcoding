def selection_sort(arr):
    for i in range(len(arr)):
        # Find the miimum element in the unsorted part of the array
        min_index = i 

        for j in range(i + 1 , len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j 
            

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr



numbers = [6,2,3,8,12,5]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)
