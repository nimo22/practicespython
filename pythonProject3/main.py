def double_letters(str):
    for letter in str:
        numb=str.index(letter)
        print(numb)
        print("##################")
        for seconde as row[]:
            toto=str.index(seconde)
            print(toto)
            if toto==numb+1:
                print("ok")
                print(str[numb])
                print(str[toto])
                if str[numb] is str[toto]:
                    return True
    return False


if __name__ == '__main__':
    print(double_letters("hello"))