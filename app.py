import openai
import streamlit as st

st.title("GPT-3 via Python") 
st.write("By Dr. Yan, v1.0, 3/15/2023")

with st.expander("Click here to see a simple explanation. Click again to hide it"):
    st.write(f" ##### Running GPT-3 via Python.")
    st.write("Based on https://www.makeuseof.com/python-gpt-3-how-use/ by SAI ASHISH KONCHADA")
    
  
with st.expander("Click here to see how to get your API Key."):
    st.write("Register an account at https://openai.com/ then get an API key")
    #st.write("https://chat.openai.com/auth/login")


with st.expander("Step 1: click here to enter your API. click again to hide."):
    myKey='a'  
    myKey=st.text_input("Copy-and-paste your API key below:")    

with st.expander("Optoinal: click here to see your API key."):
    st.write(myKey)
    
def askGPT(text):
    response = openai.Completion.create(engine="text-davinci-003",prompt=text,temperature=0.6,max_tokens=1500)
    return response.choices[0].text

myQuestion=[]
myQuestion=st.text_input("Step 2:  type your question below:")

with st.expander("Optoinal: click here to see your question."):
    st.write(myQuestion)

with st.expander("Step 3: Get your answer"):
    if len(myKey)>5:
        openai.api_key = myKey
        st.balloons()
        st.write(askGPT(myQuestion))
    else:
        st.write("Error message: No API entered  or a wrong one!")
        
