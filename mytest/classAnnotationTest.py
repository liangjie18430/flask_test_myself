class Foo(object):
    def __init__(self,func):
        self._func = func


    def __call__(self, *args, **kwargs):
        print('class decorator runing')
        self._func(*args,**kwargs)
        print('class decorator ending')

@Foo
def bar(**b):
    print(b)


bar(c='c')