import sys

lines = sys.stdin.read().splitlines()

grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
         'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}
total_a = 0
total_b = 0
for line in lines:
    a = float(line.split()[1])  # 학점
    b = line.split()[2]  # 성적
    if b == 'P':
        continue
    else:
        b = grade.get(b)
        total_a += a
        total_b += a*b

print(total_b/total_a)
