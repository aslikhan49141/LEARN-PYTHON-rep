print("List Example")

a = [2,1,23,4,5,6,7,8,9,10]
print(a)
a[2] = 100
print(a)
a[3] = 2
print(a)
#removing an element from the list
a.remove(2)
print(a)
a.remove(2)
print(a)
#adding an element to the list
a.append(20)
print(a)

print("Tuple Example")
t = (1,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10)
print(t)
#t[2] = 100  # This would cause an error because tuples are immutable


print("Set Example")
s = {6,7,8,9,10,2,3,4,5,6,7,8,9,10,1,2,3,4,5,}
print(s)
s.add(20)
print(s)
s.add(20)  
print(s)

#s.remove(2)
#print(s)

set={'a', 'e', 'f', 'h', 'i', 'k', 's', 'w','x', 'g', 'h', 'i', 'k', 's', 'w','x','e'}
print(set)
# Huge scattered numbers and negative numbers mix up the bucket math
crazy_integers = {1, -5, 999999, 12, -856, 42, 77777}
print(crazy_integers)