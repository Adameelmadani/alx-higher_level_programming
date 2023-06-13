#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    built = dir(hidden_4)
    for i in range(0, len(built)):
        if built[i][0] != '_' or built[i][1] != '_':
            print(built[i])
