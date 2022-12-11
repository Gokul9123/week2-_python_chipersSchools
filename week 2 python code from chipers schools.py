#CLASS 1
# funtions
# we use functions to make simple
print("loading")
print("loading")
print("loading")
# instead of printing these 3 times by using functions we can make simple
# def introdutions the name of the funtions
def show_loading():
    for _ in range(3):
        print("loading")
show_loading()

def show_loading():
    for i in range(3):
        print("loading","."*(i+1))
show_loading()

#functions can take parameters
def sheldon_knock(name):
    for _ in range(4):
        print("gokul","gokul","gokul",name)
sheldon_knock("leader")
# RETRUN STATEMENTS
def add(a,b):
    return a+b
a=add(1,2)
print(a)

#CLASS=2
#key arguments
def func(a,b,c):
    print(a)
    print(b)
    print(c)
func(1,2,3)
print(1,2,3,sep=",")
def func(a,b,c):
    print(a)
    print(b)
    print(c)
#func(1,2,3)
def hello():
    print("Hello world :")
a = hello
a()
hello =2
print(hello)
a()
def func():
    print(1,2,3,4,sep=",")
func()
def func(a=1, b=2):
    print(a,b)
func()
func(2)
func(34,45)
def func(a,b,*c):
    print(a,b,c)
func(1,3,4,5,5,3,3,4,"Mano","sahoo")
def func(a,b,*c,d,e="Mano"):
    print(a,b,c,d,e)
func(55,6,566,"Mano",d="Sahoo")
def func(**c):
    print(c)
func(name="Mano")
print(sorted([3,5,8,1,28,7,5,2,24,5]))
add = lambda a,c:a+c
print(add(1,2))
a =5
c = print(a)
print(c)

# class ----> 3
show = print
show("Hello World")
a = ["mano","jatin",1,1.5,"mansaj"]
for name in a:
    print(name)
a =9
b=4
temp =a+b
b = temp-b
a = temp-a
print("a=",a)
print("b=",b)
names = ["Mano","Anjan","jeeban","Ayush"]
scores=[50,22,32,21]
for i,name in enumerate(names):
    score = scores[i]
    print(name, "-",score)
for name,scores in zip(name,scores):
    print(name,"-",scores)

#class ----> 4
a,b,c,d = 1,2,3,4
print("a = {2}, b ={1}, c={0}".format(c,b,a))
name = "Manoranjan"  
print(f"name= {name}")
print(len(r"a\nb"))
print("      1     MAno     ".strip())
print("Manoranjan".replace("a","z"))
print("1,2,3,4,5".split(","))
print("Mano".count("a"))

#class ---> 5
a =[78,89,977,89]
print(a)
print(a[2])
print(a[-2])
a.insert(1,100)
print(a)
a.pop()
a.remove(100)
a.sort()
a.reverse()
print(a)
print([3747,74,848,94]+[464,83,847,84])
print(78 in a)
#sorted() this only retuns sorted value but dont change the value like sort(). 
#reversed() it also only return reverse list not cgange original list like reverse().also called lazy loading
print(list(map(lambda x:x**2,a)))
print(",".join(["jatin","samarth","molly"]))

#class--->6
a =(34,43,54,5,4,5)#tuple
print(type(a))
print(list(a))
b= {"name":"Mano"}#dictionary
print(b["name"])

#class ---> 7

b = {1,2,3,4,5,7}#set
print(type(b))
for i in b:
    print(i)
a={1,2,7,8,6,5,6}
print(a-b)
print(a.union(b))
print(a.intersection(b))
a.add(85)
a.remove(5)
print(a)

#class---> 8

a =[]
for i in range(5):
    a.append(i)
print(a)
print((j for j in range(5))for i in range(5))
print( i**2 for i in range(5))
a in range(5)
it =iter(a)
print(next(it))

#class ---> 9

student1 ={"name": "Mano"
        "marks: 100"}#Abstraction
class person:
        pass
p=person()#object
print(p)
class person:
        name ="Mano"
        def say_hi(self):
                print(f"Hello Everyone! I am {self.name}")
p=person()
p.say_hi()
person.say_hi(p)

#class ---> 10
class A:
    def _init_(self):
        print(self)
        print("initialised")
    def _del_(self):
        print(self)
        print("i am dying")
a =1
print(type(a))
print(a.__add__(5))
print(a.__mul__(5))

class A:
    a=1
    b=2
    def __add__(self,x):
        return self.a + self.b +x




