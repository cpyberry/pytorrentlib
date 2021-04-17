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
