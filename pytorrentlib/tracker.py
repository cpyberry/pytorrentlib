from enum import Enum, auto


class EventStatus(Enum):
	"""This is used to show your status to the tracker
	"""
	STARTED = auto()
	STOPPED = auto()
	COMPLETED = auto()
