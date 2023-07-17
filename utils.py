import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
from heapq import nlargest
import spacy 
# Text Preprocessing Pkg
from spacy.lang.en.stop_words import STOP_WORDS
import altair as alt
nlp = spacy.load('en_core_web_sm')
# from summarizer import Summarizer

df = pd.read_csv('results/hotel_split_reviews-sentiments-and-ldatopics-8Topics.csv')
# df = df.drop_duplicates()
# print(df.columns)
eko_df = df[df.hotel_name=='Eko Hotel']
sheraton_df = df[df.hotel_name=='Sheraton Lagos']
radisson_df = df[df.hotel_name=='Radisson Blu VI']
fourpoints_df = df[df.hotel_name=='Four Points By Sheraton']
lagos_df = df[df.hotel_name=='Lagos Oriental']


hotel_list = [
    {
        'hotel_name':'Eko Hotels & Suites, Victoria Island',
        'hotel_df': eko_df
    },
   {
        'hotel_name':'Radisson Blu Hotel, Victoria Island',
        'hotel_df': radisson_df
    },
    {
        'hotel_name':'Lagos Oriental Hotel, Lekki',
        'hotel_df': lagos_df
    },
    {
        'hotel_name':'Four Points by Sheraton Lagos, Victoria Island',
        'hotel_df': fourpoints_df
    },
    {
        'hotel_name':'Sharaton Lagos Hotel, Ikeja',
        'hotel_df': sheraton_df
    },
]

stopwords = list(STOP_WORDS)
stopwords = stopwords + ["hotel", "hotels", "lagos", "nigeria", "nigerians", "good", "great", "nice", "place"]

#  Place All As A Function For Reuseability
def text_summarizer(raw_docx, stopwords = stopwords):
    raw_text = raw_docx
    docx = nlp(raw_text)
    # Build Word Frequency
# word.text is tokenization in spacy
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    # Sentence Tokens
    sentence_list = [ sentence for sentence in docx.sents ]

    # Calculate Sentence Score and Ranking
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    summary_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summary_sentences ]
    summary = ' '.join(final_sentences)
    
    return summary

def convert_to_sentence_case(paragraph):
    sentences = paragraph.split('. ')  # Split the paragraph into individual sentences
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]  # Capitalize the first character of each sentence
    converted_paragraph = '. '.join(capitalized_sentences)  # Join the sentences back into a paragraph

    return converted_paragraph

def tokenize_text(input_text):
    doc = nlp(input_text)
    tokens = [token.text for token in doc]
    return tokens

def generate_wordcloud(text, stopwords=stopwords):
    # Tokenize the joined text into individual words
    tokens = tokenize_text(text)

    # Remove stop words from the tokens
    filtered_tokens = [word for word in tokens if word.lower() not in stopwords]

    # Join the filtered tokens back into a single string
    filtered_text = " ".join(filtered_tokens)

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, stopwords=stopwords).generate(filtered_text)

    # Display word cloud in Streamlit app
    return st.image(wordcloud.to_array())

def render_google_map(location):
    # Google Map HTML code
    html_code = f"""
    <iframe width="100%" height="500" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" 
    src="https://www.google.com/maps?q={location}&output=embed"></iframe>
    """
    # Render the HTML code using the `st.components.v1.html` function
    st.components.v1.html(html_code, width=800, height=600)

def plot_topic_sentiment_dist(hotel_df:pd.DataFrame, topic_col_name:str, sentiment_col_name:str):
    # Group data by topic and sentiment
    grouped_data = hotel_df.groupby([topic_col_name, sentiment_col_name]).size().unstack(fill_value=0)

    # Display topic categories and sentiment distribution
    # st.subheader('Sentiment Distribution by Topic')
    # st.dataframe(grouped_data)
    fig, ax = plt.subplots()
    # Generate grouped bar chart
    grouped_data.plot(kind='barh', stacked=True, ax=ax)
    # plt.xlabel('Count')
    plt.ylabel('Topic')
    # plt.title('Sentiment Distribution by Topic')
    st.pyplot(fig)
