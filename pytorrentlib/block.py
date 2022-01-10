import hashlib
import os


class Block:
	"""
	This class manages torrent pieces.
	"""

	def __init__(self, piece_hash_list: list, piece_dir_path="."):
		"""
		Args:
			piece_hash_list (int): the pieces in the torrentfile.
			piece_dir_path (str, optional): directory path to save downloaded pieces. Defaults to ".".
		"""
		self.piece_hash_list = piece_hash_list
		self.piece_dir_path = piece_dir_path
		self.piece_length = len(piece_hash_list)
		self.piece_status_list = [False] * self.piece_length

	def read(self, index: int, offset=0, size=-1) -> bytes:
		"""Read the specified piece.

		If you omit the size argument, all the data from the offer argument is read.

		Args:
			index (int): piece index.
			offset (int, optional): start position to read. Defaults to 0.
			size (int, optional): size to read. Defaults to -1.

		Returns:
			bytes: read piece data.
		"""
		path = self.get_piece_path(index)

		if not os.path.exists(path):
			return b""

		with open(path, "rb") as f:
			f.seek(offset)
			data = f.read(size)
		return data

	def write(self, index: int, data: bytes, offset=0) -> None:
		"""Write the specified piece.

		Args:
			index (int): piece index.
			data (bytes): the data you want to write.
			offset (int, optional): start position to write. Defaults to 0.
		"""
		path = self.get_piece_path(index)
		# In a mode, even if you seek, it is written at the end.
		with open(path, "r+b") as f:
			f.seek(offset)
			f.write(data)

	def is_completed(self, index: int) -> bool:
		"""Check if the saved piece is compatible.

		Args:
			index (int): piece index.

		Returns:
			bool: return True if conforming, False otherwise.
		"""
		data = self.read(index)
		data_hash = hashlib.sha1(data).digest()
		return data_hash == self.piece_hash_list[index]

	def update_completed_list_index(self, index: int) -> bool:
		"""Check the suitability of the specified piece and update self.piece_status_list.

		Args:
			index (int): piece index.

		Returns:
			bool: return True if conforming, False otherwise.
		"""
		if not self.piece_status_list[index]:
			completed = self.is_completed(index)
			self.piece_status_list[index] = completed
		return self.piece_status_list[index]

	def update_completed_list_all(self) -> list:
		"""Check the suitability of all piece and update self.piece_status_list.

		Returns:
			list: return self.piece_status_list.
		"""
		for index in range(len(self.piece_status_list)):
			self.update_completed_list_index(index)
		return self.piece_status_list

	def get_piece_path(self, index: int) -> str:
		"""Get the path that stores the piece.

		Args:
			index (int): piece index.

		Returns:
			str: path that stores the piece.
		"""
		return os.path.join(self.piece_dir_path, str(index))
