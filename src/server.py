# This Python will implement a class for handling the server side of the chat
import sys
import socket
import select
import _thread

class server():
    __server_socket = None 
    __client_list = []

    def __init__(self, IP, Port):
        """
        The first argument AF_INET is the address domain of the 
        socket. This is used when we have an Internet Domain with 
        any two hosts The second argument is the type of socket. 
        SOCK_STREAM means that data or characters are read in 
        a continuous flow.
        """
        self.__server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        __ip_address = str(IP)
        __port = int(Port)

        self.__server_socket.bind( (__ip_address, __port))

        self.__server_socket.listen(100)


    def __clien_thread(self, conn, addr):
        """
        for sending message to the client
        """
        conn.send("Chat initiated")
        while True:
            try:
                message = conn.recv(2048)
                if message:
                    """
                    """
                    predicted_message = message #This must be replaced by the predictive function
                    print( "[" + addr[0] + "] predicted message on client:" + predicted_message)
                    
                    #broadcast function sending message to all
                    message_to_send = "[" + addr[0] + "]" + message
                    self.__broadcast(message_to_send, conn)
                else:
                    self.__remove(conn)
            except:
                continue
    
    def __broadcast(self, message, connection):
        """
        Using the below function, we broadcast the message to all 
        clients who's object is not the same as the one sending 
        the message
        """
        for clients in self.__client_list:
            if clients!=connection:
                try:
                    clients.send(message)
                except:
                    clients.close()

                    self.__remove(clients)
    
    def __remove(self, connection):
        """
        just remove the client from the list
        """
        if connection in self.__client_list:
            self.__client_list.remove(connection)

    def run(self):
        """
        Handling maing running function
        """
        conn, addr = self.__server_socket.accept()
        while True:

            conn, addr = self.__server_socket.accept()

            self.__client_list.append(conn)

            print(addr[0] + "connected")

            _thread.start_new_thread(self.__clien_thread, (conn,addr))
        conn.cose()
        self.__server_socket.close()