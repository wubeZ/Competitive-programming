subjects_marks = []
totalSum = 0
N,X = map(int,input().split())
for i in range(X):
    subjects_marks.append(list(map(float,input().split())))
marks_zipped = list(zip(*subjects_marks))
for i in range(len(marks_zipped)):
    totalSum = sum(marks_zipped[i])
    print(totalSum/X)