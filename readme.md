TCP Server
==========

Python sockets example

How to run
----------
On Linux or OS X:

    git clone https://github.com/LioK/tcpserver.git
    cd tcpserver
    sudo chmod +x tcpserver.py
    python tcpserver.py

In the command prompt that appears, enter:
- `start` to start listening for connections
- `echo` to print received messages
- `clean` to clear the data file
- `stop` to exit

To send data to the server:

    echo "Your data goes here" >> data.txt
    nc 127.0.0.1 10000 < data.txt

To check that port 10000 is indeed open:

    nmap 127.0.0.1/32
