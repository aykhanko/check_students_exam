from colorama import Fore 

#Add students info

class Student():
    def __init__(self, name, surname , point):
        self.name = name
        self.surname = surname
        self.point = point

    def display_info(self):
        print(Fore.WHITE + f"Student: {self.name} {self.surname} Point:{self.point}")

#Check students exam

class Check(Student):
    def check_exam(self):
        if self.point>=51:
            print(Fore.GREEN + f"Student: {self.name} {self.surname} passed exam")

        else:
            print(Fore.RED + f"Student: {self.name} {self.surname} failed exam")


student1 = Check("Lamine","Yamal", 86)
student2 = Check("Mike","Aurelian", 50)
student3 = Check("Ali","Yildirim",91)
student4 = Check("Tony","Adams",25)
student5 = Check("Franck","Ribery",99)


for x in (student1,student2,student3,student4,student5):
    x.display_info()
    x.check_exam()




