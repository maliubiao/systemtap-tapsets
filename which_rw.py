import sys 

def read_log(log):
    read = {}
    write = {}
    f = open(log, "r")
    for x in f.readlines()[1:]: 
        modeinfo, countinfo = x.split("`")
        mode, name = modeinfo.split("'")
        fd, count = countinfo.split("-")
        count = int(count) 
        if mode == "r":
            if name in read:
                read[name] += count
            else:
                read[name] = count
        else: 
            if name in write:
                write[name] += count
            else:
                write[name] = count
    f.close() 
    return read, write 

def main():
    read, write = read_log(sys.argv[1]) 
    print sorted(read.items(), key=lambda x: x[1])
    print sorted(write.items(), key=lambda x: x[1])

if __name__ == "__main__":
    main()
