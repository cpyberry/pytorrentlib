# pytorrentlib

This library simplifies communication with trackers, composing messages for the bittorrent protocol, etc.

## Requirement

* [pybencode](https://github.com/cpyberry/pybencode)
* [pytransform](https://github.com/cpyberry/pytransform)

## Usage

When you want to parse a torrent file, you can write:

```python
from pytorrentlib import ParseTorrentFile


parser = ParseTorrentFile("example.torrent")
parser.get_pieces()  # get pieces are stored sha1 hash
parser.get_info_hash()  # get the sha1 hash of the info dictionary
parser.is_single_file()  # find out if the file being delivered is single or multiple
parser.get_total_size()  # get Total size of delivered files
```

When you want to communicate with tracker, you can write:

```python
from pytorrentlib import Tracker, EventStatus


tracker = Tracker(
	tracker_url="example.com"  # destination url
	peer_port=22222 # the port number that the client is listening on
	info_hash=parser.get_info_hash()  # sha1 hash of torrentfile info dictionary
	peer_id=b"20bytes id"  # unique id of the client generated at startup
	headers={"User-Agent": "cat"}  # header when communicating with tracker
)

tracker.access(
	event=EventStatus.STARTED  # client state
	uploaded=0  # amount uploaded
	downloaded=0  # amount downloaded
	left=22222  # remaining amount
)
```

When you want to compose messages for the bittorrent protocol, you can write:

```python
from pytorrentlib import CreateMessage


CreateMessage.handshake(
	info_hash=parser.get_info_hash()  # sha1 hash of torrentfile info dictionary
	peer_id=b"20 bytes"  # unique id of the client generated at startup
)
CreateMessage.choke()
CreateMessage.unchoke()
```

There are many others.

## Founder

* [cpyberry](https://github.com/cpyberry)

	email: cpyberry222@gmail.com
