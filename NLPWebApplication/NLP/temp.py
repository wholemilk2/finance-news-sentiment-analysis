# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## dosyayı okuyup bir değişkene atalım. 
#Bu değişkenin tipi, karakter dizisi (string) sınıfından (class str) olacak.
import pandas as pd

data = pd.read_csv(r"h.csv",encoding = "utf-8" )
data = pd.concat([data.strBaslik])
data=data.to_string()

print('"data" değişkeninin tipi:', type(data), '\n')

print('Haberlerin boşluklar dahil uzunluğu:', len(data), 'karakter.\n\n')

# noktalama işaretlerini ve sayıları temizle
from string import punctuation, digits

converter = str.maketrans('', '', punctuation)
data = data.translate(converter)
converter = str.maketrans('', '', digits)
data = data.translate(converter)

#küçük-büyük harf farkı
data = data.lower()

#Bag of words (her kelimeyi ve bu kelimenin metinde kaç kez geçtiği)
words = data.split()
print(len(words))

from collections import Counter

# Kelime çantasını hazırlamak bir satır
countsOfWords = Counter(words)

print(type(countsOfWords), '\n')

# En sık kullanılan 10 kelimeye
# tek bir fonksiyon ile bakabiliyoruz.
for word in countsOfWords.most_common(10):
    print(word)
    
#kök çıkarma (stemming) işini Türkçe için de yaoiyor 
from snowballstemmer import stemmer

kokbul1 = stemmer('turkish')

print(kokbul1.stemWords('arttı art'.split()))

from sys import path

# Python'a indirdiğimiz paketi tanıtalım
path.append('/Users/zisanyalcinkaya/turkish-stemmer-python')

from TurkishStemmer import TurkishStemmer

kokbul2 = TurkishStemmer()
print(kokbul2.stem('arttı art'.split()))
    
print('\n\nMetinde "ADEL" kelimesi', countsOfWords['adel'], 'kez geçiyor.')
