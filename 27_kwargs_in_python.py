# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):    # You can give anything name you want but important thing is '**' double asterisk
    # print("Hello "+kwargs['first']+" "+kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Mr.", first="Shoaib", middle="Shaikh", last="Dude")