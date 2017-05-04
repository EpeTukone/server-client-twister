from twisted.internet import protocol, reactor

host = 'localhost'
port = 5555


class Twist_client(protocol.Protocol):
    def sendData(self):
        data = raw_input('write message: ')
        if data:
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()


class Twist_Factory(protocol.ClientFactory):
    protocol = Twist_client

    def clientConnectionFailed(self, connector, reason):
        print 'connection failed:', reason.getErrorMessage()
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print 'connection lost:', reason.getErrorMessage()
        reactor.stop()


factory = Twist_Factory()
reactor.connectTCP(host, port, factory)
reactor.run()