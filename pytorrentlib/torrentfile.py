import hashlib
import pybencode
import pytransform


ENCODING = "ascii"


class DecodeTorrentFile:
	"""After decoding in bencode format, decode the binary part that meets the conditions
	"""

	@staticmethod
	def operation_key(key: bytes, origin: dict, value: bytes) -> str:
		return key.decode(ENCODING)


class ParseTorrentFile:
	"""Class for parsing torrent file
	"""

	def __init__(self, path: str):
		"""
		Args:
			path (str): path of torrent file you want to read
		"""
		pass
