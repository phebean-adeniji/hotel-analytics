import streamlit as st
import streamlit.components.v1 as components
import time
import utils

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

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
imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")
# Get instant insights into customer opinions using advanced NLP techniques. Discover topics, sentiments, and key highlights at a glance. Make informed decisions based on the collective voice of individuals
def home_page():
    st.markdown("""<h1 style='text-align: center; color: black;'>Welcome to Hotel Reviews Analytics!</h1><p style='color: #e6d8a7;'>""", unsafe_allow_html=True)
    st.markdown("""<p style='text-align: center; color: black;'>Get insight into other customers' opinions on these luxury hotel in Lagos. Use the insights to your advantage! Make decisions on which hotel will meet your specific needs. We provide the sentiments (positive, negative and neutral) across different topics such as the hotel rooms, food, ambience, staff, etc.</p><p style='color: #e6d8a7;'>""", unsafe_allow_html=True)
    st.subheader("")
    st.subheader("")
    st.subheader("")
    selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=400)

    if selectedImageUrl is not None:
        st.image(selectedImageUrl)
    st.markdown("""<p style='text-align: center; color: gray;'><<< Click the side bar to select a hotel and continue.</p><p style='color: #e6d8a7;'>""", unsafe_allow_html=True)


hotels = [
    'Eko Hotels & Suites, Victoria Island',
    'Radisson Blu Hotel, Victoria Island',
    'Lagos Oriental Hotel, Lekki',
    'Four Points by Sheraton Lagos, Victoria Island',
    'Sharaton Lagos Hotel, Ikeja'
]
topic_col_name = 'review_topic'  # Replace with the actual column name for topic
sentiment_col_name = 'Sentiment'  # Replace with the actual column name for sentiment

def set_page_config():
    # Set CSS style to change font type
    st.markdown(
        """
        <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
def main():
    set_page_config()
    st.sidebar.markdown("""<style>body {background-color: #2C3454;white;}</style><body></body>""", unsafe_allow_html=True)
   
    topic_names = utils.df['review_topic'].unique().tolist()
    # desired_topic = "Room Quality and Standards"  # Replace with your desired topic name
    # if desired_topic in topic_names:
    #     topic_names.remove(desired_topic)
    #     topic_names.insert(0, desired_topic)

    def get_dataframe_by_hotel_name(hotel_list, hotel_name):
        for hotel_dict in hotel_list:
            if hotel_dict["hotel_name"] == hotel_name:
                return hotel_dict["hotel_df"]


    st.sidebar.title('Menu')
    Options = st.sidebar.selectbox(
        '', ['Go Home',
        'Eko Hotels & Suites, Victoria Island',
        'Radisson Blu Hotel, Victoria Island',
        'Lagos Oriental Hotel, Lekki',
        'Four Points by Sheraton Lagos, Victoria Island',
        'Sharaton Lagos Hotel, Ikeja'], index=0
    )


    # Create checkboxes for each hotel
    # st.markdown("##### Select a hotel of choice to see what other customers think.")

    # selected_hotel = st.radio(
    #     "",
    #     hotels, label_visibility="collapsed")

    if Options == 'Go Home':
        home_page()
    else:
        hotel_df = get_dataframe_by_hotel_name(utils.hotel_list, Options)

        topic_key = f"{Options}_topic"  # Unique key for topics
        sentiment_key = f"{Options}_sentiment"  # Unique key for sentiments
        st.markdown(f"###### Do you want to find out what people are saying about {Options}?")
        topic = st.selectbox('Choose a topic:', topic_names, key=topic_key)

        # 3. Return the summary of the positive, neutral, and negative reviews under that category
        sentiment = st.selectbox('Select a sentiment type to read the summary of what people think', (
            'Positive', 
            'Negative', 
            'Neutral'), key=sentiment_key)

        df = hotel_df[hotel_df["review_topic"] == topic]

        if sentiment == 'Positive':
            reviews_df = df[df["Sentiment"] == "positive"]
        elif sentiment == 'Neutral':
            reviews_df = df[df["Sentiment"] == "neutral"]
        elif sentiment == 'Negative':
            reviews_df = df[df["Sentiment"] == "negative"]

        reviews_text = ". ".join(reviews_df["sentence"])

        with st.spinner("Summarizing the sentiments..."):
            # Simulate processing time
            time.sleep(1)
            summary = utils.text_summarizer(reviews_text)
            corrected_summary = utils.convert_to_sentence_case(summary)
            st.write(corrected_summary)

        # 4. Show the word cloud of keywords
        with st.spinner("Generating a Word Cloud..."):
            # Simulate processing time
            time.sleep(2)
            utils.generate_wordcloud(reviews_text)
            st.markdown("""<p style='text-align: left; color: gray;'>This image is a word cloud that shows the dominant words in the reviews that fall under your selection.</p><p style='color: #e6d8a7;'>""", unsafe_allow_html=True)

        # 2. Plot a chart
        st.subheader('Sentiment Distribution by Topic')
        # st.markdown("""<h3 style='text-align: center; color: black;'>Sentiment Distribution by Topic</h3><p style='color: #e6d8a7;'>""", unsafe_allow_html=True)
        st.markdown("""<p style='text-align: left; color: gray;'>These are the review topics covered and their respective sentiments.</p><p style='color: #e6d8a7;'>""", unsafe_allow_html=True)
        utils.plot_topic_sentiment_dist(hotel_df, "review_topic", "Sentiment")
        # Load your hotel_df DataFrame

        # chart = utils.plot_topic_sentiment_dist(hotel_df, topic_col_name, sentiment_col_name)

        # Display the Altair chart using st.altair_chart
        # st.altair_chart(chart, use_container_width=True)


        # 1. Show the location on a map
        st.markdown("###### Locate Hotel on Google Maps")
        utils.render_google_map(Options)
    # topic_names = utils.df['review_topic'].unique().tolist()


if __name__ == "__main__":
    main()


