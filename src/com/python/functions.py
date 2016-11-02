'''
Created on Sep 22, 2016

@author: abhay.jain
'''
def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y +a

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

print(add(1,2))
print(addFixedValue(10))

def list_benefits():
    l = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return l

def build_sentence(benefit):
    return benefit + " " + "is a benefit of functions"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print (build_sentence(benefit))

name_the_benefits_of_functions()


#Multiple function arguments
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: ", (first + second + third))

    if options.get("do") == "subtract":
        print(second - first)
        
    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first", do = "subtract")
print ("Result: ", result)


def foo(a, b, c, *args):
    return len(args)

def test(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if test(1,2,3,magicnumber = 6) == False:
    print("Great.")
if test(1,2,3,magicnumber = 7) == True:
    print("Awesome!")
