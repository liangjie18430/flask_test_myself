#http://www.jb51.net/article/80112.htm
class NonNeagtive(object):
    def __init__(self):
        pass
    #owner means the cls
    def __get__(self, instance, owner):
        return "descriptor get:"+str(instance.__score)


    def __set__(self, instance, value):
        if value <0:
            raise ValueError("score can't be negative numer!")
        print("descriptor set:",value)
        instance.__score=value

type
class MathScore():
    score = NonNeagtive()

    def __init__(self,std_id,score):
        self.std_id = std_id
        if score<0:
            raise ValueError("score can't be negative number")
        self.__score = score

    def check(self):
        if self.__score>=60:
            return 'pass'
        else:
            return 'failed'
if __name__ == '__main__':
    xiaoming = MathScore(10,90)
    print('first',xiaoming.__score)
    print(xiaoming.score)