
from twisted.internet import protocol, reactor


class Twist(protocol.Protocol):

    def connectionMade(self):
        print 'connection success!'


    def dataReceived(self, data):
        print data

        self.transport.write('Hello from server!')


    def connectionLost(self, reason):
        print 'Connection lost!'


factory = protocol.Factory()
factory.protocol = Twist
print 'wait...'
reactor.listenTCP(5555, factory)
reactor.run()
