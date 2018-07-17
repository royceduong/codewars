abc = 'abcdefghijklmnopqrstuvwxyz'
key = 'keyword'
class keyword_cipher(object):
    def __init__(self, abc, keyword):
        self.clean_abc = abc
        for letter in keyword:
            self.abc = abc
            if letter.isalpha():
                clean_letter = letter.lower()
                modified = self.abc.replace(clean_letter,'')
                abc = modified
            new_abc = keyword.lower() + abc
            self.crypt = new_abc
            # print(self.crypt)
            # print(self.abc)
            # print(self.crypt)
    def encode(self, string):
        self.array = []
        # print(self.clean_abc)
        for letter in string:
            for l in self.clean_abc:
                # print(l)
                if letter.lower() == l:
                    index = self.clean_abc.find(l)
                    self.array.append(index)
        # print(self.array)
        result = ''
        for idx in self.array:
            result += self.crypt[idx]
        print(result)
        print('hello')
        return result

    def decode(self, string):
        self.decode_array = []
        for x in string:
            for y in self.crypt:
                if x.lower() == y:
                    # print(x)
                    idx = self.crypt.find(y)
                    # print(idx)
                    self.decode_array.append(idx)
        result = ''
        for x in self.decode_array:
            result += self.clean_abc[x]
        print(result)
        return result

cipher = keyword_cipher(abc, key)
# cipher1 = keyword_cipher(abc, key)
# cipher.encode('abc')
# cipher.encode('xyz')
# cipher.decode("key") # , "abc")
cipher.decode("xyz") # , "abc")
# cipher.encode('ABCHIJ')


# key = 'keyword'

# for letter in key:
#     if letter.isalpha():
#         clean_letter = letter.lower()
#         modified = abc.replace(clean_letter,'')
#         abc = modified
#     new_abc = key.lower() + abc
#     print(new_abc)
