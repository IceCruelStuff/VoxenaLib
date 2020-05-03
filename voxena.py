from threading import Thread
import socket


class Voxena(Thread):
    def __init__(self, port, ip):
        if self.ip is not None:
            self.ip = self.ip
        else:
            self.ip = '127.0.0.1'

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

    def getPort(self):
        return self.port

    def getIp(self):
        return  self.ip