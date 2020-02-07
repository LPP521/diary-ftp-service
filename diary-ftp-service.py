import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging
import sys
import re

def get_client_list( list_file_path):
    user_list = []
    line_index = 0
    with open ( list_file_path , "r") as fd:
        for line in fd:
            line_index = line_index + 1
            if not line.__contains__("#"):
                line = line.strip("\n")
                list = line.split(",")
                if len( list ) == 4 :
                    print ("str:", list[2] )
                    if not re.match(  r'^[elradfmwMT]{1,10}$' ,list[2]):
                        print ( "用户权限错误 line_%d,%s" % (line_index,list_file_path))
                        list[2] = "elradfmwM"
                    user_list.append(  list )
                else :
                    print ( "格式错误 line_%d,%s" % (line_index,list_file_path))
    return user_list


def main():
    # 新建一个“授权者”，处理 ftp 登陆过程的鉴权，这个对象被 FTPHandler 使用，
    # 用于鉴别登陆用户的密码，返回登陆用户的目录，检查读写权限等
    authorizer = DummyAuthorizer()
    user_list = get_client_list( sys.path[0] + "/client_list" )
    for user in user_list:
        user_name,password,permit,homedir = user
        if not os.access( homedir , os.F_OK ):
            os.mkdir( homedir )
        authorizer.add_user( user_name,password,homedir,perm=permit ,msg_login="Welcome"+user_name ,msg_quit="Bye"+user_name)    
    authorizer.add_anonymous( "./ftp-anonymous",perm="elradfmwM")

    # FTPHandler,实现 FTP 协议内容，处理来自客户端的命令，所有会话的信息存储在这个实例变量中。 
    handler = FTPHandler
    handler.authorizer = authorizer

    # 连接成功是发送的字符串
    handler.banner = "Welcome to FTP Server"

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

