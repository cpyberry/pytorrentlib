# pytorrentlib

torrentクライアントを作成したりするのに便利なライブラリです。

## 必要な一般ライブラリ

* [pybencode](https://github.com/cpyberry/pybencode)
* [pytransform](https://github.com/cpyberry/pytransform)

## 機能

このライブラリには、大まかに以下の機能があります。

* torrentファイルのparser
* bittorrentメッセージの生成
* trackerとのやり取り

## 使い方

torrentファイルをparseしたい時

```python
from pytorrentlib import ParseTorrentFile


parser = ParseTorrentFile("example.torrent")
parser.get_pieces()  # 各ピースのsha1 hashが格納されたリスト
parser.get_info_hash()  # info辞書のsha1ハッシュ
parser.is_single_file()  # 配信されているファイルが1つか調べる
parser.get_total_size()  # 配信されているファイルの合計サイズ
```

トラッカーとやり取りしたい時

```python
from pytorrentlib import Tracker, EventStatus


tracker = Tracker(
	tracker_url="example.com"  # 送信先url
	peer_port=22222 # torrentクライアントに接続するのに必要なポート  ※1
	info_hash=parser.get_info_hash()  # info辞書のsha1ハッシュ  ※2
	peer_id=b"20bytes id"  # クライアント起動時に生成した一意な20bytesのid  ※3
	headers={"User-Agent": "cat"}  # トラッカーとやり取りする際に送信するHTMLリクエストに付与するheader
)

# ※1  port mappingした場合など、torrentクライアントがbindしたポートとは限らない。
# ※2  torrentファイルを参考にファイルをやり取りする場合、先ほどのtorrentファイルのparserの機能の一つ、get_info_hashメソッドを使用してください。
# ※3  sha1ハッシュで生成されるデータは20bytesなので、幅の広い適当な乱数のsha1ハッシュでも良い。

tracker.access(
	event=EventStatus.STARTED  # クライアントの状態
	uploaded=0  # アップロードしたデータの合計サイズ
	downloaded=0  # ダウンロードしたデータの合計サイズ
	left=22222  # ダウンロードしなければいけないデータの合計サイズ
)
```

bittorrentメッセージを生成したい時

```python
from pytorrentlib import CreateMessage


CreateMessage.handshake(
	info_hash=parser.get_info_hash()  # info辞書のsha1ハッシュ、先ほどと同様。
	peer_id=b"20 bytes"  # クライアント起動時に生成した一意な20bytesのid
)
CreateMessage.choke()  # chokeメッセージ
CreateMessage.unchoke()  # unchokeメッセージ
```

他にも沢山のメッセージ生成の機能（have、bitfield、requestなど）があります。

## 創始者

* [cpyberry](https://github.com/cpyberry)

	email: cpyberry222@gmail.com
