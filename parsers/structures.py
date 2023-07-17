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
