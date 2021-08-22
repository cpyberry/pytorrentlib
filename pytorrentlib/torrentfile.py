"""
Copyright 2021 cpyberry
https://github.com/cpyberry/pytorrentlib

cpyberry
email: cpyberry222@gmail.com
github: https://github.com/cpyberry
"""


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

	def get_info_hash(self) -> bytes:
		"""Get sha1 hash of info

		Sha1 hash of info is used when interacting with tracker etc

		Returns:
			bytes: sha1 hash of info
		"""
		info_bencode = pybencode.encode(self.raw_content[b"info"])
		info_hash = hashlib.sha1(info_bencode).digest()
		return info_hash

	def is_single_file(self) -> bool:
		"""Find out if the file being delivered is single or multiple

		Returns:
			bool: If it is single file, True will be returned
		"""
		# If files being delivered is not single, there is ile in info
		files = self.content["info"].get("files")

		return not bool(files)

	def get_tracker_announce_url(self) -> str:
		"""Get the tracker announce url.

		Returns:
			str: the tracker announce url.
		"""
		return self.content["announce"]

	def get_total_size(self) -> int:
		"""Get Total size of delivered files

		Returns:
			int: total size of delivered files
		"""
		size = 0

		if self.is_single_file():
			size = self.content["info"]["length"]
		else:
			files = self.content["info"]["files"]
			for file in files:
				size += file["length"]

		return size

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
