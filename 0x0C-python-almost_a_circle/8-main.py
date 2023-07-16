#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    try:                                                                        
        r1.update("i", 38, 3, "i")                                                   
        print(r1)                                                               
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    try:
        r1.update(height="h")
        print(r1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)
