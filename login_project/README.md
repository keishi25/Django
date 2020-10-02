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
1. LOGIN_REDIRECT_URL の設定(settings.py)
ログイン後にリダイレクトされるページのURLを設定する
2. ログイン,ログアウトtemplate設定
- ログイン画面: templates/registration/login.html
- ログアウト画面: templates/registration/logged_out.html
※認証ビューのデフォルト参照先は、template/registration
3. サインアップ実装
3-1. accountアプリ作成
3-2. urls設定
3-3. サインアップビュー作成
3-4. サインアップtemplate作成(templates/accounts/signup.html)
4.ログイン制限 ログイン下ユーザだけ閲覧可能になる
-  viewに@login_requiredのデコレータを付ける 
※クラスベースビューには、LoginREquiredMixinを使用する

