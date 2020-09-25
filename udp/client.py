import socket
import threading
import time

# 目标地址
HOST = socket.gethostname()
PORT = 9999
ADDRESS = (HOST, PORT)

# 本机地址，用于 bind()
myhost = "192.168.1.100"
myport = int(input("请输入一个端口号，比如3000，然后回车\n> "))

# 配置
username = input("请输入你的昵称\n> ")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 线程
class sendThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        msg = input("\n")
        localtime = time.asctime( time.localtime(time.time()) )
        msg = f"{username} 在 {localtime}\n{msg}\n"
        s.sendto(msg.encode('utf-8'), ADDRESS)

print("客户端开始工作，请在下方输入消息并回车\n")
greet = "%s进入了聊天室(●'◡'●)\n" % (username)
s.sendto(greet.encode('utf-8'), ADDRESS)

while True:
    data, address = s.recvfrom(1024)
    print(data.decode('utf-8'))
    t1 = sendThread(1, "t1", 1)
    t1.start()
    
s.close()
