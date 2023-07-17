from dataclasses import dataclass
from parsers.structures import motion_stc


@dataclass
class MotionPacket:
    structure = motion_stc

    def __init__(self, unpack):
        self.position_x: float = unpack[0]
        self.position_y: float = unpack[1]
        self.position_z: float = unpack[2]
        self.velocity_x: float = unpack[3]
        self.velocity_y: float = unpack[4]
        self.velocity_z: float = unpack[5]
        self.forward_dir_x: int = unpack[6]
        self.forward_dir_y: int = unpack[7]
        self.forward_dir_z: int = unpack[8]
        self.right_dir_x: int = unpack[9]
        self.right_dir_y: int = unpack[10]
        self.right_dir_z: int = unpack[11]
        self.g_lateral_force: float = unpack[12]
        self.g_longitudinal_force: float = unpack[13]
        self.g_vertical_force: float = unpack[14]
        self.yaw: float = unpack[15]
        self.pitch: float = unpack[16]
        self.roll: float = unpack[17]

@dataclass
class BodyType:
    options = {
        0: MotionPacket,
    }
