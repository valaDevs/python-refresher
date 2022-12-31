def add(x,y):
    return x + y

print(add(3, 3))


m = lambda x,y : x + y 
print(m(2,3))

# super
b = (lambda s,d : s + d)(4,7)
print(b)

sequence = [1,2,3,4,5,6]
doubled = [(lambda x:x * 2)(x) for x in sequence]
doubled =list( map(lambda x:x * 2, sequence))
