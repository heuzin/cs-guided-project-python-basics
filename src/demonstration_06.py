"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt):
    # Your code here
    xCount = 0
    oCount = 0
    for n in txt:
        if 'x' in n:
            xCount= xCount + 1
        if 'o' in n:
            oCount = oCount +1
    if (xCount == oCount):
        return True
    else:
        return False

print(XO("ooxx"))