from peewee import (
    SqliteDatabase,
    Model,
    UUIDField,
    TextField,
    FloatField,
    IntegerField
)

db = SqliteDatabase('../logs.db')


class Packet(Model):
    id = UUIDField(primary_key=True)
    payload = TextField()
    packet_id = IntegerField()
    timestamp = IntegerField()

    class Meta:
        database = db


class LapData(Model):
    last_lap_ms = IntegerField()
    current_lap_ms = IntegerField()
    first_sector_ms = IntegerField()
    first_sector_min = IntegerField()
    second_sector_ms = IntegerField()
    second_sector_min = IntegerField()
    delta_to_car_in_front_ms = IntegerField()
    delta_to_leader_in_front_ms = IntegerField()
    lap_distance_in_meters = FloatField()
    total_distance = FloatField()
    safety_car_delta = IntegerField()
    car_position = IntegerField()
    current_lap = IntegerField()
    pit_status = IntegerField()
    num_pit_stops = IntegerField()
    sector = IntegerField()
    current_lap_invalid = IntegerField()
    penalties = IntegerField()
    total_warnings = IntegerField()
    corner_cutting_warnings = IntegerField()
    num_un_served_drive_through_pens = IntegerField()
    num_un_server_stop_and_go_pens = IntegerField()
    grid_pos = IntegerField()
    driver_status = IntegerField()
    result_status = IntegerField()
    pit_lane_timer_status = IntegerField()
    pit_lane_time_in_lane_ms = IntegerField()
    pit_stop_ms = IntegerField()
    pit_stop_should_serve_pen = IntegerField()
    time_trial_pb_car_index = IntegerField()
    time_trial_rival_car_index = IntegerField()

    class Meta:
        database = db