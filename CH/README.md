# Common Chinese Emotional Dictionaries 
---
Here are some emotion dictionaries in Chinese.
- Multilingual dictionaries are not currently included and will be added later (with the format xxx_ru/ch/en are multilingual);
- The first part is the table. The second part is a detailed description of the dictionaries; 
- 8 dictionaries currently available



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
<br>

### 知网词典 HowNet
2003 (обновляется)<br>
Позитивные эмоциональные слова(836); Позитивные оценочные слова(3730); Негативные эмоциональные слова(1254); Негативные оценочные слова(3116)<br>
8936<br>
Ручной<br>
Бинарная шкала {–1, +1}<br>
[https://openhownet.thunlp.org/](https://openhownet.thunlp.org/)<br>
[Download from github](https://github.com/ZaneMuir/DLUT-Emotionontology/blob/master/%E6%83%85%E6%84%9F%E8%AF%8D%E6%B1%87/%E6%83%85%E6%84%9F%E8%AF%8D%E6%B1%87%E6%9C%AC%E4%BD%93.zip)<br>
>   None


<br>

### 大连理工大学中文情感词汇本体库DLUT<br>

(Dalian University of Technology Chinese Emotional Vocabulary Ontology Library)<br>

(База данных онтологии китайской эмоциональной лексики)<br>

2008<br>
Полярность делится на 4 категории. Конкретные эмоции делятся на 7 основных категорий и 21 второстепенную категорию. Эмоциональная интенсивность делится на 5 категорий 1,3,5,7,9, где 9 означает наибольшую интенсивность, а 1 - наименьшую.<br>
27466<br>
Ручной<br>
Бинарная шкала {0,1,2,3}: 0-нейтральное слово, 1-Поз., 2-Нег., 3-Поз. и Нег.<br>
[https://github.com/ZaneMuir/DLUT-Emotionontology](https://github.com/ZaneMuir/DLUT-Emotionontology) <br>
> 陈建美. 中文情感词汇本体的构建及其应用. Diss. 大连理工大学.

<br>

### BosonNLP
2014<br>
Отрицательные числа представляют отрицательные слова, а неотрицательные числа - положительные слова, и степень положительности или отрицательности может быть отражена величиной значения.<br>
114767<br>
Автом.<br>
Непрерывная шкала \[-7; 7]:  \[-7, 0] – нег., (0, 7] – поз.<br>
[http://bosonnlp.com/](http://bosonnlp.com/)<br>
[https://github.com/bosondata/bosonnlp.py](https://github.com/bosondata/bosonnlp.py)<br>
>Min, Kerui, et al. "BosonNLP: An ensemble approach for word segmentation and POS tagging." Natural language processing and chinese computing. Springer, Cham, 2015. 520-526.

<br>

### 台湾大学NTSUSD
2010<br>
Поз. (2810); Нег. (8276)<br>
11086<br>
Ручной<br>
Бинарная шкала {–1, +1}<br>
[http://nlg.csie.ntu.edu.tw/nlpresource/NTUSD-Fin/](http://nlg.csie.ntu.edu.tw/nlpresource/NTUSD-Fin/) <br>
>数据堂. "台湾大学 NTUSD-简体中文情感极性词典." 2013-03-05]. http://www. datatang. com/data/11837.(Data Tang. National Taiwan University-The Polarity of Simplified Chinese Emotional Dictionary.

<br>

### 清华大学李军中文褒贬义词典LiJun(Китайский словарь положительных инегативных определений Университета Цинхуа)
Unknown<br>
Поз. (5568); Нег. (4470)<br>
10038<br>
Ручной<br>
Бинарная шкала {–1, +1}<br>
[Download from github](https://github.com/Shimon-Guo/chinese_sentiment_dictionary/tree/master/file/%E6%83%85%E6%84%9F%E8%AF%8D%E5%85%B8/%E6%B8%85%E5%8D%8E%E5%A4%A7%E5%AD%A6%E6%9D%8E%E5%86%9B%E4%B8%AD%E6%96%87%E8%A4%92%E8%B4%AC%E4%B9%89%E8%AF%8D%E5%85%B8)<br>
>None by 清华大学李军


<br>

### 汉语情感词极值表Polarity Table(Список полярности китайских эмоциональных слов)
2017<br>
Этот список слов включает 23419 китайских слов эмоций. Формат: "слово \t полярности".<br>
23419<br>
Ручной<br>
Непрерывная шкала \[-4; 5]: \[-4, 0] – нег., (0, 5] – поз.<br>
[Github](https://github.com/ppzhenghua/SentimentAnalysisDictionary/tree/main/%E6%B1%89%E8%AF%AD%E6%83%85%E6%84%9F%E8%AF%8D%E6%9E%81%E5%80%BC%E8%A1%A8)<br>
> None by 清华大学中文系 原博

<br>

### 否定词典Negative Dictionary(Словарь отрицательных слов)
Unknown<br>
Распространенные слова отрицания в китайском языке.<br>
58<br>
Ручной<br>
Только нег.<br>
[Github](https://github.com/ppzhenghua/SentimentAnalysisDictionary/tree/main/%E5%90%A6%E5%AE%9A%E8%AF%8D%E5%85%B8)<br>
> None

<br>

### 褒贬词及其近义词PNS

(Positive and negative words and their close synonyms)<br>

(Список китайских положи-тельных иинегативных слов и их синонимов)<br>

Unknown<br>
Поз. (728); Нег. (933); Поз. и Нег. (3)<br>
1664<br>
Ручной<br>
Бинарная шкала {1,2,3}<br>
[Github](https://github.com/ppzhenghua/SentimentAnalysisDictionary/tree/main/%E8%A4%92%E8%B4%AC%E8%AF%8D%E5%8F%8A%E5%85%B6%E8%BF%91%E4%B9%89%E8%AF%8D)<br>
>None

