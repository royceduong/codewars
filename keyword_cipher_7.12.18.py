abc = 'abcdefghijklmnopqrstuvwxyz'
key = 'keyword'
class keyword_cipher(object):
    def __init__(self, abc, keyword):
        for letter in keyword:
            self.clean_abc = abc
            self.abc = abc
            if letter.isalpha():
                clean_letter = letter.lower()
                modified = self.abc.replace(clean_letter,'')
                abc = modified
            new_abc = keyword.lower() + abc
            self.crypt = new_abc
            # print(self.abc)
            # print(self.crypt)
    def encode(self, string):
        self.crypt
        self.array = []
        for letter in string:
            # print(letter)
            for l in self.clean_abc:
                print(l)
                if letter == l:
                    index = self.clean_abc.find(l)
                    self.array.append(index)
        print(self.array)
        result = ''
        for idx in self.array:
            result += self.crypt[idx]
        # print(result)
        return result


        #input 'abc'
        #return 'key'
        # what is happening here?
        # arguments recieved will look through the equivalent placement within self.crypt

    
        

    # def decode(self, str):
    #     pass;

cipher = keyword_cipher(abc, key)
cipher1 = keyword_cipher(abc, key)
cipher.encode('abc')
cipher1.encode('def')

# key = 'keyword'

# for letter in key:
#     if letter.isalpha():
#         clean_letter = letter.lower()
#         modified = abc.replace(clean_letter,'')
#         abc = modified
#     new_abc = key.lower() + abc
#     print(new_abc)
