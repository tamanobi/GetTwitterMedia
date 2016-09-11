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
あなたがファボしたら、すぐにこのスクリプトが動作して、画像・動画をローカルストレージに保存します。Twitter Stream APIを使っています。

こいつは、起動したままになるので、screenとかtmuxとかで起動するといいと思います。

## getall_fav_media.py
こいつは、過去のファボを全力で遡って、すべての画像と動画をダウンロードします。
Twitter API制限に引っ掛かりやすいので、デフォルトでは1リクエスト180件/5分で実行します。

sqlite3に保存したtweet idを保持しているので、重複する画像・動画はダウンロードされません。
