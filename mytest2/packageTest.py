
from mytest import *

from mytest.annotationTest import spamrun

@spamrun
def fuc(a,b):
    print(a*b)


if __name__ == '__main__':
    fuc(1,2)
