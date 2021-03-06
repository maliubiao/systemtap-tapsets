#-*-encoding=utf-8-*-
#1.检测阻塞的系统调用
#2.strace观察进程, 同时减少干扰性能
import sys

probe_t = """\
probe syscall.%s {
    if (execname() == "%s") {
        printf("%s: %s\\n", %s);
    }
}\n
"""

args = "argstr" 

syscalls = (
        "accept",
        "accept4", 
        "access",
        "acct",
        "add_key",
        "adjtimex",
        "alarm",
        "bdflush",
        "bind",
        "brk",
        "capget",
        "capset",
        "chdir",
        "chmod",
        "chown",
        "chown16",
        "chroot",
        "clock_getres",
        "clock_gettime",
        "clock_nanosleep",
        "clock_settime",
        "clone",
        "close",
        "connect",
        "creat",
        "delete_module",
        "dup",
        "dup2",
        "dup3",
        "epoll_create",
        "epoll_ctl",
        "epoll_pwait",
        "epoll_wait", 
        "eventfd",
        "execve",
        "exit",
        "exit_group",
        "faccessat",
        "fadvise64",
        "fchdir",
        "fchmod",
        "fchmodat",
        "fchown",
        "fchown16",
        "fchownat",
        "fcntl",
        "fdatasync",
        "fgetxattr",
        "flistxattr",
        "flock",
        "fork",
        "fremovexattr",
        "fsetxattr",
        "fstat",
        "fstatat",
        "fstatfs",
        "fstatfs64",
        "fsync",
        "ftruncate", 
        "futex",
        "futimesat",
        "getcwd",
        "getdents",
        "getegid",
        "geteuid",
        "getgid",
        "getgroups",
        "gethostname",
        "getitimer",
        "get_mempolicy",
        "getpeername",
        "getpgid",
        "getpgrp",
        "getpid",
        "getppid",
        "getpriority", 
        "getresgid",
        "getresuid",
        "getrlimit",
        "getrusage",
        "getsid",
        "getsockname",
        "getsockopt",
        "gettid", 
        "gettimeofday",
        "getuid",
        "getxattr",
        "init_module",
        "inotify_add_watch",
        "inotify_init",
        "inotify_rm_watch",
        "io_cancel",
        "ioctl",
        "io_destroy",
        "io_getevents",
        "ioperm",
        "io_setup",
        "io_submit",
        "ioprio_get",
        "ioprio_set",
        "kexec_load",
        "keyctl",
        "kill",
        "lchown",
        "lchown16", 
        "lgetxattr",
        "link",
        "linkat",
        "listen",
        "listxattr",
        "llistxattr",
        "llseek",
        "lookup_dcookie",
        "lremovexattr",
        "lseek",
        "lsetxattr",
        "lstat",
        "madvise",
        "mbind",
        "migrate_pages",
        "mincore",
        "mkdir",
        "mkdirat",
        "mknod",
        "mknodat",
        "mlock",
        "mlockall",
        "modify_ldt",
        "move_pages",
        "mount",
        "mmap2",
        "mprotect",
        "mq_getsetattr",
        "mq_notify",
        "mq_open",
        "mq_timedreceive",
        "mq_timedsend",
        "mq_unlink",
        "mremap",
        "msgctl",
        "msgget",
        "msgrcv",
        "msgsnd",
        "msync",
        "munlock",
        "munmap",
        "nanosleep",
        "nice",
        "ni_syscall",
        "open",
        "openat",
        "pause",
        "personality", 
        "pipe",
        "pivot_root",
        "poll",
        "ppoll",
        "prctl",
        "pread",
        "preadv",
        "pselect6", 
        "ptrace",
        "pwrite", 
        "pwritev",
        "quotactl",
        "read",
        "readahead",
        "readdir",
        "readlink",
        "readlinkat",
        "readv",
        "reboot",
        "recv",
        "recvfrom",
        "recvmsg",
        "remap_file_pages",
        "removexattr",
        "rename",
        "renameat",
        "request_key",
        "restart_syscall",
        "rmdir",
        "rt_sigaction",
        "rt_sigaction32",
        "rt_sigpending",
        "rt_sigprocmask",
        "rt_sigqueueinfo",
        "rt_sigreturn",
        "rt_sigsuspend",
        "rt_sigtimedwait",
        "sched_getaffinity",
        "sched_getparam",
        "sched_get_priority_max",
        "sched_get_priority_min",
        "sched_getscheduler",
        "sched_rr_get_interval",
        "sched_setaffinity",
        "sched_setparam",
        "sched_setscheduler",
        "sched_yield",
        "select",
        "semctl",
        "semget",
        "semop",
        "semtimedop",
        "send",
        "sendfile",
        "sendmsg",
        "sendto",
        "setdomainname",
        "setfsgid",
        "setgid",
        "setgroups",
        "sethostname",
        "setitimer",
        "set_mempolicy",
        "setpgid",
        "setpriority",
        "setregid",
        "setregid16",
        "setresgid",
        "setresgid16",
        "setresuid",
        "setresuid16",
        "setreuid",
        "setreuid16",
        "setrlimit",
        "setsid",
        "setsockopt",
        "set_tid_address",
        "settimeofday",
        "settimeofday32",
        "setuid",
        "setxattr",
        "sgetmask",
        "shmat",
        "shmctl",
        "shmdt",
        "shmget",
        "shutdown",
        #"sigaction",
        "sigaction32",
        "signal",
        "signalfd",
        "sigpending",
        "sigprocmask",
        "sigreturn",
        "sigsuspend",
        "socket",
        "socketpair",
        "splice",
        "ssetmask",
        "stat",
        "statfs",
        "statfs64",
        "stime",
        "swapoff",
        "swapon",
        "symlink",
        "symlinkat",
        "sync",
        "sysctl",
        "sysfs",
        "sysinfo",
        "syslog",
        "tee",
        "tgkill",
        "time",
        "timer_create",
        "timer_delete",
        "timer_getoverrun",
        "timer_gettime",
        "timer_settime",
        #"timerfd",
        "times",
        "tkill",
        "truncate",
        #"tux",
        "umask",
        "umount",
        "uname",
        "unlink",
        "unlinkat",
        "unshare",
        "uselib",
        "ustat",
        "ustat32",
        "utime",
        "utimes",
        "utimensat",
        "vfork",
        "vhangup",
        "vmsplice",
        "wait4",
        "waitid",
        "write",
        "writev" 
    ) 
if __name__ == "__main__":
    target = sys.argv[1]
    for k in syscalls:
        print probe_t % (k, target, k, "%s", "argstr")
