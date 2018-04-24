# Ubuntu Tutorial

## Installation from U-disk
modify the bios
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



