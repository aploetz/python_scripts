def readnum(prompt, min=None, max=None):
    while True:
        x = raw_input(prompt + ' ')
        try:
            val = int(x)
        except ValueError:
            print "%r is not an integer. Try again.\n" % (x,)
            continue
        if min is not None and val < min:
            print "The answer must be at least %d. Try again.\n" % (min,)
        elif max is not None and val > max:
            print "The answer must be at most %d. Try again.\n" % (max,)
        else:
            return val

numNodes = readnum(" How many nodes are in your cluster?",1,1024)
endRanges = []

# build end ranges
for counterj in range(numNodes):
    endRanges.append(str(((2**64 / 5) * counterj) - 2**63))

print "node  start range              end range"
# determine start ranges from end ranges
for counteri in range(numNodes):
    # determine start range from end range array
    if counteri == 0:
        startRange = str(long(endRanges[numNodes-1])+1)
    else:
        startRange = str(long(endRanges[counteri-1])+1)

    # print range for each node
    print "%d)    %s to %s" % (counteri, startRange, endRanges[counteri])
