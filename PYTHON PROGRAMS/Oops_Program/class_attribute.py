class Sampleclass:
    count = 0

    def increase(self):
        Sampleclass.count += 1

# Calling increase() on an object
sample1 = Sampleclass()
sample1.increase()
print(sample1.count)

sample2 = Sampleclass()
sample2.increase()
print(sample2.count)

