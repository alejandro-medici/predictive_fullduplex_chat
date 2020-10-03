# This Python will implement a class for handling the cliend side of the chat
import sys
import socket
import select

class client():
    __server_socket = None 

    def __init__(self, IP, Port):
        """
        The first argument AF_INET is the address domain of the 
        socket. This is used when we have an Internet Domain with 
        any two hosts The second argument is the type of socket. 
        SOCK_STREAM means that data or characters are read in 
        a continuous flow.
        """
        _ip_address = str(IP)
        _port = int(Port)
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket.connect( (_ip_address, _port))
    
    def run(self):
        """
        Handling maing running function
        """
        server = self.__server_socket
        while True:
            sockets_list = [server]

            read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])

            for socks in read_sockets:
                if socks == server:
                    message = socks.recv(2048)
                    predicted_message = message #This must be replaced by the predictive function
                    print(predicted_message)
                else:
                    message = sys.stdin.readline()
                    reduced_message = message
                    server.send(reduced_message)
                    sys.stdout.write("<User>")
                    sys.stdout.write(message)
                    sys.stdout.flush()
         
        self.__server_socket.close()