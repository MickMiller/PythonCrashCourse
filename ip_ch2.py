'''
See README.md for this file's organization
'''

print("\nPython's simplest built-in data types: booleans, Integers, Floats and Strings ===============================")

print("\nObjects are: booleans, integers, floats, strings, large data structures, function and programs --------------")

print("\nIn Python class and type mean pretty much the same thing ----------------------------------------------------")
print("type(9):", type(9))
print("type(0):", type(0))
print("type(99.9):", type(99.9))
print("type('abc'):", type('abc'))

print("\nVariables ---------------------------------------------------------------------------------------------------")
print("a-z, A-Z, 0-9, \"_\" AND names can't begin with a digit AND if first char \"_\" treated specially")
print("Python reserved words:")
print(" False     cleass      finally     is          return")
print(" None      continue    for         lambda      try")
print(" True      dev         from        nonlocal    while")
print(" and       del         global      not         with")
print(" as        elif        if          or          yield")
print(" assert    else        import      pass")
print(" break     except      in          raise")

print("\nNumbers -----------------------------------------------------------------------------------------------------")
print("\n1+2=", 1 + 2)
print("3-1=", 3-1)
print("2*3=", 2*3)
print("3/2=", 3/2)
print("3//2=", 3//2)
print("3 % 2=", 3 % 2)
print("3 ** 2=", 3 ** 2)
print("a = 1")
a = 1
print("a += 2 so ", end="")
a += 2
print("a =",a)

print("\nPythons main exception handling mechanism is to throw an exception ------------------------------------------")

a = 2 + 3 * 4
print("\nPrecedence: -------------------------------------------------------------------------------------------------")
print("2 + 3 * 4 = 2 + (2 * 4) =", a)

print("\nBases: 16 = 0b10000 = 0o20 = 0x10 ---------------------------------------------------------------------------")
a = 16
print("a=", a)
b = 0b10000
print("b=0b10000=", b)
c = 0o20
print("c=0o20=", c)
d = 0x10
print("d=d=0x10=", d)

print("\nType conversions --------------------------------------------------------------------------------------------")
print("Boolean=", True, end="")
print(", Boolean converted to int=", int(True))
print("int(98.6)=", int(98.6))
# to keep exit code of non-error = 0 line commented out print(int("99 bottles of beer on the wall"))

print("\nIntegers can be of ANY size! --------------------------------------------------------------------------------")

print("\nFloats ------------------------------------------------------------------------------------------------------")
print("float(True)=", end="")
print(float(True))
print("float(98)=", end="")
print(float(98))

print("\nStrings are immutable, aka you can't change a string --------------------------------------------------------")

print("\nYou can put single quotes inside double quotes AND double quotes inside single quotes -----------------------")

print("\nEscape with \ -----------------------------------------------------------------------------------------------")
palindrome = "A man, \nA plan,\nA canal:\nPanama."
print("A man, \\nA plan,\\nA canal:\\nPanama.")
print(palindrome)

print("\ncombine string with + ---------------------------------------------------------------------------------------")
print('print("2b OR NOT" + " 2b=SQRT(4b**2)") prints next line')
print("2b OR NOT" + " 2b=SQRT(4b**2)")

print("\nDuplicate with * --------------------------------------------------------------------------------------------")
print("You should give 3 examples")
print(3 * "example ")

print("\nExtract character with [] -----------------------------------------------------------------------------------")
letters = "abc"
print("Extract 2nd letter from 'abc'", letters[1])

print("\nSlice with [start: end: step] -------------------------------------------------------------------------------")
print("letters: 'abcdefghijklmnopqrstuvwxyz'")
letters = "abcdefghijklmnopqrstuvwxyz"
print("[:]=", letters[:])
print("Offset from 20 to the end letters[20:]=", letters[20:])
print("Offset from 20 to the end letters[-6:]=", letters[-6:])
print("First, second and third letters[0:3]=", letters[0:3])
print("First, second and third letters[-26:-23]=", letters[-26:-23])
print("From start to end, in steps of 7 characters letters[::7]=", letters[::7])
print("Get length with len(letters)=", len(letters))
string="a.b.c.d"
print("string=", string)
print("string.split('.')=", string.split('.'))
monster_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
monster_string = ','.join(monster_list)
print("monster_string = ','.join(monster_list) =", monster_string)
print("case and alignment")
setup = 'a duck goes into a bar...'
print("Note the string setup is unchanged, request to change printed string obeyed")
print("setup.capitalize()=", setup.capitalize())
print("right justify=", setup.rjust(30))
print("replace duck=", setup.replace('duck', 'mammoset'))

print("Things to Do --------------------------------------------------------------------------------------------------")
print("Seconds in hour=60 sec/min * 60 min/hour=", 60 * 60, "sec/hour")
seconds_per_hour = 60 * 60
print("seconds/day=seconds/hour * hour/day=", seconds_per_hour * 24, "seconds/day")
seconds_per_day = seconds_per_hour * 24
print("seconds_per_day/seconds_per_hour=", seconds_per_day/seconds_per_hour)
print("seconds_per_day//seconds_per_hour=", seconds_per_day//seconds_per_hour)

print("\nPy filling: Llists, Tuples, Dictionaries and Sets ===========================================================")

