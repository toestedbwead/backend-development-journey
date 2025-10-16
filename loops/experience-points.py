'''
Experience Points
Adventurers need experience points (XP) to level up and become stronger. We want to show the total XP a player has gained given their current level.

Each character starts with 0 XP at level 1. To reach the next level, they need to accumulate additional XP equal to their current level times 5.

For example:

At level 1, XP is 0.
To reach level 2, we need 5 XP (1 * 5) added to the current XP so far (0).
At level 2, XP is 5.
To reach level 3: we need 10 XP (2 * 5) added to the current XP so far (5).
At level 3, XP is 15.
To reach level 4: we need 15 XP (3 * 5) added to the current XP so far (15).
And so on...
To summarize the calculation in a table:

Level	XP so far	XP for next level
1	0	5
2	5	10
3	15	15
4	30	20
Assignment
Complete the calculate_experience_points function.

It accepts a level (integer) and returns the total XP a player has gained so far.
'''

def calculate_experience_points(level):
    exp = 0
    for i in range(1, level):
        exp += i * 5
    return exp

run_cases = [
    (2, 5),
    (3, 15),
    (4, 30),
]

submit_cases = run_cases + [
    (1, 0),
    (5, 50),
    (7, 105),
    (10, 225),
    (15, 525),
    (20, 950),
]


def test(input1, expected_output):
    print("---------------------------------")
    result = calculate_experience_points(input1)
    print(f"Input:     {input1}")
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
