def spamrun(fn):
    def sayspam(*args):
        print("spam,spam,spam")
        fn(*args)
    return sayspam
def spamrun2(fn):
    def sayspam2(c,d):
        print("spam2,spam2,spam2")
        fn(c,d)
    return sayspam2
@spamrun
def useful(a,b):
    print(a+b)
@spamrun2
def useful2(a,b):
    print(a*b)
if __name__ == '__main__':
    useful(2,5)
    useful2(3,5)
