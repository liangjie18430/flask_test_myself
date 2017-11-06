class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
    def __call__(self, *args, **kwargs):
        pass

if __name__ == '__main__':
    s = Student()
    s.birth=1992
    print(s.birth)
    print(s.age)
    try:
        s.age=10
    except Exception:
        print("can't not set the age")