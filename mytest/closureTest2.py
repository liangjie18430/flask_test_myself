def outer():
    a = 0
    b = 1

    def inner():
        print(a)
        b=4
        print(b)

        # b += 1        # A

        #b = 4  # B

    inner()


outer()

for i in range(10):
    print(i)

print(i)