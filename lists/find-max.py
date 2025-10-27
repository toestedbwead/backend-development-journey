'''
Assignment
Our players want a way to see their strongest attack from their last combat. Some enemies may be buffed to absorb either magic or melee attacks as health, which result in negative damage. Let's add another function to analyze data from our combat log.

Complete the find_max function. It takes as input a list of integers, nums, and returns an integer.

max_so_far is initialized as negative infinity.
Compare each number in nums to max_so_far. If any number is larger than max_so_far, replace max_so_far with that value.
Return max_so_far. If nums is empty, return negative infinity.
Here's an example of how your find_max function should work:

max_val = find_max([100, 10, 22])
print(max_val)
# 100
'''

def find_max(nums):

    if not nums:
        return float("-inf")

    max_so_far = float("-inf")
    
    for num in nums:
        if num > max_so_far:
            max_so_far = num

    return max_so_far

# UNIT TESTS
run_cases = [([1, 2, 3, 4, 5], 5), ([1, 2, 300, 4, 5], 300)]

submit_cases = run_cases + [
    ([1, 20, 3, 4, 5], 20),
    ([-1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 21, 18], 21),
    ([], float("-inf")),
    ([-1, -2, -3, -4, -5], -1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = find_max(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
