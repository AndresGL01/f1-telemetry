import struct
from parsers.constants import StructTypes as st


def packet_header_stc():
    return struct.Struct(
        st.fmt_str(
            [
                st.UINT16, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UINT64,
                st.FLOAT, st.UINT32, st.UINT32, st.UCHAR8, st.UCHAR8
            ]
        )
    )


def motion_stc():
    return struct.Struct(
        st.fmt_str(
            [
                st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.UINT16, st.UINT16,
                st.UINT16, st.UINT16, st.UINT16, st.UINT16, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT,
                st.FLOAT, st.FLOAT
            ]
        )
    )


def session_stc():
    ...


def lap_data_stc():
    return struct.Struct(
        st.fmt_str(
            [
                st.UINT32, st.UINT32, st.UINT16, st.UCHAR8, st.UINT16, st.UCHAR8, st.UINT16,
                st.UINT16, st.FLOAT, st.FLOAT, st.FLOAT, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8,
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8,
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UINT16, st.UINT16, st.UCHAR8,
                st.UCHAR8, st.UCHAR8
            ]
        )
    )


def event_stc():
    ...


def participant_arr():
    return [
        st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8,
        st.CHAR_48_BYTES, st.UCHAR8, st.UCHAR8, st.UCHAR8
    ]


def participants_stc(raw: bytes):
    """
    Participants packet have one particularity, the structure is:
    - Header
    - number of active participants
    - array of participants
    The number of participants is variable so this method need to calculate how many participants
    are racing to return a correct decoder
    :return:
    """
    sub_participants_stc = struct.Struct(st.fmt_str([st.UCHAR8]))
    number_of_participants: int = sub_participants_stc.unpack(raw[:sub_participants_stc.size])[0]

    participant_format = [st.UCHAR8]
    for _ in range(0, number_of_participants):
        participant_format.extend(participant_arr())

    return struct.Struct(st.fmt_str(participant_format))


def car_setup_stc():
    return struct.Struct(
        st.fmt_str(
            [
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT,
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8,
                st.UCHAR8, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.UCHAR8, st.FLOAT
            ]
        )
    )


def car_telemetry_stc():
    return struct.Struct(
        st.fmt_str(
            [
                st.UINT16, st.FLOAT, st.FLOAT, st.FLOAT, st.UCHAR8, st.CHAR8, st.UINT16, st.UCHAR8,
                st.UCHAR8, st.UINT16, st.UINT16, st.UINT16, st.UINT16, st.UINT16, st.UCHAR8,
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8,
                st.UINT16, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.UCHAR8, st.UCHAR8, st.UCHAR8,
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.CHAR8
            ]
        )
    )


def car_status_stc():
    return struct.Struct(
        st.fmt_str(
            [
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.FLOAT, st.FLOAT, st.FLOAT,
                st.UINT16, st.UINT16, st.UCHAR8, st.UCHAR8, st.UINT16, st.UCHAR8, st.UCHAR8,
                st.UCHAR8, st.CHAR8, st.FLOAT, st.FLOAT, st.FLOAT, st.UCHAR8, st.FLOAT, st.FLOAT,
                st.FLOAT, st.UCHAR8
            ]
        )
    )


def car_damage_stc():
    return struct.Struct(
        st.fmt_str(
            [
                st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8,
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8,
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8,
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8,
                st.UCHAR8
            ]
        )
    )


def tyre_set_stc():
    return struct.Struct(
        st.fmt_str(
            [
                st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8, st.UCHAR8,
                st.CHAR8, st.UCHAR8
            ]
        )
    )


def motion_ex_stc():
    return struct.Struct(
        st.fmt_str(
            [
                st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT,
                st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT,
                st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT,
                st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT,
                st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT,
                st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT, st.FLOAT
            ]
        )
    )
