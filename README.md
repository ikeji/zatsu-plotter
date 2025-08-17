# 雑プロッタ

コンピュータを使って物理的な機械を動かしたい。
今回は、ペンを設定した通り動かすペンプロッタを作りたい。

既存の作例は、リニアレールを使ったり既存の直動機構を使ったり、
専用の部品を使って精度高く作ってあるものが多い。

今回は、誰の家にもありそうな、汎用の部品と、
3Dプリンタで印刷したもの、
あとは100円ショップで買えるものを組み合わせて組む事で、
肩肘立てずに適当に作れる事を目標にした。

## 用意するもの

3つのグループの物が必要。

### 通販で買った物

今回のために特別に買ったのではなく、家に落ちてたものを使った。

- RaspberryPi Pico (もしくは互換ボード) 1つ 300円ぐらい
- 28BYJ-48ステッピングモータ 2つ 制御基板つきのもの 200円ぐらい
- M3 ボルトナットセット 500円ぐらい
- ジャンパワイヤ
- ブレットボード

自分はどれもAliexpressで買った。
国内の通販でも買えると思う。

### ダイソーで買った物 660円ぐらい

- バインダー ![](https://uploader.apps.ikeji.ma/file/26b6ad718e562c45ac664778a65c9d81/29b225f8-b657-4f53-a602-d86ef7db9560~1.jpg)
- 凧糸 ![](https://uploader.apps.ikeji.ma/file/554f9501d375a579f95225870d914cc6/1f866802-69ff-4781-a5d6-83dbf3fdb5b8~1.jpg)
- 太さ3mmのたけひご ![](https://uploader.apps.ikeji.ma/file/225bd9ebeb3b05e649e90d20d582990f/PXL_20250811_165156904.RAW-01.COVER.jpg)
- ボールペン
- はさみ
- ねじまわし

プラスチックのバインダーはポリカーネート製で、厚さが2mmあった。

ペンはゴムの持ち手がついてない方がよさそう。
鉛筆でもいいかも。

### 3Dプリンタで印刷したもの

- (A)[プーリー](./step/a-pully.step) 8つ ![](https://uploader.apps.ikeji.ma/file/fdb61d807233d40d4f1939bcb376d20c/320df7ec-0f20-4f2a-a2c1-77316c963975~1.jpg)
- (B)[プーリークリップ](./step/b-pully-clip.step) 2つ ![](https://uploader.apps.ikeji.ma/file/143b8d736f12af4140bd8fba50ab57bf/e782be46-7fb9-4d57-987c-f2df75e39552~1.jpg)
- (C)[プーリー軸](./step/c-pully-axis.step) 2つ ![](https://uploader.apps.ikeji.ma/file/19a988a16bd233fb0ee298f51f00f7d7/9801f13c-6a5c-4a3a-a01f-0bcc9ae9f093~1.jpg)
- (D)[モータークリップ](./step/d-motor-clip.step) 2つ ![](https://uploader.apps.ikeji.ma/file/07ce78b524179db7fe1bbf58b169b1cb/51f14226-2e7a-4901-a57a-36110730121c~1.jpg)
- (E)[モーター用プーリー](./step/e-motor-pully.step) 2つ ![](https://uploader.apps.ikeji.ma/file/8fab9581df4d73bd59f288a8c060c049/c071d57b-7c7f-48c5-9889-edb0fbbbd962~1.jpg)
- (F)[Xブロック](./step/f-x-block.step) 2つ ![](https://uploader.apps.ikeji.ma/file/c925b70e08841128fc325490493fdeb2/38009a7f-dcc7-4b1c-b82c-8072d16fdf31~1.jpg)
- (G)[Xブロック軸](./step/g-x-block-cap.step) 2つ ![](https://uploader.apps.ikeji.ma/file/edfc3341e7f377bb99f4e2d9bcef7036/62524863-9ef0-4c37-aeb4-5435118d672b~1.jpg)
- (H)[ヘッド](./step/h-head.step) 1つ ![](https://uploader.apps.ikeji.ma/file/1469bdeba9a156390a80a3a912d7f106/9daf8a5b-0054-46bb-9f5c-3bc9f2ebacf6~1.jpg)

FreeCADでデザインした。

自分はBambuLabのP1Sで印刷したが、
だいたいのプリンタでは印刷できると思う。

このプロッタを作りたいけど、
3Dプリンタがなくて困ってるという人は、
日本国内の住所を教えてくれたら郵便で送ります。

## モジュールの組み立て

### 2連プーリーモジュール

(B)プーリークリップには、ナットを入れる所が2箇所があるので押し込む。
反対からボルトを入れて締めると入れやすい。

(C)プーリー軸にも2箇所に入れるところがあるので入れる。
裏表に注意

![](https://uploader.apps.ikeji.ma/file/6ff2091df0912387430b9a7934415ce1/55cd3c2e-5746-4637-b8f6-f3024289cdb3~1.jpg)

(A)プーリーを挟んで8mmのネジと10mmのネジで組み立てる。

![](https://uploader.apps.ikeji.ma/file/aec2a8bcfaf4c286b60ca93914e75dc6/ed01cfb3-0a4b-4e4c-8617-14d795254729~1.jpg)

### モーターモジュール

28BYJ-48モータを(D)モータクリップにつける。
5mmのボルトで止める。

モータの軸に(E)モータ用プーリーをつける。
抜けないようにキツめに作ってあるので、
がんばって押し込む。

![](https://uploader.apps.ikeji.ma/file/1e684e6262f454ec0a6a3ac141585a52/d8b154cc-03ba-487c-be46-f34f5e5ec809~1.jpg)
![](https://uploader.apps.ikeji.ma/file/3883de7e241aebaf85feda17a10cf5f5/3f341cc6-b564-4b76-a4f6-3e0f442a98e5~1.jpg)

### Xモジュール

まず、2連プーリーモジュールと同じ感じで組み立てる。

(F)Xブロックに2個、(G)X軸に2つナットを入れる。

![](https://uploader.apps.ikeji.ma/file/96fb2900a14befb74aa0bbebd09b1fea/3e7f419c-410f-47de-b365-77a99d99600c~1.jpg)

左右のブロックをたけひごでつなぐ。
モジュール全体の長さがバインダーの幅と同じになるように調整したい。
たけひごはバインダーの幅から1cm減らした長さに切る。

![](https://uploader.apps.ikeji.ma/file/2f0b5b75203b0eeed1c5388ac761ef01/PXL_20250811_171027634.RAW-01.COVER~2.jpg)
![](https://uploader.apps.ikeji.ma/file/cb603569100d7ef15a5bcb9f473faf1a/f3280a6e-4990-499f-89a6-faaddfb76c51~1.jpg)

### ヘッド

裏にナット4つをつける。
表に5mmのボルトを入れる。

![](https://uploader.apps.ikeji.ma/file/72b0818063d83fee3eadcf03709f941a/630b525f-7a74-407e-801b-2642336eb9ca~1.jpg)

ペンを付けられるように20mmのボルトとナットをつける。

![](https://uploader.apps.ikeji.ma/file/6fe6fdfab8a1ff467fbaa025ee00686b/911c7eb3-1244-43bd-980e-22c3c26af903~1.jpg)

## 全体の組み立てと糸張り

### 四隅のモジュールの固定

バインダーの四隅にプーリーモジュールとモーターモジュールを挟む。
裏返して、紐をまわして縛る。
これで、バインダーにモジュールを固定してる。

![](https://uploader.apps.ikeji.ma/file/4798a88f782868ec7f12a810b51246f1/636afe53-6a89-4066-a51c-3fb308d60296~1.jpg)
![](https://uploader.apps.ikeji.ma/file/2f089fe371d431295fce151ea48ea4be/49232ea7-e58f-466b-b663-26ec8897cbac~1.jpg)

### 糸張り

Xモジュールとヘッドを置き、糸をはわせる。

次の図を参照

![](https://uploader.apps.ikeji.ma/file/ea057678b10410e644b13daf8dd62802/PXL_20250812_021223526.RAW-01.COVER~2.jpg)

1本の糸で、1-14まで順番に通す。
糸がピンと張るようにして、糸の両端をネジで止める。

中間(7と8の間)のネジはゆるめておき、
たけひごとヘッドが、水平になるように調整し中間をネジで止める。

![](https://uploader.apps.ikeji.ma/file/0e6d4b6df07d049b33aa93a24b254f00/PXL_20250812_021223526.RAW-01.COVER~3.jpg)

## 配線

モータを制御基板を経由してマイコンにつなぐ。
左のモータをマイコンの0-3ピン、
右のモータをマイコンの4-7ピンにつないだ。

制御基板の電源をマイコンのVCCとGNDにつなぐ。
自分は分配にブレッドボードを使った。

## ソフトウエア

自分はMicroPythonで制御した。

MicroPythonのサイトからU2Fをダウンロードし、
RaspberryPiに入れる。

次に用意したサンプルスクリプト([sample.py](./firmware/sample.py))を書き込む。
Linuxならmpremoteコマンドを使ってる。
このスクリプトは設定した四角形を描く。

## しくみ

このプロッタはCoreXY方式を使っている。

左右のモーターを同じ方向にまわすとヘッドが左右に動く。
例えば、両方のモータを反時計回りに動かすと、ヘッドは右に動く。

![](https://uploader.apps.ikeji.ma/file/e4240cd33ce087afbe12b78b6bafdd35/PXL_20250812_021223526.RAW-01.COVER~4.jpg)

モーターを左右で逆の方向に動かすとヘッドが上下に動く。
例えば、左のモータを反時計まわり、右のモータを時計まわりに動かすと、
ヘッドは上に動く。

![](https://uploader.apps.ikeji.ma/file/78e935f93b42535e18511b642aa06d3f/PXL_20250812_021223526.RAW-01.COVER~5.jpg)

## リンク

- 動画
  - [第一世代](https://x.com/ikeji/status/1926441077013106829)
  - [第二世代](https://x.com/ikeji/status/1931363801653526600)
- 開発ログ
  - [2025W21](https://blog.ikejima.org/weekly/2025/05/26/2025w21.html)
  - [2025W22](https://blog.ikejima.org/weekly/2025/06/03/2025w22.html)
  - [2025W23](https://blog.ikejima.org/weekly/2025/06/10/2025w23.html)
- 紹介された
  - [2025年4-6月の自作ペンプロッタを愛でる会](https://note.com/penplotter/n/n4fdf6959738a#017fe1ae-cd83-49cf-acd3-3303a340d920)

## 免責事項

無保証/MIT License

