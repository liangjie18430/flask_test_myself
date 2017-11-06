class Test(object):

    def instaceFunc(self,c):
        print(c,"instance function")

    @classmethod
    def classFunc(cls,a):
        print(a,"class function")


    @staticmethod
    def staticFunc(c):
        print(c,"static func")


if __name__ == '__main__':
    t = Test
    m=t()
    try:
        t.instaceFunc("class revoke")
    except Exception:
        print("can't use class revoke instanceFunc")
    t.instaceFunc(m,"class revoke with object")
    m.instaceFunc("object revoke")
    t.classFunc("class revoke")
    t.staticFunc("class revoke")
    m.classFunc("object revoke")
    m.staticFunc("object revoke")

