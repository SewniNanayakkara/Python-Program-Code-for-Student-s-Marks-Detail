def validation_function(mark):
   #print(mark)
  if not mark.isdigit():
    print("Integer requried")
    return False
    
  range1 = range(0,121,20)    
  if int(mark) not in range1:
    print("Out of range")
    return False

  return True
    
progressCount = 0
trailerCount = 0
retrieverCount = 0
excludeCount = 0
dic = {}

while True:
  while True:
    st_id=input("Enter st_id:")
    st_id=st_id.lower()
    if not(st_id[0]=='w' and len(st_id)==8 and st_id[1:].isnumeric()):
      print('Invalid input')
    elif st_id in dic:
      print("Id already exist")
    else:
      break

  while True:
    passMark = input("Enter the number of credits at passMark: ")
    if not validation_function(passMark):
      continue
    else:
      break

  while True:
    deferMark = input("Enter the number of credits at deferMark: ")
    if not validation_function(deferMark):
      continue
    else:
      break
      
  while True:
    failMark = input("Enter the number of credits at failmark: ")
    if not validation_function(failMark):
      continue
    else:
      break
  
  passMark=int(passMark)
  deferMark=int(deferMark)
  failMark=int(failMark)
  totalMark = passMark + deferMark + failMark
    # print(type(totalMark))
    # totalMark=str(totalMark)
    # print(type(totalMark))
    # print(type(120))
  if totalMark == 120:
    # print("ok")
    # print(passMark)
    if passMark == 120:
      print("Progress")
      progressCount = progressCount + 1
      dic[st_id] = 'progress - ' + str(passMark) + ',' + str(deferMark) + ',' + str(failMark)
    elif passMark == 100:
      print("Progress(module trailer)")
      trailerCount = trailerCount + 1
      dic[st_id] = 'Progress(module trailer) - ' + str(passMark) + ',' + str(deferMark) + ',' + str(failMark)
    elif failMark >= 80:
      print("Exclude")
      excludeCount = excludeCount + 1
      dic[st_id] = 'Exclude - ' + str(passMark) + ',' + str(deferMark) + ',' + str(failMark)
    else:
      print("Do not progress – module retriever")
      retrieverCount = retrieverCount + 1
      dic[st_id] = 'Do not progress – module retriever - ' + str(passMark) + ',' + str(deferMark) + ',' + str(failMark) 
  else:
    print("Total incorrect")
    continue
 
  print("would you like to enter another set of data?")
  while True:
    loopBreak = False
    userInput = input("Enter 'y' for yes or 'q' to quit and view results: ")
    if userInput == 'y':
      break
    elif userInput == 'q':
        for i,j in dic.items():
          print(i,':',j,end=' ')
        loopBreak = True
        break
    else:
      print("Enter a vaild input")
      continue
  if loopBreak :
    break