from collections import defaultdict
import random
import string

class Codec:
    def __init__(self):
        self.codeDB = defaultdict()
        self.urlDB = defaultdict()
        self.chars = string.ascii_letters + string.digits

    def getCode(self):
        code = ''.join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com/" + code

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.urlDB: 
            return self.urlDB[longUrl]
        code = self.getCode()
        while code in self.codeDB: 
            code = self.getCode()
        self.codeDB[code] = longUrl
        self.urlDB[longUrl] = code
        return code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.codeDB[shortUrl]

url = "https://leetcode.com/problems/design-tinyurl"
mycodec = Codec()
tinyurl = mycodec.encode(url)
print(tinyurl)
longurl = mycodec.decode(tinyurl)
print(longurl)