
website = "www.baidu.com"

user = {"age": 12, "name": "jack", "sex": "male"}

class Student:
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
    def print_info(self):
        print(f'{self.__name}-{self.__age}-{self.__sex}')
    def get_name(self):
        print(self.__name)
    def set_name(self,name):
        self.__name = name

user["age"] = 19
wenjie = Student(user["age"], user["name"], user["sex"])
wenjie.set_name("pony")

if __name__ == '__main__':
    for item in website:
        print(item)

