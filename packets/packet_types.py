from dataclasses import dataclass
from parsers.structures import (
    motion_stc,
    lap_data_stc
)


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
class LapData:
    structure = lap_data_stc

    def __init__(self, unpack):
        self.last_lap_ms = unpack[0]
        self.current_lap_ms = unpack[1]
        self.first_sector_ms = unpack[2]
        self.first_sector_min = unpack[3]
        self.second_sector_ms = unpack[4]
        self.second_sector_min = unpack[5]
        self.delta_to_car_in_front_ms = unpack[6]
        self.delta_to_leader_in_front_ms = unpack[7]
        self.lap_distance_in_meters = unpack[8]
        self.total_distance = unpack[9]
        self.safety_car_delta = unpack[10]
        self.car_position = unpack[11]
        self.current_lap = unpack[12]
        self.pit_status = unpack[13]
        self.num_pit_stops = unpack[14]
        self.sector = unpack[15]
        self.current_lap_invalid = unpack[16]
        self.penalties = unpack[17]
        self.total_warnings = unpack[18]
        self.corner_cutting_warnings = unpack[19]
        self.num_un_served_drive_through_pens = unpack[20]
        self.num_un_server_stop_and_go_pens = unpack[21]
        self.grid_pos = unpack[22]
        self.driver_status = unpack[23]
        self.result_status = unpack[24]
        self.pit_lane_timer_status = unpack[25]
        self.pit_lane_time_in_lane_ms = unpack[26]
        self.pit_stop_ms = unpack[27]
        self.pit_stop_should_serve_pen = unpack[28]
        self.time_trial_pb_car_index = unpack[29]
        self.time_trial_rival_car_index = unpack[30]


@dataclass
class BodyType:
    options = {
        0: MotionPacket,
        1: ...,
        2: LapData
    }
