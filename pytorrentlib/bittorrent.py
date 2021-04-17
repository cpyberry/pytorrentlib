import struct
from enum import auto
from .messageid import MessageIdEnum


class CreateMessage:
	"""Create a bittorrent protocol message
	"""

	@staticmethod
	def create_message(message_id: auto, data=b"") -> bytes:
		"""Add the data length and message id to the beginning of the data argument

		Args:
			message_id (auto): member variables of the MessageIdEnum class
			data (bytes, optional): binary after message id. Defaults to b"".

		Returns:
			bytes: binary with data length and message id added to the data argument
		"""
		length = len(data) + 1  # add 1 byte of message_id
		return struct.pack(">IB", length, message_id.value) + data

	@staticmethod
	def handshake(info_hash: bytes, peer_id: bytes) -> bytes:
		"""Create handshake message

		Args:
			info_hash (bytes): sha1 hash of torrentfile info dictionary
			peer_id (bytes): unique id of the client generated at startup

		Returns:
			bytes: handshake message
		"""
		encoding = "ascii"
		ptsr = "BitTorrent protocol".encode(encoding)
		ptstlen = struct.pack(">B", len(ptsr))
		empty = bytes(8)
		handshake = ptstlen + ptsr + empty + info_hash + peer_id
		return handshake

	@classmethod
	def choke(cls) -> bytes:
		"""Create choke message

		Returns:
			bytes: choke message
		"""
		return cls.create_message(MessageIdEnum.CHOKE)
