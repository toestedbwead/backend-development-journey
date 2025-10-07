'''
Debugging
When you're working as a professional developer, you'll typically write code on your computer and test it by yourself before it's deployed to users.

That first part of the process is called debugging. You write some code, run it, and if it doesn't work, you fix the bugs. You repeat this process until you're confident that your code works as expected.
'''


'''
## ASSIGNMENT
Complete the take_magic_damage function. It should return the new health after calculating how much magic-type damage the player takes. Here is a description of the arguments:

health: The player's starting health
resist: The player's magic resistance. This reduces the damage they take by a static amount
amp: The attacker's magic amplification. This increases the damage they deal by a multiplier
spell_power: The base damage of the spell

First, calculate the total maximum damage to be inflicted by multiplying the spell_power by the amp. Then, subtract the resist from the total damage to get the actual damage dealt. Apply that damage to the player's health and return the new health.
'''

def take_magic_damage(health, resist, amp, spell_power):
    total_max_dmg = spell_power * amp
    total_dmg = total_max_dmg - resist
    new_health = health - total_dmg
    return new_health

# UNIT TESTS

run_cases = [
    (100, 5, 2, 20, 65),
    (200, 10, 1, 25, 185),
]

submit_cases = run_cases + [
    (0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1),
    (100, 2, 3, 1, 99),
    (2500, 3, 2, 2, 2499),
]


def test(input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}, {input2}, {input3}, {input4}")
    result = take_magic_damage(input1, input2, input3, input4)
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
