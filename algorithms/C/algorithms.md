### Arrays
- **Definition**: An array is a linear data structure that stores elements of the same type in contiguous memory locations.
- **Operations**: Common operations include traversal, insertion, deletion, searching, and sorting.
- **Advantages**: Fast access to elements using indices.
- **Disadvantages**: Fixed size, inefficient insertion/deletion operations.

### Bubble Sort
- **Concept**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Time Complexity**: $$O(n^2)$$ in the worst and average cases.
- **Space Complexity**: $$O(1)$$.
- **Stability**: Stable.

### Selection Sort
- **Concept**: Divides the array into a sorted and an unsorted region. Repeatedly selects the smallest (or largest) element from the unsorted region and moves it to the end of the sorted region.
- **Time Complexity**: $$O(n^2)$$.
- **Space Complexity**: $$O(1)$$.
- **Stability**: Not stable.

### Insertion Sort
- **Concept**: Builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms.
- **Time Complexity**: $$O(n^2)$$.
- **Space Complexity**: $$O(1)$$.
- **Stability**: Stable.

### Quick Sort
- **Concept**: Divides the array into two smaller sub-arrays (low and high elements), then recursively sorts the sub-arrays.
- **Time Complexity**: $$O(n \log n)$$ on average.
- **Space Complexity**: $$O(\log n)$$.
- **Stability**: Not stable.

### Counting Sort
- **Concept**: Counts the number of objects that have each distinct key value, then uses arithmetic to determine the positions of each key.
- **Time Complexity**: $$O(n + k)$$, where $$k$$ is the range of the input.
- **Space Complexity**: $$O(k)$$.
- **Stability**: Stable.

### Radix Sort
- **Concept**: Processes the digits of the numbers from least significant to most significant using a stable counting sort.
- **Time Complexity**: $$O(d(n + k))$$, where $$d$$ is the number of digits.
- **Space Complexity**: $$O(n + k)$$.
- **Stability**: Stable.

### Merge Sort
- **Concept**: Divides the array into two halves, recursively sorts them, and then merges the sorted halves.
- **Time Complexity**: $$O(n \log n)$$.
- **Space Complexity**: $$O(n)$$.
- **Stability**: Stable.

### Linear Search
- **Concept**: Sequentially checks each element of the list until a match is found or the whole list has been searched.
- **Time Complexity**: $$O(n)$$.
- **Space Complexity**: $$O(1)$$.

### Binary Search
- **Concept**: Finds the position of a target value within a sorted array by repeatedly dividing the search interval in half.
- **Time Complexity**: $$O(\log n)$$.
- **Space Complexity**: $$O(1)$$.
- **Precondition**: The array must be sorted.

### Bubble Sort
```pseudo
for i from 0 to n-1
    for j from 0 to n-i-1
        if arr[j] > arr[j+1]
            swap(arr[j], arr[j+1])
```

### Selection Sort
```pseudo
for i from 0 to n-1
    minIndex = i
    for j from i+1 to n
        if arr[j] < arr[minIndex]
            minIndex = j
    swap(arr[i], arr[minIndex])
```

### Insertion Sort
```pseudo
for i from 1 to n-1
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = key
```

### Quick Sort
```pseudo
function quickSort(arr, low, high)
    if low < high
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

function partition(arr, low, high)
    pivot = arr[high]
    i = low - 1
    for j from low to high - 1
        if arr[j] < pivot
            i = i + 1
            swap(arr[i], arr[j])
    swap(arr[i + 1], arr[high])
    return i + 1
```

### Counting Sort
```pseudo
function countingSort(arr, k)
    count = array of size k+1
    for i from 0 to n-1
        count[arr[i]] = count[arr[i]] + 1
    index = 0
    for i from 0 to k
        while count[i] > 0
            arr[index] = i
            index = index + 1
            count[i] = count[i] - 1
```

### Radix Sort
```pseudo
function radixSort(arr, d)
    for i from 1 to d
        countingSortByDigit(arr, i)

function countingSortByDigit(arr, digit)
    // Similar to counting sort but for digit place
```

### Merge Sort
```pseudo
function mergeSort(arr)
    if length of arr > 1
        mid = length of arr / 2
        left = arr[0..mid-1]
        right = arr[mid..end]
        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)

function merge(arr, left, right)
    i = j = k = 0
    while i < length of left and j < length of right
        if left[i] < right[j]
            arr[k] = left[i]
            i = i + 1
        else
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    while i < length of left
        arr[k] = left[i]
        i = i + 1
        k = k + 1
    while j < length of right
        arr[k] = right[j]
        j = j + 1
        k = k + 1
```

### Linear Search
```pseudo
function linearSearch(arr, x)
    for i from 0 to n-1
        if arr[i] == x
            return i
    return -1
```

### Binary Search
```pseudo
function binarySearch(arr, x)
    low = 0
    high = n - 1
    while low <= high
        mid = (low + high) / 2
        if arr[mid] == x
            return mid
        else if arr[mid] < x
            low = mid + 1
        else
            high = mid - 1
    return -1


Source: Conversation with Copilot, 10/9/2024
(1) DSA Bubble Sort - W3Schools. https://www.w3schools.com/dsa/dsa_algo_bubblesort.php.
(2) DSA Arrays - W3Schools. https://www.w3schools.com/dsa/dsa_data_arrays.php.
(3) DSA Binary Search - W3Schools. https://www.w3schools.com/dsa/dsa_algo_binarysearch.php.
(4) Learn Data Structures and Algorithms | DSA Tutorial. https://www.geeksforgeeks.org/learn-data-structures-and-algorithms-dsa-tutorial/.
(5) Bubble Sort Algorithm - GeeksforGeeks. https://www.geeksforgeeks.org/bubble-sort-algorithm/.
(6) 13. 4. Bubble Sort - Virginia Tech. https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/BubbleSort.html.
(7) Bubble Sort in Data Structures - ScholarHat. https://www.scholarhat.com/tutorial/datastructures/bubble-sort-in-data-structures.
(8) Insertion Sort Algorithm - GeeksforGeeks. https://www.geeksforgeeks.org/insertion-sort-algorithm/.
(9) DSA Insertion Sort - W3Schools. https://www.w3schools.com/dsa/dsa_algo_insertionsort.php.
(10) 13. 3. Insertion Sort - Virginia Tech. https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/InsertionSort.html.
(11) Insertion Sort - Data Structures and Algorithms (DSA) Guide. https://dsaguide.com/learn-insertion-sort-algorithm/.
(12) Array Data Structure Guide - GeeksforGeeks. https://www.geeksforgeeks.org/array-data-structure-guide/.
(13) WHAT IS ARRAY? | Array Data Structures | DSA Course. https://www.geeksforgeeks.org/videos/what-is-array-array-data-structures-dsa-course/.
(14) Arrays in Data Structures - Types, Representation & Algorithm - ScholarHat. https://www.scholarhat.com/tutorial/datastructures/arrays-in-data-structures.
(15) Arrays - Data Structures and Algorithms (DSA) Guide. https://dsaguide.com/arrays-data-structure-guide/.
(16) DSA Selection Sort - W3Schools. https://www.w3schools.com/dsa/dsa_algo_selectionsort.php.
(17) Selection Sort - GeeksforGeeks. https://www.geeksforgeeks.org/selection-sort-algorithm-2/.
(18) DSA Selection Sort Time Complexity - W3Schools. https://www.w3schools.com/dsa/dsa_timecomplexity_selsort.php.
