# pytorrentlib

This library simplifies communication with trackers, composing messages for the bittorrent protocol, etc.

## Requirement

* [pybencode](https://github.com/cpyberry/pybencode)
* [pytransform](https://github.com/cpyberry/pytransform)

## Feature

The library has the following general features:

* torrent file parser
* create bittorrent message
* communicate with tracker

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
	peer_port=22222 # the port number that the client is listening on  ※1
	info_hash=parser.get_info_hash()  # sha1 hash of torrentfile info dictionary  ※2
	peer_id=b"20bytes id"  # unique id of the client generated at startup  ※3
	headers={"User-Agent": "cat"}  # header given to HTML request sent when communicating with tracker
)

# ※1  It is not always the port bound by the torrent client, such as when port mapping is performed.
# ※2  When exchanging files with reference to the torrent file, use the get_info_hash method, which is one of the parser functions of the torrent file.
# ※3  Since the data generated by the sha1 hash is 20 bytes, a wide and appropriate random number sha1 hash may be used.

tracker.access(
	event=EventStatus.STARTED  # client state
	uploaded=0  # total size of uploaded data
	downloaded=0  # total size of downloaded data
	left=22222  # total data that have to be downloaded
)
```

When you want to compose messages for the bittorrent protocol, you can write:

```python
from pytorrentlib import CreateMessage


CreateMessage.handshake(
	info_hash=parser.get_info_hash()  # sha1 hash of torrentfile info dictionary
	peer_id=b"20 bytes"  # unique id of the client generated at startup
)
CreateMessage.choke()  # choke message
CreateMessage.unchoke()  # unchoke message
```

There are many other message creation features, such as `have`, `bitfield`, and `request`.

## Founder

* [cpyberry](https://github.com/cpyberry)

	email: cpyberry222@gmail.com
