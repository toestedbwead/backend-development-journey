'''
Assignment
We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:

A list of the same messages but with all instances of the word dang removed.
A list containing the number of dang words that were removed from each message at that particular index.
Here are some examples:

messages = ["dang it bobby!", "look at it go"]
filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]

messages2 = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
filter_messages(messages2) # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]

Here are the steps for you to follow:

Create the 2 empty lists that you'll return at the end:
One for the filtered messages with "dang" removed.
And one for the counts of dangs removed from those messages.

For each message in the list of messages:
Split the message into a list of words using the .split() string method.
Create an empty list for all the good words in this message.
Create another empty list for all the dangs in this message.
For each word in the message:
If the word is "dang", add it to the list of dangs
If it is not "dang", add it to the list of good words
Join the list of good words into a single string using the .join() method.
Append the new filtered message to the list of filtered messages.
Append the length of the list of dangs to the list of counts of dangs.
Return the filtered messages first, then the counts of dangs
'''

def filter_messages(messages):
    filter_list = []
    filter_counts = []   

    for message in messages:
        # split the message into a list of words using the .split() string method
        good_list = []
        dang_list = []

        split_msg = message.split()

        for word in split_msg:
            if word == "dang":
                dang_list.append(word)
            else:
                good_list.append(word)
    
        good_words = " ".join(good_list) # joins list of good words
        filter_list.append(good_words) # append the filtered msg to the filter list

        dang_count = len(dang_list)  # take number of dangs
        filter_counts.append(dang_count) # insert the number of dangs into the list
    
    return filter_list, filter_counts

    


# UNIT TESTS

run_cases = [
    (
        ["darn it", "this dang thing won't work", "lets fight one on one"],
        ["darn it", "this thing won't work", "lets fight one on one"],
        [0, 1, 0],
    ),
]

submit_cases = run_cases + [
    (
        [
            "well dang it",
            "dang the whole dang thing",
            "kill that knight, dang it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the dang baddies",
        ],
        [
            "well it",
            "the whole thing",
            "kill that knight, it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the baddies",
        ],
        [1, 2, 1, 0, 0, 0, 1],
    ),
]


def test(input, expected_output1, expected_output2):
    print("---------------------------------")
    print(f"Input:")
    print(f" * messages: {input}")
    print("Expected:")
    print(f" * filtered messages: {expected_output1}")
    print(f" * words removed: {expected_output2}")
    print("Actual:")
    try:
        result = filter_messages(input)
        print(f" * filtered messages: {result[0]}")
        print(f" * words removed: {result[1]}")
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False

    if result == (expected_output1, expected_output2):
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
