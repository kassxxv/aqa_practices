class Student:
    def __init__(self, name:str, surname:str, age:int, avr_score:float):
        self.name = name
        self.surname = surname
        self.age = age
        self.avr_score = avr_score

    def change_score(self, new_score):
        self.avr_score = new_score


first_student: Student = Student('Filip', 'Fylyp', 18, 84.4)

print(f'Студента звати {first_student.name} {first_student.surname}, йому {first_student.age} років, його середній бал = {first_student.avr_score},')
first_student.change_score(28)
print(f'Після зміни його середній бал = {first_student.avr_score}.')