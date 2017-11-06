def greeting_conf(prefix):
    def greeting(name):
        print(prefix, name)
    return greeting
mGreeting = greeting_conf("Good Morning")
print("function name is:", mGreeting.__name__)
print("id of mGreeting is:", id(mGreeting))
print("dir",dir(mGreeting))
print("__closure__",mGreeting.__closure__)
print("__closure__[0]",type(mGreeting.__closure__[0]))
print("__closure__[0].cell_contents",mGreeting.__closure__[0].cell_contents)
aGreeting = greeting_conf("Good Afternoon")
print("function name is:", aGreeting.__name__)
print("id of aGreeting is:", id(aGreeting))
cGreeting = greeting_conf("Good Afternoon")
print("function name is:", cGreeting.__name__)
print("id of cGreeting is:", id(cGreeting))
dGreeting = greeting_conf("Good Morning")
print("function name is:", dGreeting.__name__)
print("id of dGreeting is:", id(dGreeting))


