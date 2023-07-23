from dataclasses import dataclass
from parsers.structures import (
    motion_stc,
    lap_data_stc,
    car_status_stc,
    tyre_set_stc,
    car_telemetry_stc,
    motion_ex_stc,
    car_damage_stc,
    car_setup_stc,
    participants_stc, participant_arr
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
class Session:
    structure = car_telemetry_stc


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
class Events:
    structure = car_telemetry_stc


@dataclass
class Participants:
    structure = participants_stc
    have_sub_stc = True

    class Participant:
        def __init__(self, *args):
            self.ai_controlled = args[0]
            self.driver_id = args[1]
            self.network_id = args[2]
            self.team_id = args[3]
            self.my_team = args[4]
            self.race_number = args[5]
            self.nationality = args[6]
            self.name = args[7].decode('utf-8').rstrip('\x00')
            self.telemetry_status = args[8]
            self.show_online_name = args[9]
            self.platform = args[10]

    def __init__(self, unpack):
        self.number_of_participants = unpack[0]
        self.participant_list = []
        lower_limit = 1
        top_limit = len(participant_arr()) + 1
        for _ in range(0, self.number_of_participants):
            self.participant_list.append(self.Participant(*unpack[lower_limit:top_limit]))
            lower_limit = top_limit + 1
            top_limit = lower_limit + len(participant_arr()) + 1


@dataclass
class CarSetups:
    structure = car_setup_stc

    def __init__(self, unpack):
        self.front_wing = unpack[0]
        self.rear_wing = unpack[1]
        self.on_throttle = unpack[2]
        self.off_throttle = unpack[3]
        self.front_camber = unpack[4]
        self.rear_camber = unpack[5]
        self.front_toe = unpack[6]
        self.rear_toe = unpack[7]
        self.front_suspension = unpack[8]
        self.rear_suspension = unpack[9]
        self.front_anti_roll_bar = unpack[10]
        self.rear_anti_roll_bar = unpack[11]
        self.front_suspension_height = unpack[12]
        self.rear_suspension_height = unpack[13]
        self.brake_pressure = unpack[14]
        self.brake_bias = unpack[15]
        self.rear_left_tyre_pressure = unpack[16]
        self.rear_right_tyre_pressure = unpack[17]
        self.front_left_tyre_pressure = unpack[18]
        self.front_right_tyre_pressure = unpack[19]
        self.ballast = unpack[20]
        self.fuel_load = unpack[21]


@dataclass
class CarTelemetry:
    structure = car_telemetry_stc

    def __init__(self, unpack):
        self.speed = unpack[0]
        self.throttle = unpack[1]
        self.steer = unpack[2]
        self.brake = unpack[3]
        self.clutch = unpack[4]
        self.gear = unpack[5]
        self.engine_rpm = unpack[6]
        self.drs = unpack[7]
        self.rev_light_percent = unpack[8]
        self.rev_light_bit_value = unpack[9]

        self.front_left_brake_temperature = unpack[10]
        self.front_right_brake_temperature = unpack[11]
        self.back_left_brake_temperature = unpack[12]
        self.back_right_brake_temperature = unpack[13]

        self.front_left_tyre_surface_temperature = unpack[14]
        self.front_right_tyre_surface_temperature = unpack[15]
        self.back_left_tyre_surface_temperature = unpack[16]
        self.back_right_tyre_surface_temperature = unpack[17]

        self.front_left_tyre_inner_temperature = unpack[18]
        self.front_right_tyre_inner_temperature = unpack[19]
        self.back_left_tyre_inner_temperature = unpack[20]
        self.back_right_tyre_inner_temperature = unpack[21]

        self.engine_temperature = unpack[22]

        self.front_left_tyre_pressure = unpack[23]
        self.front_right_tyre_pressure = unpack[24]
        self.back_left_tyre_pressure = unpack[25]
        self.back_right_tyre_pressure = unpack[26]

        self.front_left_tyre_surface_type = unpack[27]
        self.front_right_tyre_surface_type = unpack[28]
        self.back_left_tyre_surface_type = unpack[29]
        self.back_right_tyre_surface_type = unpack[30]

        self.mfd_panel_index = unpack[31]
        self.mfd_panel_index_secondary_player = unpack[32]
        self.suggested_gear = unpack[33]


@dataclass
class CarStatus:
    structure = car_status_stc

    def __init__(self, unpack):
        self.traction_control = unpack[0]
        self.anti_lock_brakes = unpack[1]
        self.fuel_mix = unpack[2]
        self.front_brake_bias = unpack[3]
        self.pit_limiter_status = unpack[4]
        self.fuel_in_tank = unpack[5]
        self.fuel_capacity = unpack[6]
        self.fuel_remaining_in_laps = unpack[7]
        self.max_rpm = unpack[8]
        self.idle_rpm = unpack[9]
        self.max_gears = unpack[10]
        self.drs_allowed = unpack[11]
        self.drs_activation_distance = unpack[12]
        self.actual_tyre_compound = unpack[13]
        self.visual_tyre_compound = unpack[14]
        self.tyres_age_laps = unpack[15]
        self.vehicle_fia_flags = unpack[16]
        self.engine_power_ice = unpack[17]
        self.engine_power_mgu_k = unpack[18]
        self.ers_store_energy = unpack[19]
        self.ers_deploy_mode = unpack[20]
        self.ers_harvested_this_lap_mgu_k = unpack[21]
        self.ers_harvested_this_lap_mgu_h = unpack[22]
        self.ers_deployed_this_lap = unpack[23]
        self.network_paused = unpack[24]


@dataclass
class CarDamage:
    structure = car_damage_stc

    def __init__(self, unpack):
        self.front_left_tyre_wear = unpack[0]
        self.front_right_tyre_wear = unpack[1]
        self.rear_left_tyre_wear = unpack[2]
        self.rear_right_tyre_wear = unpack[3]

        self.front_left_tyre_damage = unpack[4]
        self.front_right_tyre_damage = unpack[5]
        self.rear_left_tyre_damage = unpack[6]
        self.rear_right_tyre_damage = unpack[7]

        self.front_left_brake_damage = unpack[8]
        self.front_right_brake_damage = unpack[9]
        self.rear_left_brake_damage = unpack[10]
        self.rear_right_brake_damage = unpack[11]

        self.front_left_wing_damage = unpack[12]
        self.front_right_wind_damage = unpack[13]
        self.rear_wing_damage = unpack[14]
        self.floor_damage = unpack[15]
        self.diffuser_damage = unpack[16]
        self.side_pod_damage = unpack[17]
        self.drs_fault = unpack[18]
        self.ers_fault = unpack[19]
        self.gear_box_damage = unpack[20]
        self.engine_damage = unpack[21]
        self.engine_mgu_h_wear = unpack[22]
        self.engine_es_wear = unpack[23]
        self.engine_ce_wear = unpack[24]
        self.engine_ice_wear = unpack[25]
        self.engine_mgu_k_wear = unpack[26]
        self.engine_tc_wear = unpack[27]
        self.engine_blown = unpack[28]
        self.engine_seized = unpack[29]


@dataclass
class TyreSet:
    structure = tyre_set_stc

    def __init__(self, unpack):
        self.actual_tyre_compound = unpack[0]
        self.visual_tyre_compound = unpack[1]
        self.wear = unpack[2]
        self.available = unpack[3]
        self.recommended_session = unpack[4]
        self.life_span = unpack[5]
        self.usable_life = unpack[6]
        self.lap_delta_time = unpack[7]
        self.fitted = unpack[8]


@dataclass
class MotionExPacket:
    structure = motion_ex_stc

    def __init__(self, unpack):
        self.front_left_tyre_suspension_position = unpack[0]
        self.front_right_tyre_suspension_position = unpack[1]
        self.rear_left_tyre_suspension_position = unpack[2]
        self.rear_right_tyre_suspension_position = unpack[3]

        self.front_left_tyre_suspension_velocity = unpack[4]
        self.front_right_tyre_suspension_velocity = unpack[5]
        self.rear_left_tyre_suspension_velocity = unpack[6]
        self.rear_right_tyre_suspension_velocity = unpack[7]

        self.front_left_tyre_suspension_acceleration = unpack[8]
        self.front_right_tyre_suspension_acceleration = unpack[9]
        self.rear_left_tyre_suspension_acceleration = unpack[10]
        self.rear_right_tyre_suspension_acceleration = unpack[11]

        self.front_left_tyre_speed = unpack[12]
        self.front_right_tyre_speed = unpack[13]
        self.rear_left_tyre_speed = unpack[14]
        self.rear_right_tyre_speed = unpack[15]

        self.front_left_tyre_slip_ratio = unpack[16]
        self.front_right_tyre_slip_ratio = unpack[17]
        self.rear_left_tyre_slip_ratio = unpack[18]
        self.rear_right_tyre_slip_ratio = unpack[19]

        self.front_left_tyre_slip_angle = unpack[20]
        self.front_right_tyre_slip_angle = unpack[21]
        self.rear_left_tyre_slip_angle = unpack[22]
        self.rear_right_tyre_slip_angle = unpack[23]

        self.front_left_tyre_lat_force = unpack[24]
        self.front_right_tyre_lat_force = unpack[25]
        self.rear_left_tyre_lat_force = unpack[26]
        self.rear_right_tyre_lat_force = unpack[27]

        self.front_left_tyre_long_force = unpack[28]
        self.front_right_tyre_long_force = unpack[29]
        self.rear_left_tyre_long_force = unpack[30]
        self.rear_right_tyre_long_force = unpack[31]

        self.height_cog_above_ground = unpack[32]
        self.local_velocity_x = unpack[33]
        self.local_velocity_y = unpack[34]
        self.local_velocity_z = unpack[35]
        self.angular_velocity_x = unpack[36]
        self.angular_velocity_y = unpack[37]
        self.angular_velocity_z = unpack[38]
        self.angular_acceleration_x = unpack[39]
        self.angular_acceleration_y = unpack[40]
        self.angular_acceleration_z = unpack[41]
        self.front_wheel_angle = unpack[42]

        self.front_left_tyre_vert_force = unpack[43]
        self.front_right_tyre_vert_force = unpack[44]
        self.rear_left_tyre_vert_force = unpack[45]
        self.rear_right_tyre_vert_force = unpack[46]


@dataclass
class BodyType:
    options = {
        0: MotionPacket,
        1: ...,
        2: LapData,
        3: ...,
        4: Participants,
        5: CarSetups,
        6: CarTelemetry,
        7: CarStatus,
        8: ...,
        9: ...,
        10: CarDamage,
        11: ...,
        12: TyreSet,
        13: MotionExPacket
    }
