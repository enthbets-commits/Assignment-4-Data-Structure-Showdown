"""
Timed Challenge Question:
Given a list of integers, return the first duplicate value.
If no duplicate exists, return None.
"""

def first_duplicate(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return num
        seen.add(num)

    return None


# -----------------------------
# Test Cases
# -----------------------------
print(first_duplicate([1, 2, 3, 4, 2]))   # Expected output: 2
print(first_duplicate([5, 1, 5, 2, 3]))   # Expected output: 5
print(first_duplicate([1, 2, 3]))         # Expected output: None
print(first_duplicate([]))                # Expected output: None


"""
Reflection on Timed Challenge

For the timed challenge, I chose to use a set as my primary data structure.
Sets provide constant-time average performance for lookup operations, which
made them ideal for quickly checking whether a value had already been seen.
This allowed me to identify duplicates efficiently while keeping the code
simple and readable.

The 30-minute time limit strongly influenced my decision to choose a familiar
and straightforward data structure. Rather than experimenting with multiple
approaches, I focused on writing a correct and efficient solution as quickly
as possible. Using a set helped reduce complexity and minimized the risk of
logical errors under pressure.

Under the time constraint, I made trade-offs by prioritizing clarity over
advanced optimizations. I limited error handling to basic edge cases such as
empty lists, since handling every possible invalid input could have consumed
valuable time. Overall, this challenge helped me understand how time pressure
affects decision-making and reinforced the importance of choosing practical,
interview-appropriate solutions.
"""
