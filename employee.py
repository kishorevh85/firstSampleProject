class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'The object details - name - {self.name} age - {self.age}')

emp = employee('kishore',22)
emp.show()