_alphabet='abcdefghijklmnopqrstuvwxyz'
_communname=['le',' la','les','je','tu','il']
_message="""
Tmsq ytcx rpmstc jy zmllc ajc, zpytm. Cqr-ac osc a'érygr bgddgagjc ? Amkkclr ytcx tmsq npmacbc (dmpac zpsrc, ylyjwqc dpcosclrgcjjc) ? Cvnjgoscx cl oscjoscq nfpyqcq cr bmllcx jc ambc osc tmsq ytcx srgjgqc à jy oscqrgml qsgtylrc, kygq yrrclrgml ys njyegyr!"""
_communname=['le','la','les','je','tu','il']
possibilite=[]
def transfom(_message):
    _newPhrase=[]
    for x in _message.lower().strip():
        y = _alphabet.find(x)
        _newPhrase.append(y)
    return _newPhrase
if __name__ == '__main__':
    new_ph =transfom(_message)
    for i in range(25,0,-1):
        cop = ""
        for r in new_ph:
            if r!=-1:
             r=r+i
            if r>25:
             r=r-26
            if r==-1:
                cop=cop+" "
            else:

                cop=cop+_alphabet[r]
                ##essaye avec les possibilites
                if i==9 or i==2:
                 print(cop)   ##le 2 est la bonne reponse donc c est le cles est 24
        for p in  _communname:
             if (' ' + p + ' ') in cop:
              possibilite.append(abs(i-26))
              break

    print(possibilite) #17 et 24 donc a droite c est 9 et 2

