from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from generate_reply import generateReply

# Simple WebSocket for single-user chat bot
class ChatServer(WebSocket):

    def handleMessage(self):
        # echo message back to client
        message = self.data;
        self.sendMessage(generateReply(message))

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


#print(generateReply("I am not cool."))
server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()