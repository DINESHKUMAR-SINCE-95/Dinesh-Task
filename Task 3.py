Let's go through each of the tasks one by one.

### Task 1: Separating Even and Odd Numbers

Given the list `[10, 501, 22, 37, 100, 999, 87, 351]`, we need to separate the even and odd numbers into two different lists.

```python
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
```

### Task 2: Counting and Listing Prime Numbers

Given the same list, we need to count the prime numbers and create a new list containing only the prime numbers.

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = [num for num in numbers if is_prime(num)]
count_primes = len(prime_numbers)

print("Prime Numbers:", prime_numbers)
print("Count of Prime Numbers:", count_primes)
```

### Task 3: Counting Happy Numbers

Given the same list, we need to count how many numbers are happy numbers. A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number either equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.

```python
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(char) ** 2 for char in str(n))
    return n == 1

numbers = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = [num for num in numbers if is_happy_number(num)]
count_happy_numbers = len(happy_numbers)

print("Happy Numbers:", happy_numbers)
print("Count of Happy Numbers:", count_happy_numbers)
```

### Task 4: Sum of the First and Last Digit

Given an integer, find the sum of its first and last digit.

```python
def sum_first_last_digit(n):
    n_str = str(n)
    first_digit = int(n_str[0])
    last_digit = int(n_str[-1])
    return first_digit + last_digit

number = 12345  # Example number
print("Sum of first and last digit:", sum_first_last_digit(number))
```

### Task 5: Distributing Mangoes with Minimum Difference

Given a list of integers representing the number of mangoes in each bag, and the number of students, we need to distribute the mangoes so that the difference between the maximum and minimum number of mangoes given to the students is minimized.

```python
def distribute_mangoes(mangoes, m):
    mangoes.sort()
    min_diff = float('inf')
    for i in range(len(mangoes) - m + 1):
        diff = mangoes[i + m - 1] - mangoes[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

mangoes = [10, 501, 22, 37, 100, 999, 87, 351]
students = 3  # Example number of students
print("Minimum difference:", distribute_mangoes(mangoes, students))
```

These scripts should help you achieve each of the tasks.

### Task 6: Finding Duplicates in Three Lists

Given three lists, we need to find the duplicate elements that appear in all three lists.

```python
def find_duplicates(list1, list2, list3):
    # Find common elements in all three lists
    common_elements = set(list1).intersection(list2).intersection(list3)
    return list(common_elements)

# Example lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [5, 6, 7, 8, 9, 10]

duplicates = find_duplicates(list1, list2, list3)
print("Duplicates in all three lists:", duplicates)
```

### Task 7: Finding the First Non-Repeating Element in a List

Given a list of integers, we need to find the first non-repeating element.

```python
def find_first_non_repeating(lst):
    count_dict = {}
    
    # Count occurrences of each element
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the first non-repeating element
    for num in lst:
        if count_dict[num] == 1:
            return num
    return None

# Example list
numbers = [4, 5, 1, 2, 0, 4, 1, 5, 2]

first_non_repeating = find_first_non_repeating(numbers)
print("First non-repeating element:", first_non_repeating)
```

These scripts should help you accomplish each of the tasks.

### Task 8: Finding the Minimum Element in a Rotated and Sorted List

Given a rotated and sorted list, we need to find the minimum element. A rotated list is a list that has been shifted some number of times.

```python
def find_min_in_rotated_sorted_list(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# Example list
rotated_sorted_list = [4, 5, 6, 7, 0, 1, 2]

min_element = find_min_in_rotated_sorted_list(rotated_sorted_list)
print("Minimum element in rotated and sorted list:", min_element)
```

### Task 9: Finding a Triplet with a Given Sum

Given a list `[10, 20, 30, 9]` and a value `59`, we need to find a triplet in the list whose sum is equal to the given value.

```python
def find_triplet_with_sum(lst, target_sum):
    lst.sort()
    n = len(lst)
    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            if current_sum == target_sum:
                return (lst[i], lst[left], lst[right])
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return None

# Example list and target sum
lst = [10, 20, 30, 9]
target_sum = 59

triplet = find_triplet_with_sum(lst, target_sum)
print("Triplet with sum", target_sum, ":", triplet)
```

### Task 10: Finding a Sub-List with Sum Equal to Zero

Given a list `[4, 2, -3, 1, 6]`, we need to find if there is a sub-list with sum equal to zero.

```python
def has_sublist_with_zero_sum(lst):
    sum_set = set()
    current_sum = 0

    for num in lst:
        current_sum += num
        if current_sum == 0 or current_sum in sum_set:
            return True
        sum_set.add(current_sum)
    
    return False

# Example list
lst = [4, 2, -3, 1, 6]

has_zero_sum_sublist = has_sublist_with_zero_sum(lst)
print("Does the list have a sub-list with sum equal to zero?", has_zero_sum_sublist)
```

These scripts should help you accomplish each of the tasks.
