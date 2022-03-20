# daily challenge 03-19-2022
import collections

class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        valfreq = self.freq[val] + 1
        self.freq[val] = valfreq
        if valfreq > self.maxfreq:
            self.maxfreq = valfreq
        self.group[valfreq].append(val)
        

    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return val

freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
freqStack.push(7)
freqStack.pop()
print(freqStack.group)
print(freqStack.freq)
# freqStack.pop()
# freqStack.pop()
# freqStack.pop()