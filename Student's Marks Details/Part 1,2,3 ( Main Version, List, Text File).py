# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953793
# Date: 26/10/2022

redo = "yes"
while redo == "yes":
  selection = input("Enter whether you are a student or staff:- ")

  if selection == "student":
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
    List = []

    while True:
      while True:
        passMark = input("Please enter your credits at pass:- ")
        if not validation_function(passMark):
          continue
        else:
          break

      while True:
        deferMark = input("Please enter your credits at defer:- ")
        if not validation_function(deferMark):
          continue
        else:
          break
          
      while True:
        failMark = input("Please enter your credits at fail:- ")
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
          print("-------------------------------End-------------------------------")
          redo= "no"
          break
          
        elif passMark == 100:
          print("Progress(module trailer)")
          print("-------------------------------End-------------------------------")
          redo= "no"
          break
          
        elif failMark >= 80:
          print("Exclude")
          print("-------------------------------End-------------------------------")
          redo= "no"
          break        
        else:
          print("Do not progress – module retriever")
          print("-------------------------------End-------------------------------")
          redo= "no"
          break
         
      else:
        print("Total incorrect")
        continue

  elif selection == "staff":

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
    List = []

    while True:
      while True:
        passMark = input("Enter your total PASS credits:- ")
        if not validation_function(passMark):
          continue
        else:
          break

      while True:
        deferMark = input("Enter your total DEFER credits:- ")
        if not validation_function(deferMark):
          continue
        else:
          break
          
      while True:
        failMark = input("Enter your total FAIL credits:- ")
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
          List.append('progress - ' + str(passMark) + ',' + str(deferMark) + ',' + str(failMark))
        elif passMark == 100:
          print("Progress(module trailer)")
          trailerCount = trailerCount + 1
          List.append('Trailer - ' + str(passMark) + ',' + str(deferMark) + ',' + str(failMark))
        elif failMark >= 80:
          print("Exclude")
          excludeCount = excludeCount + 1
          List.append('Exclude - ' + str(passMark) + ',' + str(deferMark) + ',' + str(failMark))
        else:
          print("Do not progress – module retriever")
          retrieverCount = retrieverCount + 1
          List.append('Retriever - ' + str(passMark) + ',' + str(deferMark) + ',' + str(failMark))
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

          print('\n' + "-" * 65)
          print("Histogram")
          print("Progress", progressCount,":", progressCount*"*")
          print("Trailer", trailerCount, ":", trailerCount*"*")
          print("Retriever", retrieverCount, ":", retrieverCount*"*")
          print("Exclude", excludeCount, ":", excludeCount*"*")
          print(progressCount + trailerCount + retrieverCount + excludeCount, "outcomes in total.")
          print("-"*  65 + '\n')
          
          print("Part 2:\n")
          print('\n'.join(List))
          loopBreak = True

          print("\npart 3:\n" )
          f = open('test.txt', 'w+')
          m ='\n'.join(List)
          f.write(m)
          f.seek(0)
          print(f.read())
          f.close()
          print("\n-------------------------------End-------------------------------")
          redo="no"
          break
        else:
          print("Enter a vaild input")
          continue
      if loopBreak :
        break

  else:
    print("Invalid Input")
