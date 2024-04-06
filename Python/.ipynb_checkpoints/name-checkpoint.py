#If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name. __name__ is a built-in variable which evaluates to the name of the current module

print(__name__)