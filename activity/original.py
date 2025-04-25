def uncommon_from_sentences(s1, s2):
    dict1 = {}
    for word in s1.split():
        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1

    dict2 = {}
    for word in s2.split():
        if word in dict2:
            dict2[word] += 1
        else:
            dict2[word] = 1

    set1 = set()
    for word in dict1:
        if dict1[word] == 1:
            set1.add(word)

    set2 = set()
    for word in dict2:
        if dict2[word] == 1:
            set2.add(word)

    uncommon = set1.symmetric_difference(set2)

    return uncommon
