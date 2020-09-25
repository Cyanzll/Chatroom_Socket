# UDP面向无连接，所以没有真正的客户端，这个server端是为了实现聊天室消息广播的功能
import socket
import threading
import sys

HOST = socket.gethostname()
PORT = 9999
ADDRESS = (HOST, PORT)
addr_list = []

print(socket.gethostbyname_ex(socket.gethostname()))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDRESS)

print("服务端开始工作，请连接 %s:%d \n" % (HOST,PORT))

while True:
    data, address = s.recvfrom(1024)
    print("%s发送了一条数据：\n%s" % (address, data.decode('utf-8')))
    if(address not in addr_list):
        addr_list.append(address)
    # 广播
    for each_addr in addr_list:
        s.sendto(data, each_addr)

s.close()