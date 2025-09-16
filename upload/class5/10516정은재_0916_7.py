class console:
        def log(msg:str):
            print(msg)

        def log(num:int):
            print(num)



class calu:


    def plus():
        a = int(input('첫번째숫자 입력:'))
        b = int(input('두번째 숫자 입력:'))
        console.log(str(a) + " + " + str(b) + " = " + str(a+b))
    def minus():
        a = int(input('첫번째숫자 입력:'))
        b = int(input('두번째 숫자 입력:'))
        console.log(str(a) + " - " + str(b) + " = " + str(a-b))


        
