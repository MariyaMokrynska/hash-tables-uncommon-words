def uncommon_from_sentences(sentences):
    sentence_appearance = {}

    for sentence in sentences:
        # Convert to set to count each word only once per sentence
        words = set(sentence.split())
        for word in words:
            if word not in sentence_appearance:
                sentence_appearance[word] = 0
            sentence_appearance[word] += 1

    result = [word for word, count in sentence_appearance.items()
              if count == 1]
    return result

# using plain dict

# def uncommon_from_sentences(sentences):
#     global_counts = {}
#     per_sentence_counts = []

#     for sentence in sentences:
#         local = {}
#         for word in sentence.split():
#             local[word] = local.get(word, 0) + 1
#         per_sentence_counts.append(local)
#         for word in local:
#             global_counts[word] = global_counts.get(word, 0) + 1

#     result = []
#     for word, total in global_counts.items():
#         if total == 1:
#             for sentence_count in per_sentence_counts:
#                 if sentence_count.get(word) == 1:
#                     result.append(word)
#                     break
#     return result
