### これはなに？

[Google App Engine](https://cloud.google.com/appengine/) で [cron](https://cloud.google.com/appengine/docs/python/config/cron) を動かします。

### デプロイ

```
gcloud app deploy [DEPLOYABLES] --project airy-highlander-792
```

DEPLOYABLES には yaml ファイルを指定します。省略した場合は app.yaml になります。複数指定可能です。
airy-highlander-792 というのは app engine のプロジェクト ID です。
下記シェルスクリプトで上記コマンドを実行します。

```
$ ./deploy.sh [DEPLOYABLES]
```

### 登録済みの cron

#### Evernote

1日1回 Evernote にメールを送ってノートを作成します。日記用。

