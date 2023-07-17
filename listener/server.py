import datetime
import socket
import uuid

from logger.models import Packet

from packets.base import UdpPacket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 20777))
print('############### SERVER STARTED ###############')
while True:
    message, address = server_socket.recvfrom(10240)
    telemetry = UdpPacket(raw=message)
    if message:
        Packet.insert(
            id=str(uuid.uuid4()),
            payload=bytes.hex(message),
            packet_id=telemetry.header.packet_id,
            timestamp=datetime.datetime.now().timestamp()
        ).execute()
