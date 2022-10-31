
#inheritance code.
class test(object):
    def __init__(self,inp,str):
        self.inp = inp
        self.str = str
class test1(test):
    def fun1(self):
        c  = 0
        # print(self.inp,self.str,self.c)
        for i in self.str:
            if self.inp in i:
                c += 1
                if None:
                    break
        print("count of letters in str",c)
    


val = test1('a','siddartha kowshik garigipati')
print(val.fun1())


    
