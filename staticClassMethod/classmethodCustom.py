class MyClassMethod(object):
    def __init__(self,function):
        self.function = function
    def __get__(self, instance, type=None):
        def wrapper(*args,**kwargs):
            print("class method:",type)
            return self.function(type,*args,**kwargs)
        return wrapper
class Class2(object):
    @MyClassMethod
    def get_user(cls,x):
        print(cls)
        return x,"get_user"
print(Class2.get_user("test"))

