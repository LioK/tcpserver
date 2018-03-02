import socket
import sys
import os
import time
from cmd import Cmd


class server(Cmd):
    '''Simple TCP server class'''
    prompt = '> '

    def do_start(self, args):
        '''Listen for connections'''
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', 10000)
        print >>sys.stderr, 'starting up on %s port %s' % server_address
        sock.bind(server_address)

        # Listen for incoming connections
        sock.listen(1)

        print >>sys.stderr, 'Waiting for a connection'
        connection, client_address = sock.accept()

        try:
            print >>sys.stderr, 'Connection from', client_address

            # Receive the data in small chunks and append to a file
            while True:
                data = connection.recv(16)
                print >>sys.stderr, 'Received "%s"' % data
                if data:
                    print >>sys.stderr, 'Writing data received from the client'
                    file = open("tcpserverdata.file", "a", 1)
                    file.write(data)
                else:
                    print >>sys.stderr, 'No more data from', client_address
                    file.close()
                    break
        finally:
            connection.close()

    def do_stop(self, args):
        '''Exit'''
        print "Bye bye"
        raise SystemExit()

    def do_time(self, args):
        '''Display current time'''
        print time.strftime("%H:%M:%S")

    def do_echo(self, args):
        '''Echo the last data received'''
        lastfile = open("tcpserverdata.file", "r", 1)
        contents = lastfile.read()
        print contents
        lastfile.close()

    def do_clean(self, args):
    	'''Erase data from tcpserverdata.file'''
    	file = open("tcpserverdata.file", "w", 1)
    	file.write("")
    	file.close()
    	print "Deleted all previously received data"


if __name__ == "__main__":
    app = server()
    app.cmdloop('Enter a command to do something (start/echo/time/stop/clean)')
