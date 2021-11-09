def strxor(s1, s2):
  return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

if __name__ == '__main__':

 print(0xa7040f958efd92b05931edb36a7fb0599^0x850bd08c3405467f1ab4bcf0ca8c7d3d)