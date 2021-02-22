def hello(text):
    if 'P' not in text.upper():
        return

    for i in range(10): # range(2,10) ==> [2,3,4,5,6,7,8,9]
        print("Line #" + str(i), text)
    print('')
    

hello('Puff')
hello('Jiggly')
hello('Pook')


