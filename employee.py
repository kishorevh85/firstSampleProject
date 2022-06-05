class employee:
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob

    def show(self):
        print(f'The object details - name - {self.name} age - {self.age}, dob = {self.dob}')


emp = employee(name='kishore', age=22, dob='30/11/1985')
emp.show()
