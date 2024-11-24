import scapy.all as scapy
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Main function
def main():
    while True:
        print("\nChoose an action:")
        print("1. Send a packet")
        print("2. Receive a packet")
        print("3. Analyze packet")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Get destination IP and port
            dest_ip = input("Enter destination IP: ")
            dest_port = int(input("Enter destination port: "))

            # Send a packet
            payload = input("Enter payload: ")
            packet = scapy.IP(dst=dest_ip) / scapy.TCP(dport=dest_port, flags='S', payload=payload)
            scapy.send(packet)

        elif choice == '2':
            # Receive a packet
            packet = scapy.sniff(count=1, prn=lambda x: print(x.show()))
            print(packet.show())

        elif choice == '3':
            # Analyze packet
            packet = scapy.sniff(count=1, prn=lambda x: print(x.show()))
            analyze_packet(packet)

        elif choice == '4':
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()