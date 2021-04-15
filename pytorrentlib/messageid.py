from enum import Enum, Flag, auto


class MessageIdFlag(Flag):
	"""This is used to remember the state of the peer
	"""
	CHOKE = auto()  # 0
	UNCHOKE = auto()  # 1
	INTEREST = auto()  # 2
	NOINTEREST = auto()  # 3
	HAVE = auto()  # 4
	BITFIELD = auto()  # 5
	REQUEST = auto()  # 6
	PIECE = auto()  # 7
	CANCEL = auto()  # 8


class MessageIdEnum(Enum):
	"""Enum corresponding to message and id
	"""
	CHOKE = 0
	UNCHOKE = 1
	INTEREST = 2
	NOINTEREST = 3
	HAVE = 4
	BITFIELD = 5
	REQUEST = 6
	PIECE = 7
	CANCEL = 8
