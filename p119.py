from Bird import *

print('\nClass Instances of:\n', Bird.__doc__)

polly = Bird('Squawk, squawk!')

print('\nNumber Of Birds:', polly.count)
print('\nPolly Says:', polly.talk())

harry = Bird('Tweet, tweet!')

print('\nNumber Of Birds:', Bird.count)
print('\nHarry Says:', harry.talk())
