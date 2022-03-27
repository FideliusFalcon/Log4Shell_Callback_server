import socket
import logging
from time import sleep

class callback_server():
    def __init__(self, server_ip=None, server_port=None):
        print("Server is starting")
        self.server_ip = server_ip
        self.server_port = server_port
        self.server = socket.socket()
        self.server.bind((self.server_ip, self.server_port))
        self.server.listen()


    def start(self):
        print("Waiting for connection")
        while True:
            connection, ip_address = self.server.accept()
            data = self.callback(connection)
            logging.info(f"New connection - {ip_address} - {data}")
            print(ip_address, data)
            connection.close()

    def callback(self, connection):
        data = connection.recv(300)
        if data:
            return str(data)
        else:
            pass
    
    def close_server(self):
        self.server.shutdown(socket.SHUT_RDWR)
        self.server.close()
        print("Socket is closed")

if __name__ == "__main__:"
    while True:
        try:
            logging.basicConfig(level=logging.INFO, filename="catcher.log", format='%(asctime)s - %(message)s')
            cbserver = callback_server(server_ip = "0.0.0.0", server_port = 5000)
            cbserver.start()

        except KeyboardInterrupt:
            try: 
                cbserver.close_server
            except:
                pass
            finally:
                exit()

        except Exception as e:
            try:
                print(f"Error {e}")
                cbserver.close_server()
            except Exception as es:
                print(f"Error {es}")
            finally:
                sleep(3)
