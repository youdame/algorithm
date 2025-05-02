
참가자수 = int(input())
티셔츠사이즈= list(map(int, input().split()))
티셔츠묶음, 펜묶음 = list(map(int, input().split()))

티셔츠묶음수 = 0
for i in 티셔츠사이즈:
  if i % 티셔츠묶음 != 0:
    티셔츠묶음수+= 1
  티셔츠묶음수 += i // 티셔츠묶음

print(티셔츠묶음수)
print(참가자수 // 펜묶음 ,참가자수 % 펜묶음)