from collections import defaultdict


def uncommon_from_sentences(sentences):
    # Count how many times each word appears across all sentences
    total_count = defaultdict(int)

    # Count how many times each word appears in each sentence
    sentence_counts = []

    for sentence in sentences:
        word_count = defaultdict(int)
        words = sentence.split()
        for word in words:
            word_count[word] += 1
        sentence_counts.append(word_count)

        # Add to the total count once per sentence
        for word in word_count:
            total_count[word] += 1

    result = []

    # A word is uncommon if it appears only once in total
    # and that one time is in just one sentence
    for word in total_count:
        if total_count[word] == 1:
            for word_count in sentence_counts:
                if word_count.get(word) == 1:
                    result.append(word)
                    break

    return result
