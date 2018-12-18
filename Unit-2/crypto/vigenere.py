from helpers import alphabet_position, rotate_character
def encrypt(text,cipher):
    symbolsandnumbers = ''' !?-@#$%^&*()<>~[]\/.,;:'"1234567890'''
    message = ''
    index = 0
    for char in text:
        if index > len(cipher) - 1:
            index = 0
        if char in symbolsandnumbers:
           message += char
        else:
            message += rotate_character(char,alphabet_position(cipher[index]))
            index += 1
    return message

def main():
    text = input('Enter your message here:')
    rot = input('Enter your encryption key here (Letters only):')
    print(encrypt(text,cipher))

if __name__ == "__main__":
    main()