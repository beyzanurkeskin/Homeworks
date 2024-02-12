#!/usr/bin/env python
# coding: utf-8

# In[1]:


#beyza nur keskin
#150200320


psw = input()

pw = psw.replace('"', "")






w = ''.join(ch for ch in psw if ch.isupper() or ch.islower() or ch.isdigit())


lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '1234567890'
sp = "!._"


r = 0
x = 0
for i in pw:
    if (i not in lower_case) and (i not in upper_case) and (i not in digits) and (i not in sp):
        r += 1
    elif (i not in lower_case) and (i not in upper_case) and (i not in digits) and (i in sp):
        x += 1
        


s = r + x 



def test(str1):
            
    global a
    a=0

    for el in str1:
        if el*3 in str1:
            a += 1
                    
if x == s:           
    
    if len(pw) >= 6 and len(pw) <= 20 :

        bh = any(x.isupper() for x in pw)
        kh = any(y.islower() for y in pw)
        dg = any(char.isdigit() for char in pw)


        if bh == True and kh == True and dg == True:



            test(psw)

            b = a // 3

            if a == 0:
                print("0")

            elif a >= 1:
                print(b)



        elif bh == True and kh == False and dg == True:

            test(psw)

            if a == 0:

                print(1)


            elif a >= 1:

                print(a//3)

        elif bh == True and kh == False and dg == False:

            test(psw)

            if a == 0:

                print(1)


            elif a >= 1:

                print(a//3)


        elif bh == False and kh == True and dg == True:

            test(psw)

            if a == 0:

                print("1")


            elif a >= 1:

                print(a//3)

        elif bh == False and kh == True and dg == False:

            test(psw)

            if a == 0:

                print("1")


            elif a >= 1:

                print(a//3)

        elif bh == False and kh == False and dg == True:

            test(psw)

            if a == 0:

                print("1")


            elif a >= 1:

                print(a//3)

        elif bh == False and kh == False and dg == False:

            test(psw)

            if a == 0:

                print("2")


            elif a >= 1:

                print(a//3)

        elif bh == True and kh == True and dg == False:

            test(psw)

            if a == 0:

                print("1")


            elif a >= 1:

                print((a//3))





    elif len(pw) < 6:



        bh = any(x.isupper() for x in pw)
        kh = any(y.islower() for y in pw)
        dg = any(char.isdigit() for char in pw)


        if bh == True and kh == True and dg == True:



            test(psw)



            if a == 0:
                print(6-len(pw))

            elif a >= 1:

                print((a//3))




        elif bh == True and kh == False and dg == True:

            test(psw)

            if a == 0:

                print(6-len(pw))


            elif a >= 1:

                print((6-len(pw) +(a//3)))

        elif bh == True and kh == False and dg == False:

            test(psw)

            if a == 0:

                print(6-len(pw))


            elif a >= 1:

                print((6-len(pw) +(a//3)))


        elif bh == False and kh == True and dg == True:

            test(psw)

            if a == 0:

                print(6-len(pw))


            elif a >= 1:

                print((6-len(pw) +(a//3)))

        elif bh == False and kh == True and dg == False:

            test(psw)

            if a == 0:

                print(6-len(pw))


            elif a >= 1:

                print((6-len(pw) +(a//3)))

        elif bh == False and kh == False and dg == True:

            test(psw)

            if a == 0:

                print(6-len(pw))


            elif a >= 1:

                print((6-len(pw) +(a//3)))

        elif bh == False and kh == False and dg == False:

            test(psw)

            if a == 0:

                print(6-len(pw))


            elif a >= 1:

                print((6-len(pw) +(a//3)))

        elif bh == True and kh == True and dg == False:

            test(psw)

            if a == 0:

                print(6-len(pw))


            elif a >= 1:

                print((6-len(pw) +(a//3)))



    elif len(pw) > 20:




        bh = any(x.isupper() for x in pw)
        kh = any(y.islower() for y in pw)
        dg = any(char.isdigit() for char in pw)


        if bh == True and kh == True and dg == True:



            test(psw)

            b = a // 3

            if a == 0:
                print(len(pw)-20)

            elif a >= 1:

                print((len(pw)-20 + (a // 3)))



        elif bh == True and kh == False and dg == True:

            test(psw)

            if a == 0:

                print(len(pw)-20)


            elif a >= 1:

                print((len(pw)-20 + (a // 3)))

        elif bh == True and kh == False and dg == False:

            test(psw)

            if a == 0:

                print(len(pw)-20)


            elif a >= 1:

                print((len(pw)-20 + (a // 3)))


        elif bh == False and kh == True and dg == True:

            test(psw)

            if a == 0:

                print(len(pw)-20)


            elif a >= 1:

                print((len(pw)-20 + (a // 3)))

        elif bh == False and kh == True and dg == False:

            test(psw)

            if a == 0:

                print(len(pw)-20)


            elif a >= 1:

                print((len(pw)-20 + (a // 3)))

        elif bh == False and kh == False and dg == True:

            test(psw)

            if a == 0:

                print(len(pw)-20)


            elif a >= 1:

                print((len(pw)-20 + (a // 3)))

        elif bh == False and kh == False and dg == False:

            test(psw)

            if a == 0:

                print(len(pw)-20)


            elif a >= 1:

                print((len(pw)-20 + (a // 3)))

        elif bh == True and kh == True and dg == False:

            test(psw)

            if a == 0:

                print(len(pw)-20)


            elif a >= 1:

                print((len(pw)-20 + (a // 3)))

else:
    
    if len(pw) >= 6 and len(pw) <= 20 :

        bh = any(x.isupper() for x in pw)
        kh = any(y.islower() for y in pw)
        dg = any(char.isdigit() for char in pw)


        if bh == True and kh == True and dg == True:



            test(w)

            b = a // 3

            if a == 0:
                print(0  )

            elif a >= 1:
                print(b )



        elif bh == True and kh == False and dg == True:

            test(w)

            if a == 0:

                print(1 )


            elif a >= 1:

                print(a//3 )

        elif bh == True and kh == False and dg == False:

            test(w)

            if a == 0:

                print(1 )


            elif a >= 1:

                print(a//3 )


        elif bh == False and kh == True and dg == True:

            test(w)

            if a == 0:

                print(1 )


            elif a >= 1:

                print(a//3 )

        elif bh == False and kh == True and dg == False:

            test(w)

            if a == 0:

                print(1 )


            elif a >= 1:

                print(a//3 )

        elif bh == False and kh == False and dg == True:

            test(w)

            if a == 0:

                print(1 )


            elif a >= 1:

                print(a//3 )

        elif bh == False and kh == False and dg == False:

            test(w)

            if a == 0:

                print(2 )


            elif a >= 1:

                print(a//3 )

        elif bh == True and kh == True and dg == False:

            test(w)

            if a == 0:

                print(1 )


            elif a >= 1:

                print((a//3) )





    elif len(pw) < 6:



        bh = any(x.isupper() for x in pw)
        kh = any(y.islower() for y in pw)
        dg = any(char.isdigit() for char in pw)


        if bh == True and kh == True and dg == True:



            test(w)



            if a == 0:
                print(6-len(pw) )

            elif a >= 1:

                print((a//3) )




        elif bh == True and kh == False and dg == True:

            test(w)

            if a == 0:

                print(6-len(pw) )


            elif a >= 1:

                print((6-len(pw) +(a//3) ))

        elif bh == True and kh == False and dg == False:

            test(w)

            if a == 0:

                print(6-len(pw) )


            elif a >= 1:

                print((6-len(pw) +(a//3) ))


        elif bh == False and kh == True and dg == True:

            test(w)

            if a == 0:

                print(6-len(pw) )


            elif a >= 1:

                print((6-len(pw) +(a//3) ))

        elif bh == False and kh == True and dg == False:

            test(w)

            if a == 0:

                print(6-len(pw) )


            elif a >= 1:

                print((6-len(pw) +(a//3) ))

        elif bh == False and kh == False and dg == True:

            test(w)

            if a == 0:

                print(6-len(pw) )


            elif a >= 1:

                print((6-len(pw) +(a//3) ))

        elif bh == False and kh == False and dg == False:
            
            
            test(w)

            if a == 0:

                print(6-len(pw))


            elif a >= 1:

                print((6-len(pw) +(a//3)))

        elif bh == True and kh == True and dg == False:

            test(w)

            if a == 0:

                print(6-len(pw) )


            elif a >= 1:

                print((6-len(pw) +(a//3) ))



    elif len(pw) > 20:




        bh = any(x.isupper() for x in pw)
        kh = any(y.islower() for y in pw)
        dg = any(char.isdigit() for char in pw)


        if bh == True and kh == True and dg == True:



            test(w)

            b = a // 3

            if a == 0:
                
                print(len(pw)-20 )

            elif a >= 1:

                print((len(pw)-20 + (a // 3) ))



        elif bh == True and kh == False and dg == True:

            test(w)

            if a == 0:

                print(len(pw)-20 )


            elif a >= 1:

                print((len(pw)-20 + (a // 3) ))

        elif bh == True and kh == False and dg == False:

            test(w)

            if a == 0:

                print(len(pw)-20 )


            elif a >= 1:

                print((len(pw)-20 + (a // 3) ))


        elif bh == False and kh == True and dg == True:

            test(w)

            if a == 0:

                print(len(pw)-20 )


            elif a >= 1:

                print((len(pw)-20 + (a // 3) ))

        elif bh == False and kh == True and dg == False:

            test(w)

            if a == 0:

                print(len(pw)-20 )


            elif a >= 1:

                print((len(pw)-20 + (a // 3) ))

        elif bh == False and kh == False and dg == True:

            test(w)

            if a == 0:

                print(len(pw)-20 )


            elif a >= 1:

                print((len(pw)-20 + (a // 3) ))

        elif bh == False and kh == False and dg == False:
            
            
            test(w)
            

            if a == 0:

                print(len(pw)-20 )


            elif a >= 1:

                print((len(pw)-20 + (a // 3) ))

        elif bh == True and kh == True and dg == False:

            
            test(w)

            if a == 0:

                print(len(pw)-20 )


            elif a >= 1:

                print((len(pw)-20 + (a // 3) ))


# In[ ]:




