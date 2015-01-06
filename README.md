### これはなに？

[Google App Engine](https://cloud.google.com/appengine/) で [cron](https://cloud.google.com/appengine/docs/python/config/cron) を動かします。

### デプロイ

```
appcfg.py update . --oauth2 -A airy-highlander-792
```

airy-highlander-792 というのは app engine のプロジェクト ID です。
下記シェルスクリプトで上記コマンドを実行します。

```
$ ./deploy.sh
```

### 登録済みの cron

#### Evernote

1日1回 Evernote にメールを送ってノートを作成します。日記用。

