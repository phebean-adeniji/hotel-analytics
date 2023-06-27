import streamlit as st
import streamlit.components.v1 as components
import time
import utils

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

# st.sidebar.markdown("""<style>body {background-color: #2C3454;white;}</style><body></body>""", unsafe_allow_html=True)
st.markdown("""<h1 style='text-align: center; white;font-size:60px;margin-top:-50x;'>5 ⭐ Lagos Hotels' Analytics</h1>""", unsafe_allow_html=True)

# st.altair_chart(top_cat(df))

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

## replace this with urls of the hotel images
imageUrls = [
    "https://lh3.googleusercontent.com/proxy/XIhbefEWcqerUZwn3TaSaz_x7YsoOJntot1MT1J2am540W6VCrdsc_SrQF9J_QcQjTrnX2Hf0Jj8K60eJpHfNN12xZSdT5Dkxn42tQQ3RoR2lY-F8isCm4queJjLdfS5bvAAh5Ec5jtJhSEwmhiJ7ndcmJl6Egs=w253-h187-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipO_HDuCY3PS0WjKtg--D8kEedu7hpPdhOijneVB=w253-h189-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipPFpYsv8t-DDQZ71vTVyiURpzfodzFFAWeXqaTn=w253-h189-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipPCbGjFsv2L9Zr3v7oZkxaAAJnxVcTSZLf7J9sr=w253-h142-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipPzXwFEFbFAK28i_Fd3h7uUvvZzxpyxIK-EPASq=w253-h142-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipNSxuDAT_tgewACBLJTuzDnB3jlv9B0uD2_HgOZ=w253-h189-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipNNbgUATprfvhvCLQpwxSFmq6PxH0TWPq4IfzYA=w253-h241-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipNBf0W2KY87ktrrE7HvMyThBTdJAe5HpgvtlC4M=w253-h253-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipP1myI5-sagpTwy80G5CpqQSpWM2uB-w_kVV_qs=w253-h168-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipMEWuNKeEABiiMF55H-PIAJ4eWPpzKeCSItl_jv=w253-h168-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipM7aiGJMHvGxO0RHjnYwAblV0KYZa58DQG2QaQS=w253-h337-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipNd4FXyxqVJ5aIadirHMeaZWJqR8awNvYXybIAK=w253-h168-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipNIDKsXmu6IXJab7mApQ2KK_zRRzBtuuTte0LQK=w253-h168-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipNjdE-SXwPaoHofsEl9cXr9-upmLUh4dnSwQ1on=w253-h168-k-no",
    "https://lh5.googleusercontent.com/p/AF1QipO_g56B9MGVef_u7nQsZa8JM_CszIJSu1duS45p=w253-h168-k-no",
]
selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

if selectedImageUrl is not None:
    st.image(selectedImageUrl)


hotels = [
    'Eko Hotels & Suites, Victoria Island',
    'Radisson Blu Hotel, Victoria Island',
    'Lagos Oriental Hotel, Lekki',
    'Four Points by Sheraton Lagos, Victoria Island',
    'Sharaton Lagos Hotel, Ikeja'
]

topic_names = utils.df['review_topic'].unique().tolist()

def get_dataframe_by_hotel_name(hotel_list, hotel_name):
    for hotel_dict in hotel_list:
        if hotel_dict["hotel_name"] == hotel_name:
            return hotel_dict["hotel_df"]


# Create checkboxes for each hotel
selected_hotels = [st.checkbox(hotel) for hotel in hotels]

for index, hotel in enumerate(hotels):
    if selected_hotels[index]:
        # 1. Show the location on a map
        utils.render_google_map(hotel)
        hotel_df = get_dataframe_by_hotel_name(utils.hotel_list, hotel)
        # 2. Plot a chart
        utils.plot_topic_sentiment_dist(hotel_df, "review_topic", "Sentiment")

        topic_key = f"{hotel}_topic"  # Unique key for topics
        sentiment_key = f"{hotel}_sentiment"  # Unique key for sentiments

        topic = st.selectbox('Choose a topic:', topic_names, key=topic_key)

        # 3. Return the summary of the positive, neutral, and negative reviews under that category
        sentiment = st.selectbox('', (
            'Summary of the positive reviews', 
            'Summary of the neutral reviews', 
            'Summary of the negative reviews'), key=sentiment_key)

        df = hotel_df[hotel_df["review_topic"] == topic]

        if sentiment == 'Summary of the positive reviews':
            reviews_df = df[df["Sentiment"] == "positive"]
        elif sentiment == 'Summary of the neutral reviews':
            reviews_df = df[df["Sentiment"] == "neutral"]
        elif sentiment == 'Summary of the negative reviews':
            reviews_df = df[df["Sentiment"] == "negative"]

        reviews_text = ". ".join(reviews_df["sentence"])

        with st.spinner("Summarizing the sentiments..."):
            # Simulate processing time
            time.sleep(1)
            st.write(utils.text_summarizer(reviews_text))

        # 4. Show the word cloud of keywords
        with st.spinner("Generating a Word Cloud..."):
            # Simulate processing time
            time.sleep(2)
            utils.generate_wordcloud(reviews_text)






