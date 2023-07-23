import abc

from packets.packet_types import BodyType
from parsers.structures import packet_header_stc


class UdpHeader:
    def __init__(self, unpack):
        self.packet_format = unpack[0]
        self.game_year = unpack[1]
        self.game_major_version = unpack[2]
        self.game_minor_version = unpack[3]
        self.packet_version = unpack[4]
        self.packet_id = unpack[5]
        self.session_uid = unpack[6]
        self.session_time = unpack[7]
        self.frame_id = unpack[8]
        self.overall_frame_id = unpack[9]
        self.player_index = unpack[10]
        self.secondary_player_index = unpack[11]


class UdpBody(abc.ABC):

    @classmethod
    def create(cls, packet_id: int, raw: bytes):
        body_type = BodyType.options.get(packet_id)
        body_stc = body_type.structure
        if getattr(body_type, 'have_sub_stc'):
            return body_type(body_stc(raw).unpack(raw[:body_stc(raw).size]))
        return body_type(body_stc().unpack(raw[:body_stc().size]))


class UdpPacket:

    def __init__(self, *, raw):
        self._raw = raw
        self.header, self.body = self._decode()

    def _decode(self):
        header_parser = packet_header_stc()
        header = UdpHeader(header_parser.unpack(self._raw[:header_parser.size]))
        body = UdpBody.create(header.packet_id, self._raw[header_parser.size:])
        return header, body

    def __str__(self):
        return f'UdpPacket(packed_id -> {self.header.packet_id})'
