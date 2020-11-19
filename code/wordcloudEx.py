from newspaper import Article
article = Article('https://en.wikipedia.org/wiki/Ice_cream')
article.download()
article.parse() #단어들로 대체 필요

#print(article.text)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from wordcloud import STOPWORDS

#dependencies to load the image
from PIL import Image
import numpy as np

#show graph
def showing():
    mask = np.array(Image.open(r"C:\Users\User\Downloads\twitter.jpg")) 
    wc = WordCloud(stopwords=STOPWORDS,
                   mask=mask, background_color="white",
                   max_words=2000, max_font_size=256,
                   random_state=42, width=mask.shape[1],
                   height=mask.shape[0])
    wc.generate(article.text)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis('off')
    plt.show()