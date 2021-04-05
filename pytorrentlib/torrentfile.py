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

	@staticmethod
	def operation_value(value, origin: dict, key: bytes):
		if (type(value) != bytes) or (key == b"pieces"):
			return value
		else:
			return value.decode(ENCODING)


class ParseTorrentFile:
	"""Class for parsing torrent file

	Attributes:
		raw_content (str): content decoded in bencode format
		content (str): decode the part that can be decoded, leave it in list
	"""

	def __init__(self, path: str):
		"""
		Args:
			path (str): path of torrent file you want to read
		"""
		self.raw_content = self.load_torrent_file(path)
		self.content = pytransform.transform_dictionary(
			origin=self.raw_content,
			operation_key=DecodeTorrentFile.operation_key,
			operation_value=DecodeTorrentFile.operation_value
		)

	def get_pieces(self) -> list:
		""" Get pieces are stored sha1 hash

		Piece is used to check the suitability of split data in torrent

		Returns:
			list: pieces are stored sha1 hash
		"""
		pieces = []

		# sha1 hash is stored in units of 20 bytes
		raw_pieces = self.content["info"]["pieces"]

		raw_pieces_len = len(raw_pieces)

		for index in range(0, raw_pieces_len, 20):
			pieces.append(raw_pieces[index:index + 20])

		return pieces

	@staticmethod
	def load_torrent_file(path: str) -> dict:
		"""Load torrent file so that it can be handled as dict type

		Args:
			path (str): path of torrent file you want to read

		Returns:
			dict: content decoded in bencode format
		"""
		with open(path, "rb") as f:
			data = f.read()

		return pybencode.decode(data)
