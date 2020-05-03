import socket


class Voxena:
    def start(self, port, ip):
        if ip:
            ip = ip
        else:
            ip = '127.0.0.1'
