import streamlit as st 
import pickle

def recommend(book):
    
    #getting index of book 
    book_index = collaborative_matrix.index.get_loc(book)
    #getting similarity score with each book
    similarities = similarity_scores[book_index]
    #getting 5 most similar books 
    books_list = sorted(list(enumerate(similarities)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_books=[]
    recommended_book_posters=[]

    for i in books_list:
        
        recommended_books.append(collaborative_matrix.index[i[0]])
        recommended_book_posters.append(imageurls.loc[imageurls['Book-Title'] == collaborative_matrix.index[i[0]], 'Image-URL-M'].values[0])
    
    return recommended_books,recommended_book_posters

st.title('Book Recommender System')

collaborative_matrix = pickle.load(open('collaborative_matrix.p','rb'))

similarity_scores = pickle.load(open('similarity_scores.p','rb'))

imageurls = pickle.load(open('imageurls.p','rb'))

selected_book_name = st.selectbox('Select a book',collaborative_matrix.index.values)

if st.button('Recommend'):
    names,posters = recommend(selected_book_name)
    
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])