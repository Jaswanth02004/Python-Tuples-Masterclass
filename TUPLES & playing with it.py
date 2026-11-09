#ONE
"""
text = "Jaswanth"
tupp = tuple(text)
tuppp = list(tupp)
print(tupp)
print(tuppp)
"""

#TWO
'''
tuple = ("jaswanth")
print(tuple[1])     #a
print(tuple[:3])    #jas
print(tuple[3:])    #wanth
print(tuple[2:6])   #swan
print(tuple[:3]+tuple[3:])  #jaswanth
'''

#THREE
'''
text = ("ONE", "TWO", "THREE")
a,b,c = text
print(a,b,c)
'''

# FOUR
'''
a = ('a','b','c')
b = (1,2,3)
c = tuple(a+b)
print(c)
'''

#FIVE
'''
text = "jaswanth"
textt = tuple(text)
print(textt[::-1])  #('h', 't', 'n', 'a', 'w', 's', 'a', 'j')
print(textt[2:6])   #('s', 'w', 'a', 'n')
'''

#FIVE
'''
tupp = (1,2,3,4,5)
a,*b,c,d = tupp
print(a,b,c,d)
'''

#SIX
tupp = (1,2,3,[4,5])
print(tupp[3][0])
