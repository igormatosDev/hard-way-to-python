# -*- coding: utf-8 -*-
#name = 'Igor Matos'
age = 19
height = 74
weight = 172
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'


# %d => will format a number for display.
# %s => will insert the presentation string representation of the object (i.e. str(o))
# %r => will insert the canonical string representation of the object (i.e. repr(o))



print "Testing string with the name %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy. " % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


print "If i add %d, %d and %d I get %d." % (age , height , weight, age + height + weight)