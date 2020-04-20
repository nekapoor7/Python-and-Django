#The following example uses a decorator to count the number of times a function has been called.
# To be precise, we can use this decorator solely for functions with exactly one parameter:

def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

print(succ.calls)
for i in range(10):
    succ(i)

print(succ.calls)

