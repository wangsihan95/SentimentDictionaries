# Common English Emotional Dictionaries 
---
Here are some emotion dictionaries in English.
- Includes the English section of a multilingual emotion dictionaies (with the format xxx_ru/ch/en are multilingual);
- The first part is the table. The second part is a detailed description of the dictionaries; 
- 20 dictionaries currently available

<br>

## Table of English dictionaries
---


| Словарь                  | Год  | Объем  | Способ  | Шкала                                                                          |     |
| ------------------------ | ---- | ------ | ------- | ------------------------------------------------------------------------------ | --- |
| **ANEW**                 | 1999 | 765    | Ручной  | Непрерывная шкала \[1; 9]: <br> \[1, 4] – нег., \[6, 9] – поз.                 |     |
| **Словарь Бинга Лью**    | 2004 | 6776   | Автом.  | Бинарная шкала {–1, +1}                                                        |     |
| **MPQA**                 | 2005 | 6450   | Ручной  | Бинарная шкала {–1, +1}                                                        |     |
| **SO-CAL**               | 2007 | 6004   | Ручной  | Непрерывная шкала \[–1, 1]: <br>\[–1, 0) – нег., (0, 1] – поз.                 |     |
| **SentiWordNet**         | 2010 | 32902  | Автом.  | Непрерывная шкала \[–1, 1]: <br>\[–1, 0) – нег., (0, 1] – поз.                 |     |
| **EmoLex_en**            | 2011 | 5555   | Ручной  | Бинарная шкала {–1, +1}                                                        |     |
| **AFINN**                | 2017 | 2474   | Ручной  | Дискретная шкала \[–5, 5]:<br> \[–5, –1] – нег., \[1, 5] – поз.                |     |
| **Sentiment140-Lexicon** | 2013 | 523082 | Ручной  | Бинарная шкала {–1, +1}                                                        |     |
| **Sentiment Treebank**   | 2013 | 58980  | Гибрид. | Непрерывная шкала \[0, 1]:<br> \[0; 0,4] – нег., (0,6; 1] – поз.               |     |
| **ML-SentiCon_en**       | 2014 | 24818  | Автом.  | Непрерывная шкала \[–1, 1]:<br> \[–1, 0) – нег., (0, 1] – поз.                 |     |
| **VADER**                | 2014 | 7221   | Ручной  | Непрерывная шкала \[–4, 4]: <br>\[–4, 0) – нег., (0, 4] – поз.                 |     |
| **Chen-Skiena_en**       | 2014 | 4376   | Автом.  | Бинарная шкала {–1, +1}                                                        |     |
| **SCL-NMA**              | 2016 | 3182   | Ручной  | Непрерывная шкала \[–1, 1]:<br> \[–1, 0) – нег., (0, 1] – поз.                 |     |
| **SCL-OPP**              | 2016 | 1153   | Ручной  | Непрерывная шкала \[–1, 1]:<br> \[–1, 0) – нег., (0, 1] – поз.                 |     |
| **ETSL**                 | 2016 | 1150   | Ручной  | Непрерывная шкала \[–1, 1]: <br>\[–1, 0) – нег., (0, 1] – поз.                 |     |
| **SocialSent**           | 2016 | 2463   | Автом.  | Непрерывная шкала \[–3,9; 2,76]: <br>\[–3,9; –0.5] – нег., \[0,5; 2,76] – поз. |     |
| **SenticNet_en**         | 2016 | 100000 | Автом.  | Непрерывная шкала \[–1, 1]: <br>\[–1, 0) – нег., (0, 1] – поз.                 |     |
| **SentiWords**           | 2018 | 39663  | Автом.  | Непрерывная шкала \[–1, 1]:<br> \[–1, 0) – нег., (0, 1] – поз.                 |     |
| **WordStat**             | 2018 | 15955  | Автом.  | Бинарная шкала {–1, +1}                                                        |     |
| **SlangSD**              | 2016 | 96462  | Автом.  | Дискретная шкала \[–2, 2]: <br>\[–2, –1] – нег., \[1, 2] – поз.                |     |


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

