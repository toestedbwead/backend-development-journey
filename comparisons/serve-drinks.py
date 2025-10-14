'''
Assignment
In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!

Complete the function that determines if a bartender should serve drinks to a customer. Only return True if all of these conditions apply. If any of these conditions are False, return False:

The customer's age is 21 or older
The bartender is working
The time is between 5 and 10 o'clock (inclusive)
'''

# much readable code

def should_serve_customer(customer_age, on_break, time):
    if customer_age < 21:
        return False
    if on_break:
        return False
    if time < 5 or time > 10:
        return False
    return True

'''def should_serve_customer(customer_age, on_break, time):
    if (customer_age >= 21) and (on_break == False) and (time <= 10 and time >= 5):
        return True
    return False'''

# UNIT TESTS:

run_cases = [
    (22, False, 10, True),
    (41, False, 1, False),
    (14, False, 7, False),
]

submit_cases = run_cases + [
    (21, False, 5, True),
    (107, False, 9, True),
    (23, True, 5, False),
    (21, False, 4, False),
    (57, False, 11, False),
    (20, False, 5, False),
]


def test(input1, input2, input3, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * customer_age: {input1}")
    print(f" * on_break: {input2}")
    print(f" * time: {input3}")
    result = should_serve_customer(input1, input2, input3)
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
