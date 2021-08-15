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

	def get_piece_path(self, index: int) -> str:
		"""Get the path that stores the piece.

		Args:
			index (int): piece index.

		Returns:
			str: path that stores the piece.
		"""
		return os.path.join(self.piece_dir_path, str(index))
