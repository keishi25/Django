## 参考サイト
https://qiita.com/dai-takahashi/items/5042db0792c9f7d01c1e

## 外部Key設定
1. 外部keyに対してのみForeignKey(親model名)設定を行う
```python
　club = models.ForeignKey(親モデル, on_delete=models.CASCADE)
```
2. foreignkeyの項目には、親が持っているidが付与される
3. 親モデルには、一意な名称を戻り値で返すように設定しておく    
```python
def ＿＿str＿＿(self):
   　return [一意な名称] 
```
