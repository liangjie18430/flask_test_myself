class test(object):
    def __init__(self,score=1,name='test'):
        self._score = score
        self.__name = name
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score):
        self._score = score
    def name(self):
        return self.__name
    def name(self,name):
        if name == 'new':
            raise ValueError("can't use the new")
        self.__name = name

if __name__ == '__main__':
    t = test()
    t.score = 10
    print(t.__dict__)
    print(t.__name)
    t.__name='new'#t.name('new')
    t.name = 'new'
    print(t.__dict__)
