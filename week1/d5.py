class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def average(self):
        sum=0
        for marks in self.__marks:
            sum+=marks
        print(f"{self.__name}'s average marks: {sum/len(self.__marks)}")

s1=Student("tom",[10,20,30,40,50])
s1.average()