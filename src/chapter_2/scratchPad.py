first = [1,2,3,4,5]
second = first
second.append(6)
print(first)
print('both first and second point to the same object !')
third = second.copy()
third.append(7)
print(second)
print(third)
print('third points to a different object')
# ------------------------------------------------------

saying = "Don't panic!"
letters = list(saying)
letters[3]

first = letters[0]
last = letters[-1]

print('Python extends list bracket notation...')
# ------------------------------------------------------


