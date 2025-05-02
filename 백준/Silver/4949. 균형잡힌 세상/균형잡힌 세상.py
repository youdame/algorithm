
while True:
  inputStr = input()

  if inputStr == ".":
    break
  
  answer = "yes"
  stack = []
  for i in inputStr:  
    if i == "(" or i =="[":
      stack.append(i)
    elif i ==")":
      if len(stack) == 0:
        answer = "no"
        break
      팝 = stack.pop()
      if 팝 != "(":
        answer = "no"
        break
    elif i =="]":
      if len(stack) == 0:
        answer = "no"
        break
      팝 = stack.pop()
      if 팝 != "[" :
        answer = "no"
        break
  if len(stack) != 0:
    answer = "no"

  print(answer)  
     

