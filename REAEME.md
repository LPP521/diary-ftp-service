#  xlsx 日志 FTP 服务器
为了实现 xlsx 日志自动提交，通过 Python3 和 pyftpdlib 实现 FTP 服务器。当 FTP Client （ diary ）满足某种条件时，自动将其生成的数据（*.xlsx）文件推送到服务器。

另一方面，其他远程终端可以通过 IE 浏览器，以 ftp 协议访问本服务器查看和复制保存在本服务器中的文件。

## 依赖
* Python3
* pyftpdlib 通过 pip 安装

## 使用
在当前路径下建立以下目录：\
* ftp-anonymous/    
* ftp-user/  

两个目录，分别用于接受匿名用户和授权用户操作。并为目录提供全面的读写权限，
```sh 
$ chmod 777 <your_ftp-dir> 
```

## FTP 访问

###  Linux 本地测试
在 Ubuntu 环境下，本地新开终端启动 Python3 ,如下脚本测试登陆本地服务器

```sh
>>> from ftplib import FTP
>>> ftp = FTP("192.168.1.105")
>>> ftp.login()
'230 Login successful.'
>>> ftp.dir()
-rw-rw-r--   1 dd       dd            557 Feb 05 06:50 REAEME.md
-rw-rw-r--   1 dd       dd           1303 Feb 05 06:50 diary-ftp-service.py
drwxrwxr-x   4 dd       dd           4096 Feb 05 04:29 ftp-dir
>>> 
```

### Windows 环境登陆服务器
**特别重要**
> Windows Edge 目前不支持 LAN 条件下的 FTP 协议，只能通过 IE 访问 LAN 内的 FTP 服务器

1. 确认本地 IP (192.168.xxx.xxx ) 后，启动服务器
2. LAN 内客户机启动 IE，浏览器路径指向 FTP 服务器，如下：
` ftp://192.168.xxx.xxx `
即可通过匿名方式登陆到 FTP 服务器。 
3. 浏览器即可查看当前用户的 homedir 路径，目前测试的几种文件，
    * txt 文件可以直接在浏览器中查看；
    * xlsx 文件打开时，需要输入用户名和密码；