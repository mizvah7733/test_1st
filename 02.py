# Streamlit 라이브러리
#    데이터분석에 특화되어 있고, 웹에 대한 기반 지식이 없어도 손쉽게 데이터 웹 대시보드를 제작할 수 있는 라이브러리

# title, header, subheader
import streamlit as st

st.title('This is title')
st.header('This is header')
st.subheader('This is subheader')

# markdown
st.markdown(
    '''
   This is main text.
   This is how to change the color of text :red[Red,] :blue[Blue,] :green[Green,]
   Tihs is **Bold** and *Italic* text
   '''
)
# 터미널 종료는 윈도우 ctrl + c, 맥 command + c

# text
st.text(
    '''
   This is main text.
   This is how to change the color of text :red[Red,] :blue[Blue,] :green[Green,]
   Tihs is **Bold** and *Italic* text
   '''
)

st.title('Title 1')
st.text('Text body 1')

st.divider()

st.title('Title 2')
st.text('Text body 2')

# py 파일 저장 ctrl + s
# 크롬에서 새로고침(F5)