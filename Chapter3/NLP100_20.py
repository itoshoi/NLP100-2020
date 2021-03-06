'''
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
'''

import gzip
import json

path = 'jawiki-country.json.gz' 

def load():
    with gzip.open(path, 'rt') as f:
        for l in f:
            data = json.loads(l)
            if data['title'] == 'イギリス':
                return data['text']

if __name__ == "__main__":
    print(load())