### ANEW
1999<br>
ANEW (Affective Norms for English Words) создан в 1999 г. и содержит разметку по категориям тональности (affective valence), активности и контроля (dominance). Слова размечены вручную студентами-психологами.<br>
765<br>
Ручной<br>
Непрерывная шкала \[1; 9]: \[1, 4] – нег., \[6, 9] – поз.<br>
[https://github.com/dwzhou/SentimentAnalysis](https://github.com/dwzhou/SentimentAnalysis)
>Bradley M.M., Lang P.J. Affective Norms for English Words (ANEW): Stimuli, instruction man- ual, and affective ratings (Tech. Report C-1). – Gainesville: University of Florida, Center for Re- search in Psychophysiology, 1999.


<br>

### Словарь Бинга Лью
2004
Словарь Бинга Лью (Bing Liu's Opinion Lexicon или Hu&Liu’s Lexicon) – результат многолетней работы, начавшейся еще в 2004 г.. Его исходная версия была создана на основе расширения начального списка из 30 прилагательных синонимами и антонимами из тезауруса WordNet. В дальнейшем словарь расширялся, в том числе за счет анализа текстов социальных медиа, поэтому присутствуют слова с ошибками.
6776
Автом.
Бинарная шкала {–1, +1}
[https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html)
>Hu M., Liu B. Mining and Summarizing Cus- tomer Reviews // Proceedings of the ACM SIGKDD International Conference on Knowledge, Discovery and Data Mining – KDD-2004 (Aug 22-25, 2004, Seattle, Washington, USA). – New York: Associa- tion for Computing Machinery, 2004. – P. 168–177.

<br>

### MPQA
2005
MPQA (Multi-Perspective Question Answering Subjectivity Lexicon) является частью системы анализа мнений OpinionFinder. Каждое слово в словаре MPQA имеет указание тональности (позитивная, негативная или нейтральная), а также степень тональности (сильная или слабая). При построении MPQA существующий словарь оценочной лексики был расширен за счет тезауруса и словаря General Inquirer, а затем доразмечен вручную.
6450
Ручной
Бинарная шкала {–1, +1}
[http://mpqa.cs.pitt.edu/lexicons/subj_lexicon](http://mpqa.cs.pitt.edu/lexicons/subj_lexicon)
>Wilson T., Wiebe J., Hoffmann P. Recognizing contextual polarity in phrase-level sentiment analysis // Proceedings of the 2005 Human Language Technology Conference and the Conference on Empirical Methods in Natural Language Processing (HLT/EMNLP-05). – 2005. – P. 347–354.

<br>

### SO-CAL
2007
SO-CAL (Semantic Orientation CALculator – это программный инструмент, определяющий тональность текстов. Словарь, используемый в этом инструменте, в рамках настоящей статьи также обозначается SOCAL. Он был получен путем экспертной разметки словкандидатов, собранных из корпусов отзывов, а также из словаря General Inquirer.
6004
Ручной
Непрерывная шкала \[–1, 1]: \[–1, 0) – нег., (0, 1] – поз.
[https://github.com/sfu-discourse-lab/SO-CAL](https://github.com/sfu-discourse-lab/SO-CAL)
>Taboada M., Brooke J., Tofiloski M., Voll K., Stede M. Lexicon-based methods for sentiment analysis // Computational Linguistics. – 2011. – Vol. 37(2). – P. 267–307.

<br>

### SentiWordNet
2010
SentiWordNet создан в рамках автоматического способа на основе разметки понятий тезауруса WordNet с использованием машинного обучения и алгоритма случайного блуждания (random walk).
32902
Автом.
Непрерывная шкала \[–1, 1]: \[–1, 0) – нег., (0, 1] – поз.
[https://github.com/aesuli/sentiwordnet](https://github.com/aesuli/sentiwordnet)
[https://osf.io/download/mtwfr](https://osf.io/download/mtwfr)
>Baccianella S., Esuli A., Sebastiani F. SentiWordNet 3.0: An enhanced lexical resource for sentiment analysis and opinion mining // Proceedings of the Seventh Conference on International Language Resources and Evaluation (LREC10). 2010. – P. 2200–2204.

<br>

### EmoLex_en
2011
EmoLex (NRC Emotion Lexicon) – словарь составлен Саифом Мохаммадом (Saif Mohammad) и Питером Тёрни (Peter Turney) с помощью краудсорсинга. Словарь EmoLex содержит слова, соотнесенные с позитивной и негативной тональностью, а также с эмоциями «гнев», «предвкушение», «отвращение», «страх», «радость», «грусть», «удивление» и «доверие». 
В ноябре 2017 г. словарь был переведен на более чем 100 языков (в том числе, на русский) с помощью Google Translate. Для русского языка были отобраны слова и словосочетания, имеющие позитивную или негативную тональность. Вариант для английского языка далее называется Emolex_en.
5555
Ручной
Бинарная шкала {–1, +1}
[https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm](https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm)
>Mohammad S.M., Turney D.P. Crowdsourcing a word-emotion association lexicon // Computational Intelligence. – 2013. – Vol. 29(3). – P. 436–465.

<br>

### AFINN
2012
AFINN создавался автором с 2009 г.. Словарь был дополнен нецензурными и сленговыми выражениями с целью получения лучшего результата при автоматическом анализе сообщений в социальных медиа. В настоящей статье используется версия AFINN-111.
2474
Ручной
Дискретная шкала \[–5, 5]: \[–5, –1] – нег., \[1, 5] – поз.
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
[https://github.com/felipebravom/StaticTwitterSent/tree/master/extra/Sentiment 140-Lexicon-v0.1](https://github.com/felipebravom/StaticTwitterSent/tree/master/extra/Sentiment%20140-Lexicon-v0.1)
[Sentiment140 Affirmative Context Lexicon and Sentiment140 Negated Context Lexicon](http://saifmohammad.com/WebPages/lexicons.html)
>Mohammad S.M., Kiritchenko S., Zhu X. NRC-Canada: Building the State-of-the-Art in Sentiment Analysis of Tweets // Proceedings of the seventh international workshop on Semantic Evaluation – SemEval-2013 (June 2013, Atlanta, USA). Madison: Omnipress, Inc., 2013. – P. 321–327.

<br>

### Sentiment Treebank
2013
Stanford Sentiment Treebank – это словарь оценочной лексики, сформированный на основе одноименного корпуса, содержащего предложения, извлеченные из отзывов о фильмах. Для каждого предложения построено частичное дерево синтаксического разбора (partial parse trees). Предложения были разбиты на фразы, которые размечались по тональности при помощи краудсорсинга. Слова размечались на основе рекурсивных нейронных сетей с использованием деревьев синтаксического разбора и распределенных представлений слов.
58 980
Гибрид.
Непрерывная шкала \[0, 1]: \[0; 0,4] – нег., (0,6; 1] – поз.
[https://nlp.stanford.edu/sentiment](https://nlp.stanford.edu/sentiment)
>Socher R., Perelygin A., Wu J., Chuang J., Manning C., Ng A., Potts C. Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank // Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP 2013). – 2013. – P. 1631–1642.

<br>

### ML-SentiCon_en
2014
ML-SentiCon - это автоматически созданные многоязычные (английский, испанский, каталонский, баскский и галисийский) многоуровневые оценочные словари. Каждый словарь содержит 8 уровней, причем каждый вышележащий уровень включает все предыдущие, а также новые элементы. Многоуровневость словарей позволяет выбирать между количеством доступных слов и точностью оценок. Словари строились на основе машинного обучения и алгоритма PolarityRank с использованием WordNet.
24 818
Автом.
Непрерывная шкала \[–1, 1]: \[–1, 0) – нег., (0, 1] – поз.
[https://github.com/mauropelucchi/catalan-referendum/tree/master/ML-SentiCon](https://github.com/mauropelucchi/catalan-referendum/tree/master/ML-SentiCon)
>Cruz F.L., Troyano J.A., Pontes B., Ortega F.J. Building layered, multilingual sentiment lexicons at synset and lemma levels // Expert Systems with Applications. – 2014. – Vol. 41. – P. 5984–5994.

<br>

### VADER
2014
VADER (Valence Aware Dictionary and sEntiment Reasoner – это название словаря и инструмента анализа мнений для социальных медиа на основе правил. Исходный список оценочных слов из существующих словарей оценочной лексики (General Inquirer, LIWC и ANEW) был расширен смайликами, связанными с настроением, акронимами и часто используемым оценочным сленгом. Для разметки слов-кандидатов применялся краудсорсинг.
7 221
Ручной
Непрерывная шкала \[–4, 4]: \[–4, 0) – нег., (0, 4] – поз.
[https://github.com/cjhutto/vaderSentiment](https://github.com/cjhutto/vaderSentiment)
>Hutto C.J., Gilbert E. VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text // Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014. – Palo Alto: The AAAI Press, 2014.

<br>

### Chen-Skiena_en
2014
Словарь Чена-Скиены (Chen-Skiena’s lexicon). Яньцин Чен (Yanqing Chen) и Стивен Скиена (Steven S. Skiena) автоматически построили словари оценочной лексики для 136 языков (включая русский и английский). На основе тезаурусов WordNet и Wiktionary и с помощью машинного перевода (Google Translate) был построен многоязычный семантический граф, связывающий слова на разных языках. Затем, отталкиваясь от англоязычного словаря Бинга Лью, были сформированы оценочные словари для других языков на основе алгоритма распространения разметки. Варианты для английского называется Chen-Skiena_en.
4 376
Автом.
Бинарная шкала {–1, +1}
[https://sites.google.com/site/datascienceslab/projects/multilingualsentiment](https://sites.google.com/site/datascienceslab/projects/multilingualsentiment)
>Chen Y., Skiena S. Building Sentiment Lexicons for All Major Languages // Proceedings of the 52nd  Annual Meeting of the Association for Computational Linguistics. – Baltimore, 2014. – P. 383–389.

<br>

### SCL-NMA
2016
SCL-NMA (Sentiment Composition Lexicon for Negators, Modals, and Degree Adverbs)– представляет собой список слов и словосочетаний, включающих отрицания, модальные слова и наречия меры и степени. При создании словаря сначала были отобраны слова-кандидаты из General Inquirer, а также высокочастотные фразы из Британского национального корпуса, включающие слова из General Inquirer в комбинации с отрицаниями, модальными словами и наречиями меры и степени, которые затем были размечены при помощи краудсорсинга.
3 182
Ручной
Непрерывная шкала \[–1, 1]: \[–1, 0) – нег., (0, 1] – поз.
[http://saifmohammad.com/WebPages/SCL.html#NMA](http://saifmohammad.com/WebPages/SCL.html#NMA)
>Kiritchenko S., Mohammad S.M. The Effect of Negators, Modals, and Degree Adverbs on Sentiment Composition // Proceedings of the 7th Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis (WASSA). San Diego, California, 2016. – P. 43–52.


### SCL-OPP
2016
SCL-OPP (Sentiment Composition Lexicon for Opposing Polarity Phrases) представляет собой список отдельных слов и фраз, включающих, по крайней мере, по одному позитивному и негативному слову, например, счастливый инцидент. Словакандидаты отбирались из корпуса твитов (поэтому словарь содержит хештеги и слова с ошибками) с использованием словарей Бинга Лью, NRC Emotion lexicon (EmoLex), MPQA, ETSL и размечались с помощью краудсорсинга.
1 153
Ручной
Непрерывная шкала \[–1, 1]: \[–1, 0) – нег., (0, 1] – поз.
[http://saifmohammad.com/WebPages/SCL.html#OPP](http://saifmohammad.com/WebPages/SCL.html#OPP)
>Kiritchenko S., Mohammad S.M. Happy Accident: A Sentiment Composition Lexicon for Opposing Polarities Phrases // Proceedings of the 10th edition of the Language Resources and Evaluation Conference (LREC). – Portoroћ, Slovenia, 2016. –P. 1157–1164.

<br>

### ETSL
2016
ETSL (SemEval-2015 English Twitter Sentiment Lexicon) – это список униграмм и биграмм с отрицанием, который использовался в качестве тестового множества на семинаре SemEval2015 (задача 10, подзадача E). В качестве словкандидатов были отобраны высокочастотные термины (в том числе с ошибками в написании) из словаря хештегов и словаря Sentiment140-Lexicon, а разметка осуществлялось на основе краудсорсинга.
1 150
Ручной
Непрерывная шкала \[–1, 1]: \[–1, 0) – нег., (0, 1] – поз.
[https://saifmohammad.com/WebPages/SCL.html#ETSL](https://saifmohammad.com/WebPages/SCL.html#ETSL)
>Kiritchenko S., Zhu X., Mohammad S. Sentiment Analysis of Short Informal Texts // Journal of Artificial Intelligence Research. – 2014. – Vol. 50. –P. 723–762.

<br>

### SocialSent
2016
SocialSent – это программный код и наборы данных, в том числе словари оценочной лексики, для проведения анализа мнений по конкретным предметным областям. Алгоритм создания словарей SentProp включает два этапа: сначала формируется лексический граф на основе распределенных представлений слов, построенных с использованием предметноориентированных корпусов. Затем слова в лексическом графе размечаются на основе алгоритма случайного блуждания (random walk) и начального небольшого множества слов, специфичных для предметной области.
В SocialSent содержатся исторические словари оценочной лексики на английском языке. Для каждого десятилетия с 1850 по 2000 гг. построены пара словарей – один включает высокочастотные слова, второй – высокочастотные прилагательные. В настоящей статье использовалась пара словарей за последнее десятилетие.
2 463
Автом.
Непрерывная шкала \[–3,9; 2,76]: \[–3,9; –0.5] – нег., \[0,5; 2,76] – поз.
[https://nlp.stanford.edu/projects/socialsent](https://nlp.stanford.edu/projects/socialsent)
>Hamilton W.L., Clark K., Leskovec J., Jurafsky D. Inducing domain-specific sentiment lexicons from unlabeled corpora // Proceedings of Conference on Empirical Methods in Natural Language Processing. – 2016. – P. 595–605.

<br>

### SenticNet_en
2016
SenticNet – это проект по анализу мнений на уровне понятий, начатый в 2009 г. в MIT Media Laboratory. Для построения словаря оценочной лексики сначала был сформирован граф понятий с использованием нейронных сетей долгой краткосрочной памяти (Long short-term memory, LSTM), обучавшихся на основе распределенных представлений слов. Затем для разметки понятий по тональности применялось специальное векторное пространство AffectiveSpace. В работе используется версия словаря SenticNet 5 (далее в статье этот словарь называется SenticNet_en). В рамках SenticNet имеется проект BabelSenticNet, содержащий словари для 40 языков, в том числе русского. Далее в нашей статье словарь для русского языка обозначается SenticNet_ru.
100 000
Автом.
Непрерывная шкала \[–1, 1]: \[–1, 0) – нег., (0, 1] – поз.
[https://sentic.net/downloads](https://sentic.net/downloads)
>Cambria E., Poria S., Hazarika D., Kwok K. SenticNet 5: Discovering conceptual primitives for sentiment analysis by means of context embeddings // Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence (AAAI-18). 2018. – P. 1795–1802.

<br>

### SentiWords
2018
SentiWords создан в процессе исследования, каким образом на основе словаря SentiWordNet можно получить априорную оценку тональности слова, т.е. оценку, которая не зависит от различных семантических значений данного слова. С этой целью было использовано машинное обучение и различные признаки, выводимые из характеристик слов SentiWordNet.
39 663
Автом.
Непрерывная шкала \[–1, 1]: \[–1, 0) – нег., (0, 1] – поз.
[https://hlt-nlp.fbk.eu/technologies/sentiwords](https://hlt-nlp.fbk.eu/technologies/sentiwords)
>Gatti L., Guerini M., Turchi M. SentiWords: Deriving a high precision and high coverage lexicon for sentiment analysis // IEEE Transactions on Affective Computing. – 2016. – Vol. 7(4). – P. 409–421.

<br>

### WordStat
2018
WordStat создан путем объединения отрицательных и положительных слов из словарей Harvard-IV, Regressive Imagery Dictionary и LIWC. Затем список был автоматически расширен синонимами и связанными словами, а также различными морфологическими формами входящих в него слов.
15 955
Автом.
Бинарная шкала {–1, +1}
[https://provalisresearch.com/products/content-analysis-software/wordstat-dictionary/sentiment-dictionaries](https://provalisresearch.com/products/content-analysis-software/wordstat-dictionary/sentiment-dictionaries)
>WordStat: content analysis and text mining software. – URL: Ошибка! Недопустимый объект гиперссылки. (дата обращения: 01.08.2020).

<br>

### SlangSD(Slang Sentiment Dictionary)
2016
The author leverage web resources to construct an extensive Slang Sentiment word Dictionary (SlangSD) that is eas to maintain and extend. In estimating the sentiment strength of slang words, we scale the strength from -2 to 2, where -2 is strongly negative, -1 is negative, 0 is neutral, 1 is positive, and 2 is strongly positive.
96,462
Автом.
Дискретная шкала \[–2, 2]: \[–2, –1] – нег., \[1, 2] – поз.
[https://osf.io/y6g5b/wiki/slangsd](https://osf.io/y6g5b/wiki/slangsd)
>Wu, L., Morstatter, F. & Liu, H. SlangSD: building, expanding and using a sentiment dictionary of slang words for short-text sentiment classification. Lang Resources & Evaluation 52, 839–852 (2018). https://doi.org/10.1007/s10579-018-9416-0

