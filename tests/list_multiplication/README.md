# List multiplication
Gotcha: Python has handy feature of multiplying list which allows to repeat list's content N times.
Things can go awry if element is mutable object. What can surprise you is the feature doesn't copy objects 
but *repeats* elements. If we multiple list of lists for example, it's much safer to use list comprehension 
and make separate instances explicitly in case someone feels like mutating one of the lists. 