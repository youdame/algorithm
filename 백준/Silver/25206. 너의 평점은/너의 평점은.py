import sys

from io import StringIO

grade_to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}



input = sys.stdin.readline
sum = 0
학점총수 = 0
for line in sys.stdin:
    과목명, 학점수, 학점 = line.strip().split(" ")
    if 학점 == "P":
        continue
    sum += float(학점수) * grade_to_score[학점]
    학점총수 += float(학점수)
print(f"{sum / 학점총수:.6f}")
