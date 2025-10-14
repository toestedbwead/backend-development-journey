'''
Assignment
We need a way for our game to track whether a character's attack hits or misses.

Complete the does_attack_hit function. The function should return True if either of the following conditions are met:

The attack_roll is not a 1 and the attack roll is greater than or equal to the armor_class, or
The attack roll is a 20
Otherwise, it should return False.
'''
def does_attack_hit(attack_roll, armor_class):
    if (attack_roll != 1) and (attack_roll >= armor_class) or (attack_roll == 20):
        return True
    return False


#UNIT TESTS

run_cases = [
    (17, 18, False),
    (20, 25, True),
    (2, 2, True),
]

submit_cases = run_cases + [
    (1, 0, False),
    (16, 13, True),
    (5, 5, True),
    (1, 1, False),
    (20, 20, True),
    (15, 10, True),
    (2, 3, False),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = does_attack_hit(input1, input2)
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
