from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint


class Cliente(DatagramProtocol):
    def __init__(self, host, port):
        if host == "localhost":
            host = "127.0.0.1"

            self.id = host, port
            self.enders = None
            self.servidor = '127.0.0.1', 9999
            print("Funcionando neste id:", self.id)

    def startProtocol(self):
        self.transport.write("pronto".encode("utf-8"), self.servidor)

    def datagramReceived(self, dat, enderecos):
        dat = dat.decode('utf-8')

        if enderecos == self.servidor:
            print("Escolha um destes clientes\n", dat)
            self.enders = input("Escreva o host:"), int(input("Escreva a porta:"))
            reactor.callInThread(self.send_message)
        else:
            print(enderecos, ":", dat)

    def send_message(self):
        while True:
            self.transport.write(input(":::").encode('utf-8'), self.enders)


if __name__ == '__main__':
    port = randint(1000, 5000)
    reactor.listenUDP(port, Cliente('localhost', port))
    reactor.run()