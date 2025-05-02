def 펠린드롬(문자):
  for i in range(len(입력값) // 2 + 1):
      # print(i,len(입력값)-i-1 )
      # print(입력값[i],입력값[len(입력값)-i-1] )
      if 입력값[i] != 입력값[len(입력값)-i-1]:
        return "no"
  return "yes"
  
while True:

  입력값 = input()
  # print(입력값)
  if 입력값 == "0":
    break
  
  print(펠린드롬(입력값))

