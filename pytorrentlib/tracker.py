"""
Copyright 2021 cpyberry
https://github.com/cpyberry/pytorrentlib

cpyberry
email: cpyberry222@gmail.com
github: https://github.com/cpyberry
"""


import requests
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

	def access(self, event: auto, uploaded: int, downloaded: int, left: int) -> bytes:
		"""This is used to communicate with tracker

		Args:
			event (auto): attribute of EventStatus class
			uploaded (int): amount uploaded
			downloaded (int): amount downloaded
			left (int): remaining amount

		Returns:
			bytes: response from tracker
		"""
		data = {
			"info_hash": self.info_hash,
			"port": self.peer_port,
			"peer_id": self.peer_id,
			"event": event.name.lower(),  # must be in lowercase instead of uppercase
			"downloaded": downloaded,
			"uploaded": uploaded,
			"left": left
		}

		resp = requests.get(self.tracker_url, headers=self.headers, params=data)
		return resp.content
