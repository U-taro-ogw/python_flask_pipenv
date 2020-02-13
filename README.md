# pythonでAPIを作成する雛形

### 環境

- python 3.7
- flask
- elasticsearch
- redis

### 動作確認

1. コンテナを立ち上げる  
`$ docker-compose up -d`

2. curlを投げる  
`$ curl -X GET http://localhost:5000`  
=> Hello My App  

    `$ curl -X GET http://localhost:5000/redis_hits`  
    => Hello World! I have been seen b'1' times.

    `$ curl -X GET http://localhost:5000/aozora_books`  
    => {"key": "value"}

### テスト
mambaを使用しています。  

テストファイルは  
`/app/spec/`  
配下に配置

テストの実行コマンド  
`$ docker-compose exec flask_app pipenv run mamba`


### lint
flake8を使用しています。

flake8の実行コマンド  
`$ docker-compose exec flask_app pipenv run flake8`