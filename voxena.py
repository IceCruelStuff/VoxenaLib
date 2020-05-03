from threading import Thread
import socket


class Voxena(Thread):
    def __init__(self, port, ip):
        if ip is not None:
            ip = ip
        else:
            ip = '127.0.0.1'

    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)

    def stop(self):
        self.sock.close()

    def generateChuncks(self, id):
        pass

    def getChunks(self, id):
        pass

    def updateChunks(self):
        pass

    def ping(self):
        pass