def matching_words(sentence_1, sentence_2):
    words_1 = sentence_1.split(" ")
    words_2 = sentence_2.split(" ")
    score = 0

    for word_1 in words_1:
        for word_2 in words_2:
            if word_1.lower() == word_2.lower():
                score += 1
    return score

if __name__ == '__main__':
    import datetime
    import time

    sentences = ["This is python", "Python tutorials", "Beginner tutorial for python",
                 "Learn python for free", "Free tutorials for beginner", "This is Pycharm",
                 "Learn how to code", "Free code available", "Limited seats available",]
    query = input("Search Your Query string \n")

    scores = [matching_words(query, sentence) for sentence in sentences]

    sorted_sentence_score = [sentence_score for sentence_score in sorted(zip(scores, sentences), reverse=True)]

    time_taken = datetime.datetime.now()
    print("About",len(sorted_sentence_score), "results found in", time_taken.strftime("%S seconds \n"))
    for score, item in sorted_sentence_score:
        print(f"\"{item}\": with a score of {score}")








