import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging

def main():
    # 新建一个“授权者”，处理 ftp 登陆过程的鉴权，这个对象被 FTPHandler 使用，
    # 用于鉴别登陆用户的密码，返回登陆用户的目录，检查读写权限等
    authorizer = DummyAuthorizer()
    authorizer.add_user("user","123","./ftp-user",perm="elradfmwM")
    authorizer.add_anonymous( "./ftp-anonymous",perm="elradfmwM")
    # 可以如下设置：
    # authorizer.add_user(username,password,homedir,perm="elr",mas_login="Login successful",msg_quit="Goodbye")
    
    # FTPHandler,实现 FTP 协议内容，处理来自客户端的命令，所有会话的信息存储在这个实例变量中。 
    handler = FTPHandler
    handler.authorizer = authorizer

    # logging.basicConfig(level=logging.DEBUG)

    # 连接成功是发送的字符串
    handler.banner = "ftpd OK"

    address = ('',21)
    server = FTPServer(address,handler)

    # 最大连接数
    server.max_cons = 5
    # 同一ip的连接数
    server.max_cons_per_ip = 5

    # 启动异步IO循环
    #server.serve_forever( timeout=None,blocking=True,handle_exit=True)
    server.serve_forever()


if __name__ == "__main__":
    main()

