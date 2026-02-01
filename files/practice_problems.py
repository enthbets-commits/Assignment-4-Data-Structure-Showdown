"""
Practice Problems – Data Structure Selection and Justification
"""

# --------------------------------------------------
# Problem 1
# Scenario: Reverse a list of items.
# --------------------------------------------------
# Data Structure Used: List
# Justification:
# A list is ideal because it supports ordered data and easy traversal.
# Reversing a list runs in O(n) time, which is efficient for this task.

def reverse_list(items):
    return items[::-1]


# --------------------------------------------------
# Problem 2
# Scenario: Count how many times each value appears in a list.
# --------------------------------------------------
# Data Structure Used: Dictionary
# Justification:
# Dictionaries provide O(1) average-time lookups and updates.
# This makes them ideal for counting frequencies efficiently.

def count_items(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


# --------------------------------------------------
# Problem 3
# Scenario: Simulate a stack and remove the most recent item.
# --------------------------------------------------
# Data Structure Used: Stack (implemented using a list)
# Justification:
# Stacks follow a Last-In-First-Out (LIFO) structure.
# Push and pop operations run in O(1) time using a list.

def pop_stack(values):
    stack = []
    for value in values:
        stack.append(value)

    if stack:
        return stack.pop()
    return None
