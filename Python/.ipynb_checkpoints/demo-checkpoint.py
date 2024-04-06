
# import name
# print("in demo",__name__)


def add():
    print("adeed")
def sub():
    print("subb")
def main():
    add()
    sub()

if __name__=="__main__":#i want to exceute entire file only if it is excecuted as standalone file otherwise wont
        main()