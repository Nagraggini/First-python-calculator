import streamlit as st

st.title("Hello 👋")
st.markdown(
    """ 
   Welcome to Andrea's Streamlit app!
    """
)

if st.button("Send balloons!"):
    st.balloons()
