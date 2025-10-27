'''
Mini Drill: “Find Min” (the mirror of your last problem)

You need to write a function that returns the smallest number in a list of integers.

Rules (same logic, opposite goal):

If the list is empty → return float("inf")
(because every number is smaller than infinity)

Otherwise → find the minimum value manually, using a loop.

No min() function allowed.

Return the smallest number.
'''


def find_min(nums):
    if not nums:
        return float("inf")
    
    minimum_value = float("inf")

    for num in nums:
        if num < minimum_value:
            minimum_value = num

    return minimum_value

# UNIT TESTS

def test_find_min():
    cases = [
        ([1, 2, 3, -2], -2),
        ([], float("inf")),
        ([-5, -10, -3], -10),
        ([0], 0),
    ]
    for nums, expected in cases:
        result = find_min(nums)
        print(f"Input: {nums} | Expected: {expected} | Got: {result} | {'PASS' if result == expected else 'FAIL'}")

test_find_min()
