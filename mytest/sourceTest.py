#use the construct
#the default classType is function,so use the lambda
args = property(lambda self: object(), lambda self, v: None, lambda self: None)
args2 = property(lambda self: object(), lambda self: None, lambda self: None)
args3=property(object(),None,None)
print(args)
print(args2)
print(args3)
#print(args.__dict__)