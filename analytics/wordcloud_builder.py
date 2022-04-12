import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from wordcloud import WordCloud
from stop_words import get_stop_words
import numpy as np
from PIL import Image
import os

def create_wordcloud(file_name):
    stop_words = get_stop_words('english')
    additional_words = ["just", "said", "told", "like", "t", "s", "get", "time", "year", "got", "one"]
    stop_words.extend(additional_words)
    file = open(file_name, encoding="utf8")
    line = file.read()
    words = line.split()

    if file_name.startswith('nta'):
        image_name = "nta.png"
        with open('filteredtext_nta.txt', "a") as filtered_file:
            for r in words:
                if not r in stop_words:
                    filtered_file.write(" " + r)

        with open('filteredtext_nta.txt', 'r') as txt_file:
            filteredtext = txt_file.read()

    else:
        image_name = "yta.png"
        with open('filteredtext_yta.txt', "a") as filtered_file:
            for r in words:
                if not r in stop_words:
                    filtered_file.write(" " + r)

        with open('filteredtext_yta.txt', 'r') as txt_file:
            filteredtext = txt_file.read()

    #mask = np.array(Image.open('dinosaur.png'))
    wordcloudd = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black',
                        colormap='viridis', collocations=False,
                             stopwords=stop_words).generate(filteredtext)
    # Display image
    plt.figure(figsize=(40, 30))
    plt.axis("off")
    wordcloudd.to_file(image_name)

def main():
    for file in os.listdir("."):
        if file.endswith(".txt") and not file.startswith("filtered"):
            create_wordcloud(file)
    quit()

if __name__ == '__main__':
    main()
