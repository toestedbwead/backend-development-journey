'''
Different Types of Exceptions
We haven't covered classes and objects yet, which is what an Exception really is at its core. We'll go more into that in the course on object-oriented programming.

For now, what is important to understand is that there are different types of exceptions, and we can handle them differently depending on the situation. Some exceptions are more specific, like ZeroDivisionError (which happens when you divide by zero) or IndexError (which happens when you try to access a list element at an invalid index—either too high or too low). Others are more general, like the base Exception.
'''

# SYNTAX

try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)

'''
0 division
index error
'''

'''
Why Specific Exceptions Come First
When handling exceptions, it’s important to catch the most specific ones first, because Python stops checking once it finds a matching exception handler. If you catch a more general Exception first, any specific errors will never get handled individually.

For example:
'''

try:
    nums = [0, 1]
    print(nums[2])
except Exception:
    print("An error occurred")
except IndexError:
    print("Index error")

'''
In this case, the general Exception will catch the error before the IndexError can be reached, and the message “Index error” will never be printed. Always handle the most specific exception first!
'''

'''
Alias Exception Messages
As seen in the example, you can also access the error using as, like this:
'''

#except Exception as e:
#    print(e)

'''
The default behavior of print is that it will print the string representation of whatever object is passed to it. In this case, it will print the error message.
'''