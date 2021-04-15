from enum import Enum, auto


class EventStatus(Enum):
	"""This is used to show your status to the tracker
	"""
	STARTED = auto()
	STOPPED = auto()
	COMPLETED = auto()


class Tracker:
	"""This is used to communicate with tracker

	Attributes:
		tracker_url (str): destination url
		peer_port (int): the port number that the client is listening on
		info_hash (bytes): sha1 hash of torrentfile info dictionary
		peer_id (bytes): unique id of the client generated at startup
		headers (dict): header when communicating with tracker
	"""

	def __init__(self, tracker_url: str, peer_port: int, info_hash: bytes, peer_id: bytes, headers={}):
		"""
		Args:
			tracker_url (str): destination url
			peer_port (int): the port number that the client is listening on
			info_hash (bytes): sha1 hash of torrentfile info dictionary
			peer_id (bytes): unique id of the client generated at startup
			headers (dict, optional): header when communicating with tracker. Defaults to {}.
		"""
		self.tracker_url = tracker_url
		self.peer_port = peer_port
		self.info_hash = info_hash
		self.peer_id = peer_id
		self.headers = headers
