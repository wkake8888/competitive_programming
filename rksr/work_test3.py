# 問題3. MVC
# 中古スマホ販売事業を行っている経営者が、中古のSIMフリースマートフォン販売のためのウェブサイトを構築したいと考えている。
# 「経営者が、販売するスマートフォンの在庫の登録ができるようにする」という要件について以下の問に答えよ。
# 3-a. スマートフォンの属性をメーカー(例: Apple, Samsung) / 機種(例: iPhone X) / データ容量 (例128GB) / 発売日 / OSバージョン
# / 色 / 販売価格とした場合のモデルを書け
from django.db import models

class UsedSmartPhone(models.Model):
    maker = models.CharField(max_length=30)
    phone_model = models.CharField(max_length=30)
    data_storage_gb = models.IntegerField()
    release_date = models.DateField()
    os_version = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    price = models.IntegerField()
# ※コードのファイル・手書きの図の写真ファイルなどをアップロードして回答ください
# 3-b. 入力を行うためのワイヤーフレームを提案せよ（手書きでも可）
# ※手書きの図の写真ファイルなどをアップロードして回答ください
# 3-c. 登録の POST をハンドリングするメソッドを実装せよ
# ※テキストエリアにコードをコピー&ペーストしてご回答ください
# 3-d. この要件について依頼者（経営者）に質問するとしたら何を質問するか。最も聞いてみたい質問を３つ挙げよ