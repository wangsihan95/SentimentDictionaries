# Common Russia Emotional Dictionaries 
---
Here are some emotion dictionaries in Russia.
- Includes the Russia section of a multilingual emotion dictionaies (with the format xxx_ru/ch/en are multilingual);
- The first part is the table. The second part is a detailed description of the dictionaries; 
- 12 dictionaries currently available

<br><br>

## Table of Russia dictionaries
---


| Словарь                                 | Год  | Объем | Способ  | Шкала                                                        |      |
| --------------------------------------- | ---- | ----- | ------- | ------------------------------------------------------------ | ---- |
| **ProductSentiRus**                     | 2012 | 5000  | Гибрид. | Нет разделения                                               |      |
| **Словарь Блинова**                     | 2013 | 3839  | Гибрид. | Бинарная шкала {–1, +1}                                      |      |
| **Chen-Skiena_ru**                      | 2014 | 2876  | Автом.  | Бинарная шкала {–1, +1}                                      |      |
| **LinisCrowd**                          | 2016 | 2506  | Ручной  | Дискретная шкала \[–2, 2]:<br> \[–2, –1] – нег., \[1, 2] – поз. |      |
| **Котельников_large**<br> (Kotelnikov)  | 2016 | 3247  | Ручной  | Непрерывная шкала \[–1, 1]: <br>\[–1, 0) – нег., (0, 1] – поз. |      |
| **СловарьТутубалиной**<br> (Tutubalina) | 2016 | 2508  | Ручной  | Бинарная шкала {–1, +1}                                      |      |
| **EmoLex_ru**                           | 2017 | 4750  | Ручной  | Бинарная шкала {–1, +1}                                      |      |
| **RuSentiLex_large**                    | 2017 | 12784 | Ручной  | Бинарная шкала {–1, +1}                                      |      |
| **RuSentiLex_small**                    | 2017 | 8331  | Ручной  | Бинарная шкала {–1, +1}                                      |      |
| **SenticNet_ru**                        | 2018 | 24765 | Автом.  | Непрерывная шкала \[–1, 1]:<br> \[–1, 0) – нег., (0, 1] – поз. |      |
| **SentiRusColl**                        | 2019 | 6577  | Ручной  | Бинарная шкала {–1, +1}                                      |      |
| **Карта слов**<br> (онлайн)             | 2019 | 11324 | Ручной  | Бинарная шкала {–1, +1}                                      |      |
|                                         |      |       |         |                                                              |      |


<br>
<br>





## Introduction
---

Some descriptions are cited from the paper:
>Котельников, Е. В., et al. "Современные словари оценочной лексики для анализа мнений на русском и английском языках (аналитический обзор)." \_Научно-техническая информация. Серия_ 2 (2020): 16-33.

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

