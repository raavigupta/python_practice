if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)
    
    
raw_input(prompt=None)
raw_input([prompt]) -> string

Read a string from standard input. The trailing newline is stripped. 
If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError. On Unix, 
GNU readline is used if enabled. The prompt string, if given, is printed without a trailing newline before reading
