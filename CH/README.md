# Common Chinese Emotional Dictionaries 
---
Here are some emotion dictionaries in Chinese.
- Multilingual dictionaries are not currently included and will be added later (with the format xxx_ru/ch/en are multilingual);
- The first part is the table. The second part is a detailed description of the dictionaries; 
- 8 dictionaries currently available

<br><br>

## Table of Chinese dictionaries
---


| **Словарь**                                                  | Год  | Объем  | Способ | Шкала                                                        |      |
| ------------------------------------------------------------ | ---- | ------ | ------ | ------------------------------------------------------------ | ---- |
| 知网词典 HowNet                                              | 2003 | 8936   | Ручной | Бинарная шкала {–1, +1}                                      |      |
| 大连理工大学中文情感词汇本体库DLUT<br>(База данных онтологии китайской эмоциональной лексики) | 2008 | 27466  | Ручной | Бинарная шкала {0,1,2,3}:<br>0-нейтральное слово, 1-Поз., 2-Нег., 3-Поз. и Нег. |      |
| BosonNLP                                                     | 2014 | 114767 | Автом. | Непрерывная шкала \[-7; 7]: <br>\[-7, 0] – нег., (0, 7] – поз. |      |
| 台湾大学NTSUSD                                               | 2010 | 11086  | Ручной | Бинарная шкала {–1, +1}                                      |      |
| 清华大学李军中文褒贬义词典LiJun<br>(Китайский словарь положительных инегативных определений Университета Цинхуа) | /    | 10038  | Ручной | Бинарная шкала {–1, +1}                                      |      |
| 汉语情感词极值表Polarity Table<br>(Список полярности китайских эмоциональных слов) | 2017 | 23419  | Ручной | Непрерывная шкала \[-4; 5]: <br>\[-4, 0] – нег., (0, 5] – поз. |      |
| 否定词典Negative Dictionary<br>(Словарь отрицательных слов)  | /    | 58     | Ручной | Только нег.                                                  |      |
| 褒贬词及其近义词PNS <br>(Positive and negative words and their close synonyms)) | /    | 1664   | Ручной | Бинарная шкала {1,2,3}                                       |      |

<br>
<br>

## Introduction
---

The format as follows:
- Name
- Year
- Introduction
- Size
- Collection method
- Marking method
- URL
- Citation
---

### 知网词典 HowNet
2003 (обновляется)
Позитивные эмоциональные слова(836); Позитивные оценочные слова(3730); Негативные эмоциональные слова(1254); Негативные оценочные слова(3116)
8936
Ручной
Бинарная шкала {–1, +1}
[https://openhownet.thunlp.org/](https://openhownet.thunlp.org/)
[Download from github](https://github.com/ZaneMuir/DLUT-Emotionontology/blob/master/%E6%83%85%E6%84%9F%E8%AF%8D%E6%B1%87/%E6%83%85%E6%84%9F%E8%AF%8D%E6%B1%87%E6%9C%AC%E4%BD%93.zip)
>   Later


<br>

### 大连理工大学中文情感词汇本体库DLUT

(Dalian University of Technology Chinese Emotional Vocabulary Ontology Library)

(База данных онтологии китайской эмоциональной лексики)

2008
Полярность делится на 4 категории. Конкретные эмоции делятся на 7 основных категорий и 21 второстепенную категорию. Эмоциональная интенсивность делится на 5 категорий 1,3,5,7,9, где 9 означает наибольшую интенсивность, а 1 - наименьшую.
27466
Ручной
Бинарная шкала {0,1,2,3}: 0-нейтральное слово, 1-Поз., 2-Нег., 3-Поз. и Нег.
[https://github.com/ZaneMuir/DLUT-Emotionontology](https://github.com/ZaneMuir/DLUT-Emotionontology) 
>Later

<br>

### BosonNLP
2014
Отрицательные числа представляют отрицательные слова, а неотрицательные числа - положительные слова, и степень положительности или отрицательности может быть отражена величиной значения.
114767
Автом.
Непрерывная шкала \[-7; 7]:  \[-7, 0] – нег., (0, 7] – поз.
[http://bosonnlp.com/](http://bosonnlp.com/)
[https://github.com/bosondata/bosonnlp.py](https://github.com/bosondata/bosonnlp.py)
>Later

<br>

### 台湾大学NTSUSD
2010
Поз. (2810); Нег. (8276)
11086
Ручной
Бинарная шкала {–1, +1}
[http://nlg.csie.ntu.edu.tw/nlpresource/NTUSD-Fin/](http://nlg.csie.ntu.edu.tw/nlpresource/NTUSD-Fin/) 
>Later

<br>

### 清华大学李军中文褒贬义词典LiJun(Китайский словарь положительных инегативных определений Университета Цинхуа)

Unknown
Поз. (5568); Нег. (4470)
10038
Ручной
Бинарная шкала {–1, +1}
[Download from github](https://github.com/Shimon-Guo/chinese_sentiment_dictionary/tree/master/file/%E6%83%85%E6%84%9F%E8%AF%8D%E5%85%B8/%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6%E6%9D%8E%E5%86%9B%E4%B8%AD%E6%96%87%E8%A4%92%E8%B4%AC%E4%B9%89%E8%AF%8D%E5%85%B8)
>Later


<br>

### 汉语情感词极值表Polarity Table(Список полярности китайских эмоциональных слов)

2017
Этот список слов включает 23419 китайских слов эмоций. Формат: "слово \t полярности".
23419
Ручной
Непрерывная шкала \[-4; 5]: \[-4, 0] – нег., (0, 5] – поз.
[Github](https://github.com/ppzhenghua/SentimentAnalysisDictionary/tree/main/%E6%B1%89%E8%AF%AD%E6%83%85%E6%84%9F%E8%AF%8D%E6%9E%81%E5%80%BC%E8%A1%A8)
> Later

<br>

### 否定词典Negative Dictionary(Словарь отрицательных слов)

Unknown
Распространенные слова отрицания в китайском языке.
58
Ручной
Только нег.
[Github](https://github.com/ppzhenghua/SentimentAnalysisDictionary/tree/main/%E5%90%A6%E5%AE%9A%E8%AF%8D%E5%85%B8)
> None

<br>

### 褒贬词及其近义词PNS

(Positive and negative words and their close synonyms)

(Список китайских положи-тельных иинегативных слов и их синонимов)

Unknown
Поз. (728); Нег. (933); Поз. и Нег. (3)
1664
Ручной
Бинарная шкала {1,2,3}
[Github](https://github.com/ppzhenghua/SentimentAnalysisDictionary/tree/main/%E8%A4%92%E8%B4%AC%E8%AF%8D%E5%8F%8A%E5%85%B6%E8%BF%91%E4%B9%89%E8%AF%8D)
>Later

