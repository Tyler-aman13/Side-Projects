##Common questions for python

print("hello world")


## Questions Below
'''Reverse a String
Write a Python function to reverse a given string.'''
#Break Down Question:
#1. Create Function (so it can be repeated)
#2. take string as input
#3. Return reverse of string

#function taking a string
def reverse(string_in):
    #iterates through the given string starting from the end and going to the beginning one step at a time
    return string_in [::-1]

#test with my name
print(reverse("tyler"))

print('tame'[slice(-1,-len('tame')-1,-1)])

#creating a list
list_boi = ["hi","i'm", "paul"]

#mapping the reverse function for each element in the list
print(list(map(reverse,list_boi)))


'''Check for Palindrome
Write a function to check if a given string is a palindrome.'''
#Question breakdown
#1. Create a function that intakes string
#2. compares input to the reverse of its own input
#3. prints a statement based on the result
def pal_boi(string_in):
    if string_in == string_in[::-1]:
        return print(string_in, "is a palindrome")
    else:
        return print(string_in, "is not a palindrome")

pal_boi("tame")
pal_boi("racecar")

'''Fibonacci Sequence
Write a function that returns the Fibonacci sequence up to n numbers.'''
#question breakdown:
#1. create a function that takes in value n
#2. function calculates each value in the sequence up to n
#3. returns list of numbers that are apart of the sequence up to n

#iterative approach effiecent for large values of n
def fibonacci_iterative(n):
    #define the known values
    fib_sequence = [0, 1]
    #if we get zero it should return no numbers
    if n <= 0:
        return []

    #the first int in the sequence is just the first entry in the sequence
    elif n == 1:
        return fib_sequence[0:1]

    #we know that the list for the first ones
    elif n == 2:
        return fib_sequence

    #now we will create the sequence using the sum of the previous two numbers and appending it to the list
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    return fib_sequence

print(fibonacci_iterative(7))

#recursive with caching to make sure we don't spend time recalculating values
def fibonacci_memoization(n, cache={0: [0], 1: [0], 2: [0, 1]}):
    #setting the base cases so we don't recure infinitely
    if n in cache:
        return cache[n]
    #setting up recursion which will create the list we use
    fib_sequence = fibonacci_memoization(n - 1)
    #this will take the list created above and add to the the end the last two entries and put them in the dictionary as the integer
    cache[n] = fib_sequence + [fib_sequence[-1] + fib_sequence[-2]]
    #returns the entry in the dictionary that we set up above
    return cache[n]

print(fibonacci_memoization(7))


'''Find the Largest Element in a List
Write a Python function to find the largest element in a list.'''
#question breakdown
#1. function receives list
#2. orders list from smallest to largest
#3. finds largest element
#4. finds where largest element is in the original list
#5. prints the element and what number it is

test_list = [1,7,8,15,3,45,45,7]

def largest(list_in):
    #sorting list
    sorted_list = sorted(list_in)
    #taking the largest element which is last in the list
    largest_el = sorted_list[-1]
    # we return a printed statement letting people know that the elements in the list
    return print("elements", [i for i,x in enumerate(list_in) if x == largest_el], "are the largest with value", largest_el)

largest(test_list)

'''Remove Duplicates from a List
Write a function that removes duplicates from a list while maintaining the original order.'''
#question breakdown
#1. create a function that takes a list as an arguement
#2. check if the list has duplicates if so return same list
#3. if duplicates find the duplicates and remove them and return the list in the same order
l1 = [1,2,1]
l2 = [1,2,3]
l3 = ["turtle",1,"turtle"]

#what to learn from this: dictionaries maintain order but also remove duplicates easily
def remove_dup(list_dup):
    if len(list_dup) == len(set(list_dup)):
        return list_dup
    else:
        return list(dict.fromkeys(list_dup))

print(remove_dup(l3))



'''Check for Anagrams
Write a Python function to check if two strings are anagrams of each other.'''
#question breakdown
#1. create a function that takes two strings
#2. take both words and split them up into their individual letters and order them
#3. compare both lists have the same length
#4. then check is the ordered lists are the same
#5. return a phrase that states if they are or are not anagrams

stringr = "cinema"
stringe = "iceman"
print(sorted(stringr))

def anagram (string1, string2):
    sortstring1 = sorted(string1)
    sortstring2 = sorted(string2)
    if sortstring1 == sortstring2:
        return print(string1, "and", string2, "are anagrams")
    else:
        return print(string1, "and", string2, "are not anagrams")

anagram(stringr, stringe)


'''Count Vowels in a String
Write a function to count the number of vowels in a given string.'''
#question breakdown
#1. function intakes string
#2. filters out non-vowels in a list
#3. finds and returns length of remaining string

def vowels (stringin):
    vowels = {"a","e","i","o","u","y","A","E","I","O","U","Y"}
    return len(list(filter(lambda x: x in vowels, stringin)))

print(vowels("pOpo butmUnch"))

'''Merge Two Sorted Lists
Write a function that merges two sorted lists into one sorted list.'''
#question breakdown:
#1.function takes in two sorted lists
#2. combine two lists
#3. sort again

def sortlist(list1, list2):
    return sorted(list1 + list2)

print(sortlist([1,2,3],[4,6,3]))

'''Find the Intersection of Two Lists
Write a function to find the intersection (common elements) of two lists.'''
#Question Breakdown:
#1. function takes in two lists
#2. create a blank list that will house the common elements of the two lists
#3. iterate through each element in one list against the other
#4. if entries are the same add it to the blank list
#5. go through each entry in the list until we reach the end, and return the finalized list

def commonelements (list1, list2):
    #using the set intersection method is faster in terms of time complexity than iterating through the each list.
    #remember lookups in sets are O(1) versus lists are O(n) and if you are comparing two lists it is O(n*m)
    return list(set(list1).intersection(list2))

print(commonelements([1,2,3,5], [1,2,3,4]))

'''Find the First Non-Repeating Character in a String
Write a Python function to find the first non-repeating character in a given string.'''
#question breakdown:
#1. function intakes a string
#2. get a count for each character in the string
#3. eliminate the characters that appear more than once
#4. for each remaining character check where it is in the string
#5. return the letter with the lowest element
from collections import Counter


stringboi = "dodobird"


def nonrepeatfind(stringin):
    stringcount = Counter(stringin)
    nonrepeat = []
    charreturn = ""
    placement = -1

    for character in list(stringcount):
        if stringcount[character] == 1:
            nonrepeat.append(character)

    print(nonrepeat)

    for i in nonrepeat:
        if placement == -1 or stringin.index(i) < placement:
            charreturn = i
            placement = stringin.index(i)

    return charreturn

print(nonrepeatfind(stringboi))

def nonrepeatfindtwo(stringin):
    stringcount = Counter(stringin)

    for character in stringin:
        if stringcount[character] == 1:
            return character

    return None


print(nonrepeatfindtwo(stringboi))
