alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
def encrypt(msg, s):
    codemsg = []
    x = [i for i in msg]
    for i in range(0, len(x)):
        if x[i] in alphabet:
            index = alphabet.index(x[i])
            position = index + s
            if position > len(alphabet):
                if position <= len(alphabet) - 1:
                    codemsg.append(alphabet[position])
            elif position > len(alphabet):
                codemsg.append(alphabet[position - len(alphabet) - 1])
    for i in range(len(codemsg)):
        print(codemsg[i], end='')


# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
# message = input("Type your message,\n: ").lower()
# shift = int(input("Type the shift number: "))

# print(len(alphabet))
# if direction == 'encode':

message = 'There are various situations we might encounter when a list is given and we convert it to string. For example, conversion to string from the list of string or the list of integer.'
encrypt(message, 54)
