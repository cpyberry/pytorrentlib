from enum import Flag, auto


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
