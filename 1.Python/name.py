#If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name. __name__ is a built-in variable which evaluates to the name of the current module
# def main():
#     print("file excected as main program")
# if __name__=="__main__":
#     main()
# else:
#     print("file is being imported")



from demo import add#the movement whenever i import demo file will be exccuted but i dont want that i just want add only
def fun1():
    add()
    print("function1")

def fun2():
    print("function2")

#in a standard way of programming everything in functions
def main():
    fun1()
    fun2()
main()
