maxnum=int(input("최대값 입력 : "))
minnum=0
middle=(maxnum+minnum)//2
count=0
while True:
  count+=1
  middle=(minnum+maxnum)//2
  print("num ==", middle, "?")
  a=input('큼, 맞음, 또는 작음 :')
  if a=='큼':
    minnum=middle
  elif a=='작음':
    maxnum=middle
  else:
    print(count,"번 만에 맞췄다!")
    break