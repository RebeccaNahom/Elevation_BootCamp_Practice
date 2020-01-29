## spot check 1
# def add(x, y):
#    sum = x + y
#     if sum >= 100:
#         print('whoa')
#     else:
#         print("do better")
#
# add (2,7)
# add(4,99)

# # spot check 2

# def remove_letter_from_text(text, letter):
#     return str(filter(lambda c: c != letter, text))
#
# def encode_text(text):
#     return "-".join(map(lambda c: str(ord(c)), text))
#
# def show_encoded_filter(string, letter):
#     text = remove_letter_from_text(string, letter)
#     print("updated text into: " + text)
#     encoded_text =  encode_text(text)
#     print(f'encrypted text is: {encoded_text}')
#
#
# show_encoded_filter("sinusitis", "s")

# #spot check 3
#
# def determine_biggest(int1, int2):
#     if(int1 > int2):
#         return int1
#     return int2
#
# biggest = determine_biggest(1, 2)
# print("Biggest number is " + str(biggest))
