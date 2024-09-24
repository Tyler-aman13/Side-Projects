import math
import functools

a = 270 * .33333334
print(a)
print(math.sin(a))
''' sup this is my comment below are some dictionaries for fun {}'''

this_Dict = {'name':'William', 'age':25, 'city':'London'}

this_Dict["name"]

for key,value in this_Dict.items():
    print (key,value)

''' lists these are ordered unlike dictionaries []'''

things = [1,2,3,5,7,11]

'''time to stop using for loops, rip to the loops'''

def make_Bigger(x): return x+1

print(list(map(make_Bigger,things)))

'''map function it lets you map a function onto a list because its organinzed'''
'''can also do this within the map function using lambda'''

print(list(map((lambda x: x*7),things)))

''' x**y is a function that puts x to the power of y'''
''' similarly to map you can use list(filter(function, list)) and reduce(funciton,list) 
to produce a list of the pieces that fit the inserted filter funciton or a single number with reduce
reduce can also be used to find like a sum of a list or the larges input
if used with proper functions'''

'''Advantages of Python:
- versatile
- open source
- has a bunch of libraries
- greaet for prototypes
- productivity

disadvantages:
- speed limitations
- problems with threading (is a solution with a particular package)
- not native to mobile dev
- Memory consumption

Hashable: a object is hashable if it has a hash value which never changes during its lifetime(it needs a __hash__() method),
and can be compared to other objects (it needs an __eq__() method). hashable objects which compare equal must have the same hash value
this makes the object usable as a dictionary key and a set member because these data structures use the hash value internally

mutable vs immutable: data types in python can either be changed or not changed. for example an int is not mutable.
this is because changing an int causes it to become a new object(remember everything in python is in fact an object) in python (AKA its not the same thing).
however lists are mutable, you can append to a list and the object id remains the same
mutable objects: list, set, dict
immutable objects: int, float, bool, complex, tuple, frozenset, str

#greedy Algorithms
 used in optimiation problems
 key words are (min/max,longest/shortest,largest/smallest)
 follow simple format:
    find best choice and perform it
    just do what looks best until done
    assume best choice at every step leads to best final answer
 how to know the greedy algo works:
  use intuition:
    try a bunch of ideas
    find counterexamples (if none you are probably right)
 Steps to use:
    id the different steps and choices of a problem
        have comparable choices (and have a way to determine if a choice is better than another)
    check if greedy works
        try finding small cases where greedy isn't optimal
        if cases pass try to deduce why the greedy is optimal
 why use greedy:
    simple to code
    doesn't use complex algorithms
    runtime is fast usually O(n) or O(nlogm)
    however greedy isn't always optimal
 example prob:
    make change with fewest coins possible: (1,5,10,50,100)
    solution:
        step/state: an amount of change you have left
        choice: which coin to use
        so start with 100
        then go to 50 if 100 wont work
        so on and so on
        this works because the coins are multiples of each other, if that is not the case it would likely involve needing to do dynamic programming







