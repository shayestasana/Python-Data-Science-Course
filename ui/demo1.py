'''
to run this, open terminal and type
# cd Coding Python
# streamlit run ui/demo1.py
'''
import streamlit as st

# text elements
st.title("Streamlit Demo")
st.header("Streamlit is awesome")
st.subheader("It's easy to use")
st.text("This is a simple text example")
st.write("This is a magical function")
st.markdown("This is a **markdown** `example`")
st.success("This is a success message")
st.info("This is an info message")
st.warning("This is a warning message")
st.error("This is an error message")
st.exception("This is an exception message")

# media elements
st.image("ui/background.jpg")  
st.video('https://youtu.be/BdrDZWhDpYE')
#st.audio(r"C:\Users\sanas\Music\Senorita")

#audio_file = open('Senorita.mp3', 'rb')
#audio_bytes = audio_file.read()
#st.audio(audio_bytes, format='audio/mp3')

# widgets
name = st.text_input("Enter the username")
cost = st.number_input("Enter the cost")
comment = st.text_area("Enter remarks")
status = st.checkbox("save this data")
gender = st.radio("Gender", ["Male","Female","Others"])

querylist = ['How to use streamlit?',
             'Is streamlit free or paid?',
             'Is it gonna rain now?']
query = st.selectbox("What the Query",querylist)
rating = st.slider("Select the rating",1,5)
btn = st.button("Submit the response")
# if btn is pressed
if btn:
    st.write("Username:", name)
    st.write("Cost:", cost)
    st.write("Comment:", comment)
    st.write("Status:", status)
    st.write("gender:", gender)
    st.write("query:", query)
    st.write("rating:", rating)