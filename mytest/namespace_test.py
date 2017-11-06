
a_string = "This is a global variable"
def foo():
     print("local",locals())
print("globals",globals() )# doctest: +ELLIPSIS

foo()
