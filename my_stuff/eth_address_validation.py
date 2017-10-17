

from ethereum.utils import normalize_address

from bitcoin import privtopub
import sys
import rlp
from rlp.sedes import big_endian_int, BigEndianInt, Binary
from rlp.utils import decode_hex, encode_hex as _encode_hex, ascii_chr, str_to_bytes
from ethereum.utils import zpad

import random
a1='3078d0ae364ead991cb99018496b2b2388edd2182e76'
a2='0x3078d0ae364ead991cb99018496b2b2388edd2182e76'


def add_padding(address):
    """
    Provide proper length of address and add 0x to it
    :param address: Address to validation
    :return: Padded address
    """
    if address is None:
        return address
    elif isinstance(address, str):
        address = address.encode()
    if isinstance(address, bytes):
        if address.startswith(b'0x'):
            return address
        return b'0x' + zpad(address, 32)
    raise TypeError('Address must be a string or a byte string')


print(len(a1))
dec = decode_hex(a1)
print(dec)


n = normalize_address("7b82fd1672b8020415d269c53cd1a2230fde9386")
x = normalize_address(add_padding(a2))
print('==========')