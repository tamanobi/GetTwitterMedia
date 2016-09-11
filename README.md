# Get Media Favorited From Twitter
Twitterでファボしたタイミングで自動的にローカルストレージに画像・動画を保存できるスクリプト

Twitterに眠るあなたのお気に入り画像と動画たち。やつらをローカルストレージに落としたい。そういうときにこのスクリプトを使います。

## Requirements
* Python2.7
* `pip install twitter`
* `sqlite3`: tweetの重複を検出するために使っています
* Twitterアプリケーション登録

## token.py
Twitterアプリケーションに登録したら、このスクリプトに記述します。
* CONSUMER_KEY
* CONSUMER_SECRET
* ACCESS_TOKEN
* ACCESS_TOKEN_SECRET

## get_twitter_fav_media.py
このスクリプトを動かしておけば、あなたがファボしたことを検知して、ツイートに含まれる画像・動画をストレージに保存します。
Twitter Stream APIを使っています。

こいつは、起動したままになるので、screenとかtmuxとかで起動するといいと思います。

## getall_fav_media.py
上のスクリプトは、起動してからのファボにしか適用されません。
あなたが昔大切に集めた、ファボの数々はこのスクリプトでストレージに保存できます。

このスクリプトを起動すると、過去のファボを遡って画像・動画をダウンロードします（API制限の事情で、すべてダウンロードできるとは限りません）。
短時間で終わらせたいと思いますが、Twitter API制限に引っ掛かりやすいので、1リクエスト180件取得/5分で実行します。

sqlite3に保存したtweet idを保持しているので、複数回起動しても重複する画像・動画はダウンロードされません。
