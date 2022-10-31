

def hello(fun):
    def inner():
        print("decornators one")
        fun() # parent class funnction is called

    return inner
def world():
    print("decorators two")

# @decorators
hello  = hello(world)
hello()
# decorator is func in  which it can change the behaviour of a func or class  without modifying the functionality permantely.




