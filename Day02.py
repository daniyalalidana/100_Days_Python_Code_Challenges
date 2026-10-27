'''
Define a function analyze_text(text: str) -> dict that accepts a string of arbitrary text and returns a dictionary containing:

"total_words": Total word count (ignoring case and punctuation).

"unique_words": Total count of distinct words.

"word_frequencies": A dictionary mapping each unique word (lowercase) to its frequency.

"top_3_words": A list of the 3 most frequent words as tuples (word, count).

Clean the input text by stripping punctuation (., ,, !, ?, ;, :, ").

Handle edge cases cleanly (e.g., empty string input should return total word count 0 without throwing errors).
'''
def analyze_text(text: str):
    str_dict = {}
    str_dict['total_words'] = len(text)
    text_strip = text.split()
    str_dict['unique_words'] = len(set(text_strip))
    word_frequencies = {}
    top_3_words = []


    for  val in text_strip:
        if val in word_frequencies:
            word_frequencies[val] +=1
        else:
            word_frequencies[val] = 1
    str_dict["word_frequencies"] = word_frequencies
    print(str_dict)


sample_text = "Python is great. Python is dynamic, fast, and Python is fun!"
analyze_text(sample_text)