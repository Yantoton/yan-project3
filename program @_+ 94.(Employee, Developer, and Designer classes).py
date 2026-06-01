class Employe:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Developer(Employe):
    def __init__(self,name,age,salary):
        super() .__init__(name,age)
        self.salary = salary

class Designer(Developer):
    def __init__(self,name,age,salary,id):
        super() .__init__(name,age,salary)
        self.id = id

info = Designer("Rashid",25,100,420)
print(f"Salary:{info.salary} Id:{info.id}")
