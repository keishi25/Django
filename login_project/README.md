# ログインフォーム作成
# 参考サイト
https://it-engineer-lab.com/archives/544

## 解説
### 認証汎用ビューがある項目</br>
- ログイン
- ログアウト
- パスワード管理

### 自作が必要な項目</br>
- サインアップ

## 初期条件
- アプリ-myapp　
- DB-Postgresql　
※上記設定済み

## 手順
### 1. LOGIN_REDIRECT_URL の設定(settings.py)
ログイン後にリダイレクトされるページのURLを設定する
### 2. ログイン,ログアウトtemplate設定
- ログイン画面: templates/registration/login.html
- ログアウト画面: templates/registration/logged_out.html
※認証ビューのデフォルト参照先は、template/registration
### 3. サインアップ実装
- accountアプリ作成
- urls設定
- サインアップビュー作成
- サインアップtemplate作成(templates/accounts/signup.html)
- ログイン制限 ログイン下ユーザだけ閲覧可能になる
### 4. ログイン制限をする
- LoginREquiredMixinを継承するだけ
- view.py　⇒　class クラス名(LoginRequiredMixin, TemplateView):
- ※継承の順番には注意。urlの設定は、通常のクラスベースビューと同じ

## その他
django.contrib.auth.urlsをインポートするだけで、
templates/registration/以下に配置されたlogin.htmlおよびlogged_out.htmlという名前のテンプレートが、それぞれ上記URLにおいて自動的に表示される。
myapp/urls.pyで、loginおよびlogoutに関するビューを記述する必要がなくなる

### a.ログイン情報の取得
- self.request.userで取得可能

### b.サインイン情報の変更
- forms.pyでUserCreationFormを継承。fieldsに追加したいフォームの項目を追加する
