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
- view関数login_requirerdのデコレータを付ける
- クラスベースビューには、LoginREquiredMixinを使用する
- view.py　⇒　class ViewB(LoginRequiredMixin, TemplateView):
- ※継承の順番には注意。urlの設定は、通常のクラスベースビューと同じ


