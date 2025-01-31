def fizzBuzz():

    for i in range(1, 101):
        message = ''

        if i % 3 == 0:
            message += 'Fizz'

        if i % 5 == 0:
            message += 'Buzz'

        if (message == ''):
            message = str(i)

        print(message)

# An alternative way of solving fizz-buzz. It uses lists and a nestled for-loop instead of sequential if-conditions 
# This way might not be as 'intuitive' but shows how you can program in a way such that it is easy to change and evolve in the future 
# If you wanted to make the function more general, you could seperate out the nestled list 'selectors'. For the purposes of this code demo, it is kept inside the function

def fizzBuzz_lists():
    selectors = [
        [3, 'Fizz'],
        [5, 'Buzz'],
        [7, 'Fuzz']
    ]

    for i in range (1, 101):
        msg = ''
        
        for (num, exchange) in selectors:
            if i % num == 0:
                msg += exchange

        if msg == '':
            msg = str(i)
        print(msg)

fizzBuzz_lists()