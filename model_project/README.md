## 参考サイト
https://qiita.com/dai-takahashi/items/5042db0792c9f7d01c1e

## 外部Key設定
- 外部keyに対してのみForeignKey(親model名)設定を行う　 </br>
　club = models.ForeignKey(親モデル, on_delete=models.CASCADE)
- foreignkeyの項目には、親が持っているidが付与される
- 親モデルには、一意な名称を戻り値で返すように設定しておく    
```python
def ＿＿str＿＿(self):
   　return [一意な名称] 
```
