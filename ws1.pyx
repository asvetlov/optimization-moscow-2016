import sys

native_byteorder = sys.byteorder


def _websocket_mask_cython1(mask, data):
    assert isinstance(data, bytearray), data
    assert len(mask) == 4, mask
    datalen = len(data)
    if datalen == 0:
        return bytearray()
    data = int.from_bytes(data, native_byteorder)
    mask = int.from_bytes(mask * (datalen // 4) + mask[: datalen % 4],
                          native_byteorder)
    return (data ^ mask).to_bytes(datalen, native_byteorder)
