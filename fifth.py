class cryp():

    def rmcryp(self):
        a = input("Enter your plain-Text:")
        key = [15 , 0 ,18 , 2 ,0,11]
        cipher = []
        listkistring = ''
        Q = len(a)/6
        q = int(Q+1)
        for y in range(0,q):
          for j in range(0,6):
           key.append(key[j])

        for element in range(0,len(a)):
            b = (ord(a[element])- 65 )
            d = ((key[element]))
            z =(b+d)%26
            y = (chr(z+65))
            cipher.append(y)

        for x in cipher:
            listkistring +=  x

        print(f'Encrypted Cipher-text:{listkistring}')




    def  decryp(self):
        t = input("Enter your cipher-text:")
        key = [15 , 0 ,18 , 2 ,0,11]
        (Q) = len(t) / 6
        q = int(Q + 1)
        for y in range(0, q):
            for j in range(0, 6):
                key.append(key[j])


        for element in range(0, len(t)):
          u = (ord(t[element]) - 97)
          v = u-key[element]
          if(v<0):
            m=v+26
            print(chr((m%26) +97))
          else:
             print(chr((v%26)+97))



print('-------------------------------------------------')
print(">>Welcome to HIGH LEVEL VIGENERE ENCRYPTION<<")

audumber = cryp()
print("Enter your choise \n 1.Encryption  \n 2.Decryption")
print("[Hint = enter your choise in int form]")
f = int(input("Ans:"))
print('-------------------------------------------------')
if(f==1):
    audumber.rmcryp()
elif(f==2):

  audumber.decryp()
else:
    print("Sorry , you have enter invalid choise")