### ProductSentiRus
2012
Разработали Илья Четвёркин и Наталья Лукашевич для предметной области товаров (фильмы, книги, игры, цифровые фотокамеры, мобильные телефоны). Сначала было использовано машинное обучение для построения модели на основе множества вручную размеченных слов из отзывов о фильмах и набора статистических и лин- гвистических признаков слов. Затем построенная модель применялась для классификации оценочной лексики в других областях. В результате общий словарь оценочной лексики для всех пяти областей включает 5 000 слов. Слова в словаре отсортированы по мере убывания вероятности их оценочности, но не разделены на позитивные и негативные.
5000
Гибрид.
Нет разделения
[http://panchenko.me/data/snalp/sentiment/ProductSentiRus.txt](http://panchenko.me/data/snalp/sentiment/ProductSentiRus.txt) 
>Chetviorkin I., Loukachevitch N. Extraction of Russian Sentiment Lexicon for Product Meta- Domain // Proceedings of COLING 2012. – Mum- bai, 2012. – P. 593–610.


<br>

### Словарь Блинова
2013
Павел Блинов с соавторами сформировали вручную список из 969 наиболее позитивных и 1 138 наиболее негативных слов из словаря ProductSentiRus, а затем автоматически расширили список синонимами и антонимами из рус- ского Викисловаря ([https://ru.wiktionary.org/wiki](https://ru.wiktionary.org/wiki)).
3839
Гибрид.
Бинарная шкала {–1, +1}
[https://github.com/kotelnikov-ev/BlinovSentimentLexicon](https://github.com/kotelnikov-ev/BlinovSentimentLexicon)
>Blinov P.D., Klekovkina M.V., Kotelni- kov E.V., Pestov O.A. Research of lexical ap- proach and machine learning methods for sentiment analysis // Computational Linguistics and Intellectual Technologies: Papers from the Annual International Conference “Dialogue-2013”. –2013. – Vol. 12(19). – P. 51–61.

<br>

### Chen-Skiena_ru
2014
Автоматически построили словари оценочной лексики для 136 языков (включая русский и английский). На основе тезауру- сов wordnet и wiktionary и с помощью машинного перевода (google translate) был построен много- язычный семантический граф, связывающий слова на разных языках. Затем, отталкиваясь от англоязычно- го словаря бинга лью, были сформированы оценоч- ные словари для других языков на основе алгоритма распространения разметки. Варианты для английского и русского языков далее называются chen-skiena_en и chen-skiena_ru.
2876
Автом.
Бинарная шкала {–1, +1}
[https://sites.google.com/site/datascienceslab/projects/multilingualsentiment](https://sites.google.com/site/datascienceslab/projects/multilingualsentiment)
>Chen Y., Skiena S. Building Sentiment Lexicons for All Major Languages // Proceedings of the 52nd Annual Meeting of the Association for Computa- tional Linguistics. – Baltimore, 2014. – P. 383–389.

<br>

### LinisCrowd
2016
Олеся Кольцова с соавторами создавали свой словарь при помощи краудсорсинга. Сначала они отобрали 7 546 слов на основе списка высокочастотных прилагательных, словаря Productcenters, толкового словаря и перевода англоязычного словаря оценочной лексики SentiStrength. Затем не менее трех аннотаторов каждому слову присваивали оценки от –2 до +2. В настоящем исследовании позитивными и негативными считаются такие слова, которые получили большинство оценок соответст- вующей тональности.
2506
Ручной
Дискретная шкала \[–2, 2]: \[–2, –1] – нег., \[1, 2] – поз.
[http://www.linis-crowd.org](http://www.linis-crowd.org) 

>Koltsova O.Yu., Alexeeva S.V., Kolcov S.N. An Opinion Word Lexicon and a Training Dataset for Russian Sentiment Analysis of Social Media // Computational Linguistics and Intellectual Tech- nologies: Papers from the Annual International Con- ference “Dialogue-2016”. –2016. – Vol. 15(22). – P. 277–287.

<br>

### Котельников_large(Словарь Котельникова)
2016
Евгений Котельников с соавторами сначала автоматически отобрали по 10 000 слов-кандидатов для каждой из пяти предметных областей (отзывы о ресторанах, автомобилях, фильмах, книгах и камерах), четыре аннотатора оценили каждое слово как позитивное, негативное, нейтральное или противоречивое, затем было создано два объединенных по предметным об- ластям словаря: в первый вошли слова, относительно тональности которых были согласны три аннотатора из четырех (Kotelnikov_large), во второй – слова, от- носительно тональности которых согласны все анно- таторы (Kotelnikov_small).
3247
Ручной
Бинарная шкала {–1, +1}
[https://github.com/kotelnikov-ev](https://github.com/kotelnikov-ev)
>Kotelnikov E., Bushmeleva N., Razova E., Peskisheva T., Pletneva M. Manually Created Sentiment Lexicons: Research and Development // Computational Linguistics and Intellectual Tech- nologies: Papers from the Annual International Con- ference “Dialogue-2016”. – 2016. – Vol. 15(22). – P. 300–314.

<br>

### Словарь Тутубалиной
2016
Елена Тутубалина в своей диссертации создала вручную словарь на основе строго позитивных и негативных отзывов пользователей об автомобилях (в отзывах учитывались только разделы преимуществ и недостатков). Словарь был расширен за счет добавления синонимов.
2508
Ручной
Бинарная шкала {–1, +1}
[https://www.ispras.ru/dcouncil/docs/diss/2016/tutubalina/dissertacija-tutubalina.pdf](https://www.ispras.ru/dcouncil/docs/diss/2016/tutubalina/dissertacija-tutubalina.pdf)
>Тутубалина Е.В. Методы извлечения и резю- мирования критических отзывов пользователей о продукции: дис. ... канд. физ.-мат.. наук. – М.: ИСП РАН, 2016. – 145 с.
<br>

### EmoLex_ru
2017
EmoLex (NRC Emotion Lexicon) – словарь составлен Саифом Мохаммадом (Saif Mohammad) и Питером Тёрни (Peter Turney) с помощью краудсорсинга. Словарь EmoLex содержит слова, соотнесенные с позитивной и негативной тональностью, а также с эмоциями «гнев», «предвкушение», «отвращение», «страх», «радость», «грусть», «удивление» и «доверие». 
В ноябре 2017 г. словарь был переведен на более чем 100 языков (в том числе, на русский) с помощью Google Translate. Для русского языка были отобраны слова и словосочетания, имеющие позитивную или негативную тональность. Вариант для русского языка далее называется Emolex_ru.
4 750
Ручной
Бинарная шкала {–1, +1}
[https://www2.imm.dtu.dk/pubdb/pubs/6010-full.html](https://www2.imm.dtu.dk/pubdb/pubs/6010-full.html)
[https://osf.io/download/zexfc](https://osf.io/download/zexfc)
>Nielsen F. A new ANEW: Evaluation of a word list for sentiment analysis in microblogs // Proceedings of the ESWC2011 Workshop on Making Sense of Microposts: Big things come in small packages, Heraklion. – 2012. – P. 93–98.

<br>

### Sentiment140-Lexicon
2013
Sentiment140-Lexicon создан на основе одноименного корпуса, включающего 1,6 млн твитов с позитивными и негативными хештегами. Слова размечались с использованием метода поточечной взаимной информации (PMI).
523092
Автом.
Непрерывная шкала \[–6, 8]: \[–6, 0) – нег., (0, 8] – поз.
[https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.html](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.html)
>Mohammad S.M., Turney D.P. Crowdsourcing a word-emotion association lexicon // Computational Intelligence. – 2013. – Vol. 29(3). – P. 436–465.

<br>

### RuSentiLex_large
2017
Наталья Лукашевич и Анатолий Левчик создали словарь RuSentiLex, в котором для каждого слова указывается тональность (позитивная, негативная, нейтральная) и источник (мнение, факт, чувство). Сначала были сгенерированы списки оце- ночных слов на основе тезауруса РуТез, существую- щих словарей оценочной лексики, новостных статей и Twitter, затем лингвисты анализировали получен- ные списки для формирования итогового словаря. Словарь содержит более десяти тысяч слов и выра- жений, выражающих оценку тональности. В работе использовалась версия словаря 2017 г. и только слова и сочетания с позитивной или негативной тональностью. Исследовалось две версии – *RuSentiLex_large*, включающая все позитивные и негативные элементы, и RuSentiLex_small, включающая позитивные и негативные элементы, для которых источником является мнение.
12784
Ручной
Бинарная шкала {–1, +1}
[https://www.labinform.ru/pub/rusentilex](https://www.labinform.ru/pub/rusentilex)
>Loukachevitch N., Levchik A. Creating a General Russian Sentiment Lexicon // Proceedings of Language Resources and Evaluation Conference LREC-2016. – 2016. – P. 1171–1176.

<br>

### RuSentiLex_small
2017
Наталья Лукашевич и Анатолий Левчик создали словарь RuSentiLex, в котором для каждого слова указывается тональность (позитивная, негативная, нейтральная) и источник (мнение, факт, чувство). Сначала были сгенерированы списки оце- ночных слов на основе тезауруса РуТез, существую- щих словарей оценочной лексики, новостных статей и Twitter, затем лингвисты анализировали получен- ные списки для формирования итогового словаря. Словарь содержит более десяти тысяч слов и выра- жений, выражающих оценку тональности. В работе использовалась версия словаря 2017 г. и только слова и сочетания с позитивной или негативной тональностью. Исследовалось две версии – RuSentiLex_large, включающая все позитивные и негативные элементы, и *RuSentiLex_small*, включающая позитивные и негативные элементы, для которых источником является мнение.
8331
Ручной
Бинарная шкала {–1, +1}
[https://www.labinform.ru/pub/rusentilex](https://www.labinform.ru/pub/rusentilex)
>Loukachevitch N., Levchik A. Creating a General Russian Sentiment Lexicon // Proceedings of Language Resources and Evaluation Conference LREC-2016. – 2016. – P. 1171–1176.

<br>

### SenticNet_ru
2018
Это проект по анализу мнений на уровне понятий, нача- тый в 2009 г. В mit media laboratory. Для построе- ния словаря оценочной лексики сначала был сфор- мирован граф понятий с использованием нейронных сетей долгой краткосрочной памяти (long short-term memory, lstm), обучавшихся на основе распреде- ленных представлений слов. Затем для разметки понятий по тональности применялось специальное векторное пространство affectivespace. В нашей статье используется версия словаря senticnet 5 (да- лее в статье этот словарь называется senticnet_en). В рамках senticnet имеется проект babelsenticnet, содержащий словари для 40 языков, в том числе русского. Далее в нашей статье словарь для русского языка обозначается senticnet_ru.
24 765
Автом.
Непрерывная шкала \[–1, 1]:  \[–1, 0) – нег., (0, 1] – поз.
[https://sentic.net/downloads](https://sentic.net/downloads) 
>Cambria E., Poria S., Hazarika D., Kwok K . SenticNet 5: Discovering conceptual primitives for sentiment analysis by means of context embed- dings // Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence (AAAI-18). – 2018. – P. 1795–1802.

<br>

### SentiRusColl
2019
Это оценочный словарь словосочетаний. Для его создания использовался корпус отзывов по десяти предметным областям (книги, фильмы, музыка, автомобили, компьютеры, бытовая техника, телефоны, банки, отели, рестора- ны), из него автоматически отбирались словосочета- ния-кандидаты, которые далее размечались тремя аннотаторами. В словарь внесены словосочетания, получившие большинство голосов. Для нашего ис- следования использовался вариант словаря SentiRus- Coll со стоп-словами, содержащий предлоги и союзы.
6577
Ручной
Бинарная шкала {–1, +1}
https://github.com/kotel-nikov-ev/SentiRusColl 
>Kotelnikova A.V., Kotelnikov E.V. Senti- RusColl: Russian Collocation Lexicon for Sentiment Analysis // Artificial Intelligence and Natural Lan- guage Conference (AINL). Communications in Computer and Information Science (November 20– 22, 2019. Tartu, Estonia). –Cham: Springer, 2019. – Vol. 1119. – P. 18–32.

<br>

### Карта слов
2019
Это онлайн-карта слов и выражений русского языка. Оценочный словарь, разработанный в рамках этого проекта, содержит слова русского языка, снабжённые метками тональности (позитивная, негативная или нейтральная) и силы эмоционально-оценочного заряда. При создании словаря использовался краудсорсинг: в процессе разметки пользователю предлагалось оценить то или иное слово как нейтральное, позитивное, негативное или ответить «не знаю». 
11324
Ручной
Бинарная шкала {–1, +1}
https://kartaslov.ru 

>Кулагин Д.И. Карта слов: переосмысление подхода к составлению онлайн-словарей в по- стмобильную эру // Международная конференция «Диалог 2017» – Компьютерная лингвистика и интеллектуальные технологии (Москва, 31 мая – 3 июня 2017 г.). – URL: http://www.dialog-21.ru/ media/3974/kulagindi.pdf (дата обращения: 01.08.2020).

