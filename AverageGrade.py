from ast import Break, Pass
from turtle import done
import sys

while True:
    try:
        print("please enter your 5 marks below")
        try:
            mark1 = int(input("enter mark 1: "))
            assert 0 <= mark1 <= 100
        except ValueError:
            pass
        try:
            mark2 = int(input("enter mark 2: "))
            assert 0 <= mark2 <= 100
        except ValueError:
            pass
        try:
            mark3 = int(input("enter mark 3: "))
            assert 0 <= mark3 <= 100
        except ValueError:
            pass
        try:
            mark4 = int(input("enter mark 4: "))
            assert 0 <= mark4 <= 100
        except ValueError:
            pass
        try:
            mark5 = int(input("enter mark 5: ")) 
            assert 0 <= mark5 <= 100
        except ValueError:
            pass
        #create array/list with five marks
        marksList = [mark1, mark2, mark3, mark4, mark5]
        #print the array/list
        print(marksList)
        #calculate the sum and average
        sumOfMarks = sum(marksList)
        averageOfMarks = sum(marksList)/5
        #display results
        print("The sum of your marks is: "+str(sumOfMarks))
        print("The average of your marks is: "+str(averageOfMarks))
        break
    except: ValueError, 
    print("Invaild value")
    print("Please enter in a number equal to or greater then 0")
    print("But equal and or less then 100")