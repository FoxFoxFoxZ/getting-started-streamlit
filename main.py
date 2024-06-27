import streamlit as st
import pandas as pd

with st.echo():
    st.title("Getting started streamlit")
    st.write("This is introduction to streamlit")

    md = st.text_area('Type in your markdown string (without outer quotes)',
                    "Happy Streamlit-ing! :balloon:")


    st.markdown(md)

    show_btn = st.button("RUn")
    if show_btn:
        st.code(f"""
    import streamlit as st
    st.markdown('''{md}''')
    """)

    cols = st.columns(2) 
    with cols[0]:  
        age_input = st.number_input("Input your age")
        st.markdown(f"Your age {age_input}")


    # st.markdown("# NLP Task")
    with cols[1]:   
        text_int = st.text_input("Input your text")
        word_tokenize = "|".join(text_int.split())
        st.markdown(f"{word_tokenize}")

    df = pd.DataFrame({
        "first column" : [1,2,3,4],
        "second column" : [10,20,30,40]
    }
    )
    st.dataframe(df)
    show_chart_botton = st.button("Click this")
    if show_chart_botton:
        st.line_chart(df, x ="first column",y="second column")