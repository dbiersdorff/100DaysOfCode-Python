alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(word, shift_num):

    ret_list = []

    word_list = list(word)

    for char in word_list:
        index = alphabet.index(char.lower())

        index_shifted = (index + shift_num) % 26

        ret_list.append(alphabet[index_shifted])
    
    return str(ret_list)

def decode(word, shift_num):

    ret_list = []

    word_list = list(word)

    for char in word_list:

        index = alphabet.index(char.lower())

        index_shifted = index - shift_num

        ret_list.append(alphabet[index_shifted])
    
    return str(ret_list)

running = True

while running:

    code_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    message = input("Type your message:\n")

    shift_num = int(input("Type the shift number:\n"))

    if code_choice == "encode":
        print(f"Here's the encoded result: {encode(message, shift_num)}")
    elif code_choice == "decode":
        print(f"Here's the encoded result: {decode(message, shift_num)}")
    else:
        running = False


