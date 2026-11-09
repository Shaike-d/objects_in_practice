class User:

    def __init__(self,age):
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value < 0 or value > 120 :
            raise ValueError("age must be 0-120")
        self.__age = value


def answer_4():
    user = User(30)
    user.age = user.age + 1
    print(user.age)
    try:
        user.age = -5
    except ValueError as error:
        print("error:", error)
    print(user.age)

