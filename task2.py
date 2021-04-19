#   STARTING POINT OF ASCENDING PATTERN
ascending_start = 1
#   STARTING POINT OF DESCENDING PATTERN
descending_start = 5

#   CREATE A FOR LOOP THAT WILL GO UP TILL 5, WHICH WILL MAKE THE ROWS
for x in range(5):
    #   THIS LOOPS RANGE WILL CHANGE BECAUSE OF THE ascending_start
    for y in range(ascending_start):
        # PRINT *, THE end PARAMETER BASICALLY MAKES SURE THAT THE NEXT PRINT IS ON THE SAME LINE
        print("*", end="")

    #   UPDATE THE ascending_start VARIABLE FOR THE NEXT ITERATION
    ascending_start = ascending_start + 1
    #   START A NEW LINE
    print("\n")

#   SAME THING JUST IN REVERSE
for x in range(5):
    for i in range(descending_start):
        print("*", end="")

    descending_start = descending_start - 1
    print("\n")

















#NK SAMPLE ANSWER
ascending_start = 0
descending_start = 5

range_changer = True
for x in range(10):
    if range_changer:
        ascending_start = ascending_start + 1
    else:
        ascending_start = ascending_start - 1

    for y in range(ascending_start):
        if descending_start - 1 == y:
            range_changer = False
        print("*", end="")
    print("\n")
