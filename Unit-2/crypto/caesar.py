
from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    #text = str(text)
    #rot = int(rot)
    return rotate_character(text,rot)

def main():
    text = input('Enter your message here:')
    rot = input('Enter how many rotations here')
    print(encrypt(text,rot))

if __name__ == "__main__":
    main()