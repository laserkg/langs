# Ubuntu Tutorial

## Installation from U-disk
modify the BIOS
RAID0 -> ACHI

## Install Sogo PinYin
[Ubuntu 16.04安装sogou 拼音输入法](https://blog.csdn.net/ljheee/article/details/52966456)
[ubuntu搜狗输入法切换快捷键fcitx设置](https://blog.csdn.net/win_turn/article/details/53637293)

#### Terminal不能Ctrl V和 Ctrl C
在terminal里，linux-term，自己定义了ctrl+c ;  ctrl+v  的意义。
分别是：^C,  和 ^V的功能。   另外， ctrl+v + m  => ^M ( 如果加n就是 ^N）

拷贝: ctrl + Insert
粘贴: shift + Insert
当然直接点击鼠标中键可以复制，并粘贴, 这两个命令不只是作用在terminal里，还可以作用在Ｕｂｕｎｔｕ的其他ｇｕｉ上。


不同于Windows，Linux系统里存在两个剪切板：一个叫做选择缓冲区(X11 selection buffer)，另一个才是剪切板(clipboard)。

选择缓冲区是实时的，当使用鼠标或键盘选择内容时，内容已经存在于选择缓冲区了，这或许就是选择缓冲区的由来吧。

使用下面的命令查看选择缓冲区的内容：:
```
$ xclip -out
```

#### gnome-terminal 如何设定鼠标选择即复制
本来就是如此，不必设置，只是粘贴不是ctr + v而是shift + insert.


## [免sudo使用docker命令](https://www.jianshu.com/p/95e397570896)
1. 添加用户到docker组
```
$ sudo usermod -aG docker zhishan
```
切换当前会话到新 group 或者重启 X 会话
```
$ newgrp - docker

```

2. 并修改`/lib/systemd/system.service`配置文件，增加`User=docker`，以下是`colord`进程的配置文件
```
[Unit]
Description=Manage, Install and Generate Color Profiles

[Service]
Type=dbus
BusName=org.freedesktop.ColorManager
ExecStart=/usr/lib/colord/colord
User=colord
# We think that udev's AF_NETLINK messages are being filtered when
# network namespacing is on.
# PrivateNetwork=yes
PrivateTmp=yes

```
进程管理中显示：
```
$ ps -ef | grep colord
colord    1313     1  0 17:56 ?        00:00:00 /usr/lib/colord/colord

$ sudo systemctl enable docker.service
Synchronizing state of docker.service with SysV init with /lib/systemd/systemd-sysv-install...
Executing /lib/systemd/systemd-sysv-install enable docker


$ sudo service docker start
Warning: docker.service changed on disk. Run 'systemctl daemon-reload' to reload units.
Job for docker.service failed because the control process exited with error code. See "systemctl status docker.service" and "journalctl -xe" for details.
```

#### How to start and stop a service?
 service --status-all

### [systemctl 命令完全指南](https://www.linuxidc.com/Linux/2015-07/120833.htm)
### [linux中service与chkconfig的替代者systemctl](https://blog.csdn.net/hshl1214/article/details/45566957)

### [以非root账号启动docker](https://www.jianshu.com/p/95e397570896)
```
$ docker ps
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.26/containers/json: dial unix /var/run/docker.sock: connect: permission denied
$ cd /var/run
$ ls -l |grep docker.
srw-rw----  1 root  docker    0 5月   8 06:05 docker.sock
```
可以看到其属主为root，权限为rw，可读可写；其属组为docker，权限为rw，可读可写。如果要当前用户可直接读取该文件，那么我们就为当前用户添加到docker属组即可。

####

* 删除用户组 groupdel yourgrp


$ sudo apt install openjdk-9-jdk
[sudo] password for zhishan: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following package was automatically installed and is no longer required:
  snap-confine
Use 'sudo apt autoremove' to remove it.
The following additional packages will be installed:


## 设置快速打开Terminal的快捷键
Ctrl+Alt+T，快捷键搞定: 这是启动新的窗口


