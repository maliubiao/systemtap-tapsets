#-*-encoding=utf-8-*-
#确定调用某个syscall时的uid
#比如create失败,进程chown到了另外一个用户?
import sys
template = """\
probe syscall.{syscall} {{
    if (execname() == "{app}") {{
        printf("{app} uid:%d gid:%d %s\\n", uid() , gid(), argstr);
    }}
}}
"""

print template.format(**{"syscall": sys.argv[2], "app": sys.argv[1]})

"""
output sample:
python uid:1000 gid:100 "/usr/lib/python27.zip/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/lib64/python2.7/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/lib64/python2.7/plat-linux2/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/lib64/python2.7/lib-tk/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/lib64/python2.7/lib-old/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/lib64/python2.7/lib-dynload/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/lib64/python2.7/site-packages/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/lib64/python2.7/site-packages/PIL/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/local/lib64/python2.7/site-packages/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/local/lib/python2.7/site-packages/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/lib64/python2.7/site-packages/gtk-2.0/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/lib/python2.7/site-packages/<stdin>", O_RDONLY
python uid:1000 gid:100 "/usr/lib64/python2.7/site-packages/wx-2.8-gtk2-unicode/<stdin>", O_RDONL
