def fizzbuzz(t):
    for i in t[1:]:
        if i % 3 ==0 and i % 5 == 0:
            print 'fizz buzz',i
        elif i % 3 == 0:
            print 'fizz',i
        elif i % 5 == 0:
            print 'buzz',i
