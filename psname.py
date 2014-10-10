
if __name__ == "__main__":
    import os
    for comm, cmdline in [("/proc/%s/comm" % i, "/proc/%s/cmdline" % i) for i in os.listdir("/proc") if i[0].isdigit()]:
        print "================================"
        print open(comm, "r").read().strip("\n")
        print open(cmdline, "r").read().strip("\n").replace("\x00", " ")
