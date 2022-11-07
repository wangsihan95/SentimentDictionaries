

# ANEW

ANEW, short for Affective Norms for English Words, is a database of 1,034 English words that have been manually rated by many human volunteers on three affective measures: pleasure (valence), arousal (excitement), and dominance (level of control), as elicited by a particular word (Bradley & Lang 1999). In 2013, Warriner et al. expanded the database to nearly 14,000 English lemmas, and also split data by gender, age, and educational differences in raters (Warriner et al. 2013). In both databases, affective ratings are on a scale from 1 to 9, where 1 is the least pleasurable/exciting/controlling, and 9 is the most.

In our implementation, we used Warriner et al.’s expanded database, extracting the average valence, pleasant, and arousal for each word from the larger database, for word-by-word sentiment analysis.

We wrote a Python script to perform sentiment analysis with the resulting data. Given a body of text in .txt format, we first tokenized the text into sentences using the NLTK’s sentence tokenizer, and then tokenized each sentence into individual words with the NLTK’s word tokenizer, stripping out all stop words found in the NLTK’s English stop word database. For each non-stop word in each sentence, we searched for the word in the database and stored its individual valence, arousal, and dominance values.

As ANEW uses ratings from a scale of 1 (most negative) to 9 (most positive), valence values of 5 are considered neutral; values less than 5 are considered positive, and values greater than 5 are considered negative. In accordance with Hutto & Gilbert (2014)’s method for accounting for negative values, if a word in the three words prior to the word indicated negation – “not” or “no” – we reversed the polarity of that word. We did this by computing (5 – (valence – 5)) as the new valence value.

After finding sentiment ratings for each non-stop word in each sentence, we found overall sentiment ratings for the sentence by either taking the median or the mean of the sentiment ratings for each word in that sentence, according to the method selected by the user. For each sentence, we labeled the sentence’s valence as negative if less than 5, neutral if equal to 5, and positive if greater than 5.
Weaknesses of this approach: As this is a word-for-word approach to analyzing the sentiment of an entire sentence, the results are limited by the number of words available in ANEW.



# References

> Bradley, M. M., & Lang, P. J. (1999). Affective norms for English words (ANEW): Instruction manual and affective ratings (pp. 1-45). Technical report C-1, the center for research in psychophysiology, University of Florida.

<br>

> Warriner, A. B., Kuperman, V., & Brysbaert, M. (2013). Norms of valence, arousal, and dominance for 13,915 English lemmas. Behavior research methods, 45(4), 1191-1207.
