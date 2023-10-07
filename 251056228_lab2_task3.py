from socket import *
from base64 import *
import ssl

YOUR_EMAIL = input("Enter your email address: ")
YOUR_PASSWORD = input("Enter your password: ")
YOUR_DESTINATION_EMAIL = input("Enter email destination: ")

msg = "\r\n I love computer networks! this is my task 3 message"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google Mail server) and call it mailserver
mailserver = 'smtp.gmail.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 465))
clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_TLS)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Nikita\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

#Account Authentication
startTLSCommand = "STARTTLS\r\n".encode()
clientSocket.send(startTLSCommand)
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != '220':
    print('220 reply not received from server.')

EMAIL_ADDRESS = b64encode(YOUR_EMAIL.encode())
EMAIL_PASSWORD = b64encode(YOUR_PASSWORD.encode())

authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '334':
    print('334 reply not received from server.')

clientSocket.send(EMAIL_ADDRESS + '\r\n'.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '334':
    print('334 reply not received from server.')

clientSocket.send(EMAIL_PASSWORD + '\r\n'.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
mailFromCommand = "MAIL FROM: <{}>\r\n".format(YOUR_EMAIL)
clientSocket.send(mailFromCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptToCommand = "RCPT TO: <{}>\r\n".format(YOUR_DESTINATION_EMAIL)
clientSocket.send(rcptToCommand.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv8 = clientSocket.recv(1024).decode()
print(recv8)
if recv8[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())


# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9)
if recv9[:3] != '221':
    print('221 reply not received from server.')

clientSocket.close()