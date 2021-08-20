# Release Notes

## v1.1.1

* Fix F403 violation in \_\_init\_\_.py
* Add more detailed description in README.md
* Add Japanese README.md
* Add RELEASE_NOTES.md
* Add Japanese RELEASE_NOTES.md

## v1.1.0

* Support creating messages for the following bittorrent protocols
	* keep-alive
	* port
* Add port message to enumerator corresponding to message id of bittorrent protocol
* Add port message to bitmask to store peer state

## v1.0.0

* Create a bittorrent protocol message  ※1
* Enumerator corresponding to the message id of the bittorrent protocol  ※2
* Bit mask that stores the state of peers  ※3
* Torrent file parser
* Classes that interact with trackers

※1, ※2 and ※3 are supported by the following bittorrent protocol messages.

* choke
* unchoke
* interest
* nointerest
* have
* bitfield
* request
* piece
* cancel

The torrent file parser has the following features:

* Get a list of sha1 hash pieces
* Get info_hash
* Find out if a single file is being delivered
* Get the total size of the delivered files

Tracker class that interact with trackers have the following features:

* Send client information to tracker
