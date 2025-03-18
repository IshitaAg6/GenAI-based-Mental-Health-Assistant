import streamlit as st
from src.sentiment_analysis import analyze_sentiment
from src.recommendations import get_coping_strategies, get_self_care_recommendations


st.title("Personalized Mental Health Support System")
st.subheader("Analyze your journal entries and get personalized mental health recommendations.")

journal_entry = st.text_area("Write your journal entry here:")

if st.button("Analyze"):
    if journal_entry:
        sentiment = analyze_sentiment(journal_entry)
        st.write("### Sentiment Analysis:")
        st.write(sentiment)

        coping_strategies = get_coping_strategies(sentiment)
        self_care_recommendations = get_self_care_recommendations(sentiment)

        st.write("### Coping Strategies:")
        st.write(coping_strategies)

        st.write("### Self-Care Recommendations:")
        st.write(self_care_recommendations)
    else:
        st.error("Please enter your journal entry before analyzing.")

