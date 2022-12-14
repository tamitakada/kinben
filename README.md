# きんべん（KINBEN）　漢字練習アプリ

きんべんは、Python・Tkinterで作られた簡単な漢字練習アプリです。漢字の問題が出題されますが、アプリにはノートパッドが付いていないので、別に紙と鉛筆を揃えて勉強するという形になります。漢字の問題は付属のデータベースから出題されますが、アプリの中で自分から問題を加えたり、すでにデータベースの中にある問題を変えることも可能です。

Kinben is a simple kanji practice app made with Python/Tkinter. Since there is no built-in notepad, the app is meant to be used as a random question generator that you can use with pencil and paper to wrte down your answers. You can change add to/change the data in the attached kanji database from the app as well.

## インストールの仕方 (How to Install)
1. コンピューターの端末を開き、`git clone git@github.com:tamitakada/kinben.git`を入力  
   Open your computer terminal and enter the command `git clone git@github.com:tamitakada/kinben.git`.
2. `cd kinben; pip3 install requirements.txt`を入力  
   Enter the command `cd kinben; pip3 install requirements.txt`.
2. `python3 run.py`を入力し、アプリを開く  
   Enter `python3 run.py` to run the app.

## 漢字練習機能の使い方
1. 端末を開き、`cd kinben; python3 run.py`を入力してアプリを開く。
2. 「練習を始める」ボタンを押し、漢字問題を解き始める。
3. 右上に設置された青い丸のボタンを押し、答え合わせをする。
4. 正解・不正解を記録するため、青い丸・黄色いバツを押す。
5. 好きなだけ問題を解いてから、右上に設置された漢字練習終了ボタンを押す。
6. 右上の白いボタンを押し、メニューに戻る。

## データベース変更の仕方
1. 端末を開き、`cd kinben; python3 run.py`を入力してアプリを開く。
2. 「データの変更」ボタンを押す。
3. 新しい単語追加の場合、右上に設置してある「+」のボタンを押す。すでにデータベースの中にある単語のデータ変更の場合、サーチバーを使って単語を検索し、単語の右に設置してある白い矢印を押す。
4. 単語・読み・例文の項目を自由に変更し、「保存」ボタンを押す。新しい単語追加のときに保存失敗が生じれば、すでにその単語がデータベースの中に存在している可能性がある。
5. 左上の白いボタンを押し、漢字検索場面に戻る。

## 使用したソフトウェア等
* アプリで使用されている背景は、すべて[Haikei](https://haikei.app/)を使って作成されています。
* アプリでは、大平義道様の[ZEN丸ゴシック体](https://fonts.google.com/specimen/Zen+Maru+Gothic?query=zen+)と井上デザインの[id-壊雲体](http://idfont.jp/infos_mb.html)を使わせていただきました。
