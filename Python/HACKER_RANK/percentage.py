N = int(input())
results = {}
for i in range(N):
    a = input().split(' ')
    results[a[0]] = [float(x) for x in a[1:]]
student = input()
print("%.2f" %(sum(results[student])/len(results[student])))



if __name__ == '__main__':
     n = int(input())
     student_marks = {}
     for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        query_name = input()