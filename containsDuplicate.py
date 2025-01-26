# list - [1,2,3,4,5] o/p - False
# list - [1,2,3,3,4] o/p - True

# Brute Force solution - run nested loop and check for each number 1 to len(list)

def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

nums = [1,2,3,4,5]  # Output: False
print(contains_duplicate(nums))

nums = [1,2,3,3,4]  # Output: True
print(contains_duplicate(nums))

# Time Complexity - O(n^2) - because of nested loop
# Space Complexity - O(1) - because we are not using any extra space

""" Optimized solution - use set to store the numbers and check if the number is already in the set or not.
If it is, then return True. If not, then add the number to the set and continue. 
If we finish the loop, then return False. This solution will have a time complexity of O(n) and a space complexity of O(n). """

def contains_duplicate_optimal(nums):
    seen = set()  # Create an empty set to store the numbers we have seen so far.
    for num in nums:  # Iterate over the list of numbers.
        if num in seen:  # If the number is already in the set, then we have found a duplicate.
            return True  # Return True.
        seen.add(num)  # Otherwise, add the number to the set.
    return False  # If we finish the loop, then we have not found any duplicates, so return False.


# Example usage:

nums1 = [1, 2, 3, 4, 5]  # Output: False
print(contains_duplicate_optimal(nums1))

nums2 = [1, 2, 3, 3, 4]  # Output: True
print(contains_duplicate_optimal(nums2))

#Time Complexity - O(n) - because we are iterating over the list only once.
#Space Complexity - O(n) - because we are using a set to store the numbers.

