# # exercise 1-2:
#
#
# def longest_string(str1, str2):
#     if len(str1) > len(str2):
#         return str1
#     if len(str1) < len(str2):
#         return str2
#     if len(str1) == len(str2):
#         return  True
#
#
# long_str = longest_string("aa", "dd")
# print(long_str)


# # exercise 3:


def is_long_string(str):
    if len(str) > 10:
        return True
    return False


string1 = is_long_string("dgfhddddddddj")
print(string1)


def judge(str1, str2):
    longest = longest_string(str1, str2)
    if is_long_string(longest):
        print(str(longest) + " is a long string")
    else:
        print(str(longest) + " is a normal string")


judge("shepherd", "cataclysmic")
judge("horse", "cat")


