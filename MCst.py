import streamlit as st
from datetime import date, timedelta
import time
import streamlit.components.v1 as components

st.set_page_config(
page_title="MangoVirus",
page_icon="🥭",
layout="wide",
initial_sidebar_state="collapsed", #expanded/collapsed
menu_items={
         'Get Help': 'https://www.google.com/',
         'Report a bug': "https://www.google.com/",
         'About': "# ХУЙ"
     })
menu = st.sidebar.selectbox(
     'Меню',
     ('Стартовая страница','Маджестики'))
hour_count=0
if menu=='Стартовая страница':
    '''Привет)'''
if menu=='Маджестики':

    vip=0
    hour=0
    lvl_now = st.number_input('Ваш LVL')
    next_lvl_exp = lvl_now * 4 + 4
    next_lvl= lvl_now+1
    exp_now=st.number_input('Кол-во респектов')
    exp_now_count=exp_now
    mc_now= st.number_input('Cколько у вас Маджестиков')
    mc_now_count=mc_now
    wish=st.number_input('Желаемое кол-во Маджестиков')
    genre = st.radio(
        "Есть ли у вас Платинум ВИП?",
        ('Да', 'Нет'))
    if genre=='Да':
        vip=2
    elif genre=='Нет':
        vip=1
    i = 0
    exp_fin=0
    while mc_now_count < wish:
        hour = ((((lvl_now + i) * 4 + 4)-exp_now_count) // vip) + hour
        exp_now_count=0
        MCday = hour // 5
        if wish<mc_now_count+MCday*200:
            need=wish-mc_now_count
            if need%200==0:
                mc_now_count+=need
            else:
                need+=100
                mc_now_count+=need
            hour_count+=need//200*5
            exp_fin+=(need//200*5)//vip
            break
        hour_count += hour
        hour = hour % 5
        mc_now_count += MCday * 200
        MCday = 0
        if next_lvl == 5:
            mc_now_count += 500
        elif next_lvl == 10:
            mc_now_count += 1000
        elif next_lvl == 15:
            mc_now_count += 2000
        elif next_lvl == 20:
            mc_now_count += 3000
        elif next_lvl == 25:
            mc_now_count += 4000
        elif next_lvl == 30:
            mc_now_count += 5000
        elif next_lvl > 30:
            mc_now_count += 1500
        i += 1

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Ваш lvl", lvl_now)
        col2.metric("Маджестики",mc_now)
        col3.metric("Желаемое кол-во MC",wish)
    with st.container():
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric("Опыта до след lvl",next_lvl_exp)
        col2.metric("Часов до цели",hour_count)
        col3.metric("Итог Exp", str(exp_fin) + '/' + str((lvl_now + i) * 4 + 4))
        col4.metric("Итог Лвл",lvl_now+i)
    if st.button('Обновить данные'):
        with st.spinner('Wait for it...'):
            time.sleep(5)

        st.success('Данные обновлены!')
