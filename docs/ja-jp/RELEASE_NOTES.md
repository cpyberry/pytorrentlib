# リリースノート

## v1.1.1

* \_\_init\_\_.pyのF403違反を修正
* README.mdにより詳しい説明を追加
* 日本語版README.mdの追加
* RELEASE_NOTES.mdの追加
* 日本語版RELEASE_NOTES.mdの追加

## v1.1.0

* 以下のbittorrentプロトコルのメッセージの作成に対応
	* keep-alive
	* port
* bittorrentプロトコルのmessage idに対応した列挙子にportメッセージを追加
* ピアの状態を保管するビットマスクにportメッセージを追加

## v1.0.0

* bittorrentプロトコルのメッセージの作成  ※1
* bittorrentプロトコルのmessage idに対応した列挙子  ※2
* ピアの状態を保管するビットマスク  ※3
* torrentファイルのパーサー
* トラッカーとのやり取りを行うクラス

※1, 2, 3に対応したのは以下のbittorrentプロトコルのメッセージです。

* choke
* unchoke
* interest
* nointerest
* have
* bitfield
* request
* piece
* cancel

torrentファイルのパーサーには以下の機能があります。

* sha1ハッシュのpieceのリストの取得
* info_hashの取得
* 配信されているのが単一のファイルか調べる
* 配信されているファイルの総サイズを取得する

トラッカーとのやり取りをするクラスには以下の機能があります。

* トラッカーにクライアントの情報を送信する機能
