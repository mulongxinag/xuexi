# 2手写一个偏底层的简单web框架
# 套接字 socket：（插座）。我们已经在谷歌浏览器开发者工具中看到了   http协议的请求和响应。但我们并没有自己去实现tcp报文、IP协议网络传输这些底层细节。这些底层复杂我们不必从头造轮子。
# socket 将 ip地址、端口号、TCP封装了起来，通过socket，我们可以像读本地文件一样方便的进行网络请求和响应。
# socket web框架、QQ通信软件、LOL游戏 等通信传输基础。

import socket

HOST, PORT ='127.0.0.1', 8000

# 开启一个监听的套接字对象。  等待消息到达
listen_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
# 套接字对象 绑定 网络地址
listen_socket.bind((HOST,PORT))
listen_socket.listen(1)
print('http服务监听在  http://{}:{}' .format(HOST,PORT))

# 返回客户端的内容
while True:
    # 获取客户端的请求对象和请求网络地址
    client_connection,client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)

    http_response = b"""
    HTTP/1.1 200 OK\r\n
    
    """

"""
理解127.0.0.1
客户端和服务器
生产环境：客户端是我们的浏览器，服务端是远程服务器，例如淘宝的服务器是阿里云，形如45.46.221.10：80
开发环境：由于我们没有服务器，所以我们的服务代码还跑在我们的个人电脑上。个人电脑既是服务器，又是客户端，只是端口不同。127.0.01:8000  是后台运行的一个服务器程序，谷歌浏览器是客户端负责请求和展示服务器返回的数据。

socket包：封装好底层的ip tcp协议需要手动拼接。

"""
# 作业：基于socket简单局域网聊天室。