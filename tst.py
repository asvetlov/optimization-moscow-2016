import sys
import timeit

import pyximport; pyximport.install()

from ws1 import _websocket_mask_cython1



native_byteorder = sys.byteorder


def _websocket_mask_python(mask, data):
    assert isinstance(data, bytearray), data
    assert len(mask) == 4, mask
    datalen = len(data)
    if datalen == 0:
        return bytearray()
    data = int.from_bytes(data, native_byteorder)
    mask = int.from_bytes(mask * (datalen // 4) + mask[: datalen % 4],
                          native_byteorder)
    return (data ^ mask).to_bytes(datalen, native_byteorder)



setup = "mask=b'1234'; data=bytearray(b'1234567890'*100); from __main__ import _websocket_mask_python, _websocket_mask_cython1"

print(timeit.timeit('_websocket_mask_python(mask, data)', setup))

print(timeit.timeit('_websocket_mask_cython1(mask, data)', setup))
