import streamlit as st
import pickle
import pandas as pd





def recommendation(music_name, music_df, similarity):
    assert isinstance(music_df, pd.DataFrame), "'music_df' should be a DataFrame"
    idx = music_df[music_df['music_name'] == music_name].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    recommended_music = []
    for i in distances[1:21]:
        recommended_music.append(music_df.iloc[i[0]]['music_name'])
        
    return recommended_music 

# Load data
music_df = pickle.load(open('music.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

music_list = music_df['music_name'].values

st.title("Music Recommendation System")

select_music_name = st.selectbox('Select song', music_list)

if st.button("Recommend"):
    names = recommendation(select_music_name, music_df, similarity)

    

    for i in names:
        st.write(i)      


if st.button("Reset"):
    st.rerun()






