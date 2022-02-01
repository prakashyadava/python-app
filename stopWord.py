import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "Nick likes to play football however he is not too fond of tennis. hello!!"
punc = '''!()-{};:'"\,<>./?@#$%^&*_~'''
no_punc = ""
for char in text:
    if char not in punc:
        no_punc +=char
text_tokens = word_tokenize(no_punc)
# print(text_tokens)

token_without_sw = [word for word in text_tokens if not word in stopwords.words('english')]
# print(token_without_sw)

filtered_sentence = (" ").join(token_without_sw)
print(filtered_sentence)
#
# print(stopwords.words('english'))