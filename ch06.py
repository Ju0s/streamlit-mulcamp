# -*- coding:utf-8 -*-

import streamlit as st
import matplotlib.pyplot as plt


def main():
    value1 = st.slider("숫자 선택", 0, 100)
    # st.write(value1)
    st.sidebar.write(value1)

    value2 = st.sidebar.slider("숫자 선택(sidebar)", 0, 100)
    # st.sidebar.write(value2)
    st.write(value2)

    with st.sidebar:
        # 데코레이터: 음식 서빙이 종료되고 나면 / 웨이터 처음부터 세팅
        value3 = st.slider("숫자 선택, with sidebar", 0, 100)
        st.write(value3)

        st.markdown("Matplotlib")
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        st.pyplot(fig)

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3])
    st.pyplot(fig)

if __name__ == "__main__":
    main()