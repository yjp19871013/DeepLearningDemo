good_sentences=[
    'i like you',
    'i love you',
    'you are so cool',
    'you are right',
    'you are beautiful'
]


bad_sentences=[
    'i hate you',
    'i beat you',
    'you are not cool',
    'you are wrong',
    'you are ugly'
]

good_sentences_join = ' '.join(good_sentences)
good_words = good_sentences_join.split()

bad_sentences_join = ' '.join(bad_sentences)
bad_words = bad_sentences_join.split()

good_words_freq = {}
for word in good_words:
    good_words_freq.setdefault(word, round(good_words.count(word)/len(good_words), 2))

bad_words_freq = {}
for word in bad_words:
    bad_words_freq.setdefault(word, round(bad_words.count(word)/len(bad_words), 2))

p_bad = {}
keys = set(good_words + bad_words)
for key in keys:
    bad_freq = 0.0
    if key in bad_words_freq:
        bad_freq = bad_words_freq[key]

    good_freq = 0.0
    if key in good_words_freq:
        good_freq = good_words_freq[key]

    p_bad.setdefault(key, max(0.01, min(0.99, bad_freq/(bad_freq+good_freq))))

def analyse_bad_sentence(sentence, p_not_found=0.5):
    words = sentence.lower().split()
    p_bad_word = 1.0
    p_bad_word_reverse = 1.0
    for word in words:
        if word in p_bad:
            p_bad_word *= p_bad[word]
            p_bad_word_reverse *= 1 - p_bad[word]
        else:
            p_bad_word *= p_not_found
            p_bad_word_reverse *= 1 - p_not_found
    return p_bad_word / (p_bad_word + p_bad_word_reverse)

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Usage: ai_simulate sentence')
    
    sentence = sys.argv[1]
    confidence = analyse_bad_sentence(sentence)
    if confidence > 0.9:
        print('You should not swear at me!')
    else:
        print('Thank you!')
    
    

