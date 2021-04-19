import socketserver
import subprocess
import shlex

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data.decode())
        text = self.data.decode()
        if text[0]=='#':
            print("running premade command")
            if text[1] == "c":
                subprocess.call(
                    ["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"]
                    +shlex.split(text[3:])
                )
        else:
            print(shlex.split(text))
            subprocess.call(shlex.split(text), shell=True)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "192.168.1.77", 3647

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
#



