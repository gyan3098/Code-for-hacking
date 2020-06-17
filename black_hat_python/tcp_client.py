import socket

"""Assumptions made :- 
The first assumption is that our connection will always succeed
the second is that the server is always expecting us to send data first (as opposed to servers that expect to send data to you first and await your response)
third assumption is that the server will always send us data back in a timely fashion"""

target_host = "127.0.0.1"
target_port = 9999

#create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send some data
#client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
client.send("ABCDEF")

# receive some data
response = client.recv(1024)

print response

