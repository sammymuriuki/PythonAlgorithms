from collections import defaultdict
from collections import Counter

def getOddOccurrence1(myString):
    count = defaultdict(int)
    for letter in myString:
        count[letter] += 1
    for letter in myString:
        if count[letter] % 2 != 0:
            return letter


def getOddOccurrence2(myString):
    count = Counter(myString)
    for letter in myString:
        if count[letter] % 2 != 0:
            return letter


# driver code
myString = "llo world!"
print(getOddOccurrence2(myString))

# Output: "l"
