n = int(input("n ="))

# filled diamond
# upper half, plus "middle"
for i in range(n):
    # leading spaces
    for j in range(2*n-i-1):
        print (" ",end="")

    # filler
    for k in range(2*i+1):
        print(i,end="")
    print()

# bottom half
for a in range(n-2,-1,-1):
    # leading spaces
    for b in range(n-a+i):
        print (" ",end="")

    for c in range(2*a+1):
        print(a,end="")
    print()


print()

# empty diamond
# upper half, plus "middle"
for i in range(n):
    # leading spaces
    for j in range(2*n-i-1):
        print (" ",end="")

    if i > 0:
        print(i,end="")
        for k in range(2*i-1):
            print(" ",end="")
        print(i,end="")
        print()
    else:
        print(0)


# bottom half
for a in range(n-2,-1,-1):
    # leading spaces
    for b in range(n-a+i):
        print (" ",end="")

    if a > 0:
        print(a,end="")
        for c in range(2*a-1):
            print(" ",end="")
        print(a,end="")
        print()
    else:
        print(0)

