def get_initials(fullname):
    name_list = fullname.split()
    init = ""
    for name in name_list:
        init = init + name[0]
    upperinit = init.upper()
    return upperinit

def main():
    input("What is your first and last name?")
    print(upperinit)

if __name__ == '__main__':
    main()