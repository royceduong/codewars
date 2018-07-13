import math

# def get_middle(s):
#     if len(s) % 2 == 0:
#         e = len(s)/2
#         f = e - 1
#         print(s[f] + s[e])
#         return s[f] + s[e]
#     else:
#         print(s[int(math.floor(len(s)/2))])
#         return s[int(math.floor(len(s)/2))]

# s = "royceduong"
# print(s[4.5:3.33])

def get_middle(s):
    print((len(s)-1)/2:len(s)/2+1)
    # print(s[(len(s)-1)/2:len(s)/2+1])
    return s[(len(s)-1)/2:len(s)/2+1]
get_middle("test")
get_middle("testing")
get_middle("middle")
get_middle("A")
get_middle("of")
# Test.assert_equals(get_middle("test"),"es")
# Test.assert_equals(get_middle("testing"),"t")
# Test.assert_equals(get_middle("middle"),"dd")
# Test.assert_equals(get_middle("A"),"A")
# Test.assert_equals(get_middle("of"),"of")