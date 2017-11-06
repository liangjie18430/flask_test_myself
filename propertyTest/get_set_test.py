class test(object):

    def __init__(self,score=1):
        self._score = score

    def __get_score(self):
        return self._score

    def __set_score(self,score):
        self._score = score

    score = property(__get_score,__set_score)

if __name__ == '__main__':

    t = test()
    t.score = 10

    print(t.score)