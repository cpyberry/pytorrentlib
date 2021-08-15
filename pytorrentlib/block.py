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

	def get_piece_path(self, index: int) -> str:
		"""Get the path that stores the piece.

		Args:
			index (int): piece index.

		Returns:
			str: path that stores the piece.
		"""
		return os.path.join(self.piece_dir_path, str(index))
