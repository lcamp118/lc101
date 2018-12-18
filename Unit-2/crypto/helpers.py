def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upperalphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbolsandnumbers = ''' !?@-#$%^&*()<>~[]\/.,;:'"1234567890'''
    if letter in symbolsandnumbers:
        return letter
    if letter in upperalphabet:
        result = upperalphabet.index(letter)
    elif letter in alphabet:
        result = alphabet.index(letter)
    return result

def rotate_character(text,rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upperalphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbolsandnumbers = ''' !?@-#$%^&*()<>~[]\/.,;:'"1234567890'''
    encrypted = ''
    for char in text:
        if char in symbolsandnumbers:
                encrypted = encrypted + char
        else:
            new_index = alphabet_position(char) + rot
            if new_index < 26:
                if char in alphabet:
                    encrypted = encrypted + alphabet[new_index]
                else:
                    new_char = upperalphabet[new_index]
                    encrypted = encrypted + new_char
            else:
                if char in alphabet:
                    new_char = alphabet[new_index % 26]
                    encrypted = encrypted + new_char
                else:
                    new_char = upperalphabet[new_index % 26]
                    encrypted = encrypted + new_char
    return encrypted