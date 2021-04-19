#   DIVISIBLE MEANS WHEN DIVIDING BY A CERTAIN NUMBER GIVES A WHOLE NUMBER
#   SO WE TEST FOR THAT BY USING THE MODULUS OPERATOR
#   FIRST, WE CREATE A FOR LOOP THAT STARTS AT 1 AND ENDS AT 100
for i in range(1, 101):
    #   WE TEST FOR THE FIZZBUZZ FIRST SO THAT WE DON'T PRINT FIZZ AND BUZZ SEPARATELY BEFORE PRINTING FIZZBUZZ
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        # EXIT THIS CURRENT ITERATION

    #   NOW, WE TEST FOR FIZZ BY CHECKING THE MODULO BY 3 OF THE CURRENT NUMBER
    elif i % 3 == 0:
        print("Fizz")

    #   NOW, WE TEST FOR FIZZ BY CHECKING THE MODULO BY 5 OF THE CURRENT NUMBER
    elif i % 5 == 0:
        print("Buzz")

    #   IF ALL ELSE FAILS, JUST PRINT THE NUMBER
    else:
        print(i)

