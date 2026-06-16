x=3 
print(type(x)) 
print(x)
print(x+1)
print(x-1)
print(x*2)
print(x**2)

x=x+1
print(x)
x*=2
print(x)
y=2.5
print(type(y))
print(y,y+1,y*2,y**2)

#Booleans

t=True
f=False
print(type(t))
print(t and f)
print(t or f)
print(not t)
print(not f)
print(t != f)
print(t == f)

#strings
print(type("Hello World"))
a="Alif Shahiriar Likhan"
print(type(a))
print(a)

print(a[0])
print(a[1])
print(a[2])
print(a[0:5])
print(a[5:13])

print(a.upper())
print(a.lower())
print(a.replace("Alif Shahiriar Likhan","Lamiya Akter Sneha"))
print(a)
print(len(a))
print(a.split())

print("""
      Lamiya 
      Akter 
      Sneha""" )

t1= "Alif Loves Lamiya"
t2= "Lamiya Loves Alif"
print(t1)
print(t2)

t1, t2 = t2, t1 #replacing 2 variables
print(t1)
print(t2)

a = 10
print(f'The value of a is {a}')

a = 10
print(f'The value of a plus 5 is {a+5}')