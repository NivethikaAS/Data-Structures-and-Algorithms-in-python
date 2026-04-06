def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Sort both halves
        merge_sort(left)
        merge_sort(right)

        lp = 0  # left pointer
        rp = 0  # right pointer
        fp = 0  # final pointer

        # Merge left and right into array
        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                array[fp] = left[lp]
                lp += 1
            else:
                array[fp] = right[rp]
                rp += 1
            fp += 1

        # Remaining elements in left
        while lp < len(left):
            array[fp] = left[lp]
            lp += 1
            fp += 1

        # Remaining elements in right
        while rp < len(right):
            array[fp] = right[rp]
            rp += 1
            fp += 1


# Example
array = [4, 2, 3, 1]
merge_sort(array)
print(array)