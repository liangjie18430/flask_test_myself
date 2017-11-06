class my_staticmethod(object):
    def __init__(self,function):
        self.function = function
    def __get__(self, instance, owner):
        def wrapper(*args,**kwargs):
            print("static method")
            return self.function(*args,**kwargs)
        return wrapper
class Class2(object):
    @my_staticmethod
    def get_user(x):
        return x,"get_user"
print(Class2.get_user("111"))