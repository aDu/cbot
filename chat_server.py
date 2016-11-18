from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class ChatServer(WebSocket):

    def handleMessage(self):
        # echo message back to client
        message = self.data;
        self.sendMessage(message.upper())

    def handleConnected(self):
        print self.address, 'connected'

    def handleClose(self):
        print self.address, 'closed'

server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()