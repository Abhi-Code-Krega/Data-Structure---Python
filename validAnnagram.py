# return True if string s and string t are valid annagram else return False

from collections import Counter

# Brute Force Solution using list sorting method

def are_anagrams(s, t):
    # Check if the lengths of the strings are the same
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

# Example 1:

s = "listen"
t = "silent"

print(are_anagrams(s, t))  # Output: True

# Example 2:
s = "hello"
t = "world"
print(are_anagrams(s, t))  # Output: False

# T.C: O(n log n) due to sorting
# S.C: O(1) if we ignore the space used for sorting

# Using Counter from collections module

def are_anagrams_counter(s, t):
    # Check if the lengths of the strings are the same
    if len(s) != len(t):
        return False
    # Use Counter to count the frequency of each character in both strings and compare them
    return Counter(s) == Counter(t)

#E.g. 1:
s = "listen"
t = "silent"
print(are_anagrams_counter(s, t))  # Output: True

#E.g. 2:
s = "hello"
t = "world"
print(are_anagrams_counter(s, t))  # Output: False

# T.C: O(n) due to counting the frequency of each character in both strings
# S.C: O(1) if we ignore the space used for the Counter objects and assume the character set is fixed otherwise O(n)

# Brute Force Solution without using sorting method

def are_anagrams_brute_force(s, t):
    # Check if the lengths of the strings are the same
    if len(s) != len(t):
        return False
    t_list = list(t)  # Convert t to a list to remove characters easily
    for char in s:
        # Check if the character is in the list and remove it if it is present
        if char in t_list:
            t_list.remove(char)
        else:
            return False  # If the character is not present, the strings are not anagrams
    return True  # If all characters are matched and removed, the strings are anagrams

#E.g. 1:
s = "listen"
t = "silent"
print(are_anagrams_brute_force(s, t))  # Output: True

#E.g. 2:
s = "hello"
t = "world"
print(are_anagrams_brute_force(s, t))  # Output: False

# Optimal Solution without using Counter method

def are_anagrams_optimal(s, t):
    # Check if the lengths of the strings are the same
    if len(s) != len(t):
        return False
    # Create dictionaries to count the frequency of each character in both strings
    s_count = {}  # Dictionary to store the frequency of characters in s
    t_count = {}  # Dictionary to store the frequency of characters in t

    # Count the frequency of each character in s and t
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1  # Increment the count for the character in s_count
    
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1  # Increment the count for the character in t_count

    # Compare the dictionaries to check if they are equal
    return s_count == t_count

#E.g. 1:
s = "listen"
t = "silent"
print(are_anagrams_optimal(s, t))  # Output: True

#E.g. 2:
s = "hello"
t = "world"
print(are_anagrams_optimal(s, t))  # Output: False

# Optimal Solution using single dictionary

def are_anagrams_optimal_single_dict(s, t):
    # Check if the lengths of the strings are the same
    if len(s) != len(t):
        return False
    temp_dict = {}
    for char in s:
        temp_dict[char] = temp_dict.get(char, 0) + 1  # Increment the count for the character in temp_dict
    
    for char in t:
        temp_dict[char] = temp_dict.get(char, 0) - 1  # Decrement the count for the character in temp_dict

    return all(value == 0 for value in temp_dict.values())

#E.g. 1:
s = "listen"
t = "silent"
print(are_anagrams_optimal_single_dict(s, t))  # Output: True

#E.g. 2:

s = "hello"
t = "world"
print(are_anagrams_optimal_single_dict(s, t))  # Output: False


#showcase to Dhiman


