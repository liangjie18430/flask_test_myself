class test(object):
    def __init__(self,score=1,name='test'):
        self._score = score
        self._name = name
    #@property
    def gscore(self):
        return self._score
    #@score.setter
    def sscore(self,score):
        self._score = score
    def name(self):
        return self._name
    def name(self,name):
        if name == 'new':
            raise ValueError("can't use the new")
        self._name = name
    score = property(gscore,sscore)
    #score = property(gscore)
    #score.setter(sscore)

if __name__ == '__main__':
    t = test()
    #print("first",type(t.score))
    print(t.__dict__)
    print(t._name)
    t.score = 10
    t._name='new'#t.name('new')
    t.name = 'new'

