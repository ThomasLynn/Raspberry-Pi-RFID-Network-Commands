import socketserver
import subprocess
import shlex
import argparse

class CommandTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        
        # convert the recieved data to a regular string
        text = self.data.decode()
        print(text)
        
        # if the string starts with a # then it's a special command
        # this is useful because rfid tags have a character limit of 49 (from my testing)
        if text[0]=='#':
            print("running premade command")
            if text[1] == "c":
                # opens a URL using chrome
                subprocess.call(
                    ["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"]
                    +shlex.split(text[3:])
                )
        else:
            # runs the command given by the client
            print(shlex.split(text))
            subprocess.call(shlex.split(text), shell=True)
            
        # just send back the same data, but upper-cased
        # this is totally not required for the command stuff
        # but I just haven't gotten around to removing it
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", default="127.0.0.1",
        help="The ip the server should be bound to, type ipconfig (or ifconfig) in the command line to get your local ip.")
    parser.add_argument("-port", default="3647", help="The port the server should be bound to.")
    args = parser.parse_args()
    
    HOST, PORT = args.ip, int(args.port)

    # Create the server, binding to localhost on port 3647
    with socketserver.TCPServer((HOST, PORT), CommandTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
#



