# Get Media Favorited Your Media To Twitter
Twitterでファボしたタイミングで自動的にローカルストレージに画像・動画を保存できるスクリプト

Twitterに眠るあなたのお気に入り画像と動画たち。やつらをローカルストレージに落としたい。そういうときにこのスクリプトを使います。

## Requirements
* Python2.7
* Twitterアプリケーション登録
* `pip install twitter`
* `sqlite3`: tweetの重複を検出するために使っています

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
こいつは、過去のいいねを全力で遡ってすべての画像と動画をダウンロードします。
Twitter API制限に引っ掛かりやすいので、デフォルトでは180件/5分で実行します。
