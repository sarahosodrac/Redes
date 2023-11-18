from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Servidor(DatagramProtocol):
    def __init__(self):
        self.cliente = set()

    def datagramReceived(self, dat, endereco):
        dat = dat.decode("utf-8")
        if dat == "pronto":
            enders = "\n".join([str(x) for x in self.cliente])

            self.transport.write(enders.encode('utf-8'), endereco)
            self.cliente.add(endereco)


if __name__ == '__main__':
    reactor.listenUDP(9999, Servidor())
    reactor.run()