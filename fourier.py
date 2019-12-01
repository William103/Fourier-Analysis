import math

# read the data into a list and process it a little bit
data = []
with open("fourier.txt", "r") as f:
    data = [float(x) for x in f.readlines()[0].replace('(','').replace(')','').split(',')]

# returns the discrete inner product of two functions, fun1 and fun2
def inner_product(fun1, fun2, N):
    product = 0
    for i in range(N):
        product += fun1((i+1)/N) * fun2((i+1)/N)
    product *= 2/N
    return product

# handy little function returning a sine wave of a given frequency
def sinfreq(freq):
    def sin(x):
        return math.sin(2 * math.pi * freq * x)
    return sin

# same thing but cosine
def cosfreq(freq):
    def cos(x):
        return math.cos(2 * math.pi * freq * x)
    return cos

# the mystery function we are dealing with
def mystery(x):
    x = math.floor(1000 * x)
    return data[x-1]

# two lists of frequencies and notes to test
frequencies = [262, 277, 293, 311, 330, 349, 370, 392, 415, 440, 466, 494]
symbols = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B']

# The idea here is to iterate through each note and see if the resulting dot
# product is greater than 0, give or take 0.1. If it is, then the corresponding
# basis vector, i.e. the sine wave (or cosine, it doesn't really matter) with
# that particular frequency, has a nonzero coefficient. The mystery wave then,
# is the sum of those waves multiplyied by their coefficients, so it is made up
# of notes with those frequencies.
for frequency, symbol in zip(frequencies, symbols):
    prod = inner_product(sinfreq(frequency), mystery, 1000)
    if abs(prod) > 0.1:
        print(str(symbol) + ':\t' + str(prod))
