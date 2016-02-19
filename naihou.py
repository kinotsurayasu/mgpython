# coding: shift_jis

#内包表記について書いてみました。速くて、1文で読みやすいとのこと。オライリーの「集合知プログラミング」によく出てきます。




#リストの定義です
list={'yasuhiro':{'nike':5,'adidas':2,'puma':4},'takuro':{'adidas':5,'nike':4,'asics':1}}



#リスト内包です。辞書型で共通するキーを引っ張ってきます
y=[x for x in list['yasuhiro'] if x in list['takuro']]
print y



#共通しているキーの平均点をリスト型で出します
z=[(x,(list['yasuhiro'][x]+list['takuro'][x])/2.0) for x in list['yasuhiro'] if x in list['takuro']]
print z



#共通しているキーの平均点を辞書型で出します
si={}
z=dict([(x,(list['yasuhiro'][x]+list['takuro'][x])/2.0) for x in list['yasuhiro'] if x in list['takuro']])
print z



#自分以外の人の名前を抽出する関数を作りました。これで、自分以外の人について色々計算ができます。

si={'yasuhiro':{'nike':5,'adidas':2,'puma':4},'takuro':{'adidas':5,'nike':4,'asics':1},'tomoko':{'nike':4,'puma':5}}

def test(dic,person):
    x=[item for item in dic if item!=person]
    print x

test(si,'yasuhiro')



