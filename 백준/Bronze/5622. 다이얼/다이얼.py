import sys

input = sys.stdin.readline

알파벳모음 = input().strip()


dial_dict = {
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"]
}

answer = 0
for 알파벳 in 알파벳모음:
  for key, value in dial_dict.items():
    if 알파벳 in value:
      answer += (int(key)) + 1
print(answer)