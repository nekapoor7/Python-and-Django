def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

@call_counter
def mull(x, y=1):
    return x * y + 1

print(succ.calls)
for i in range(10):
    succ(i)
mull(3,4)
mull(4)
mull(y=3 , x=2)

print(succ.calls)
print(mull.calls)

