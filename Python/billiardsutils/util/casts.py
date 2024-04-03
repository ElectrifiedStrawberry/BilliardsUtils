from __future__ import annotations

import struct
import typing

_BIG = '>'
_LITTLE = '<'
_MACHINE = '@'

_U32 = 'I'
_F32 = 'f'

def _get_endianness_symbol(endianness: bool | None=None) -> str:
	if endianness is None: return _MACHINE
	return _BIG if endianness else _LITTLE


def _cast(x: typing.Any, sym_in: str, sym_out: str, endianness: bool | None=None) -> typing.Any:
	s: str = _get_endianness_symbol(endianness)
	return struct.unpack(s + sym_out, struct.pack(s + sym_in, x))[0]



def u32_to_f32(x: int, endianness: bool | None=None) -> float:
	'''
	Converts an integer to a floating point value
	:param x: The value to convert
	:param endianness: True for big, False for little, None for machine
	'''
	return _cast(x, _U32, _F32, endianness)


def f32_to_u32(x: float, endianness: bool | None=None) -> int:
	'''
	Converts a floating point value to an integer
	:param x: The value to convert
	:param endianness: True for big, False for little, None for machine
	'''
	return _cast(x, _F32, _U32, endianness)
