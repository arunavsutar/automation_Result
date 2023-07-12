import streamlit as st
import pandas as pd
import data


def main():
    st.set_page_config(layout='wide', page_title="Student's Result")
    st.title("Student's Result")

    #############################################
    st.sidebar.title("Enter Details")
    name = st.sidebar.text_input("Enter your name:-")
    reg = st.sidebar.text_input("Enter Registration no:-")
    rng = st.sidebar.text_input("Enter the range:-")
    btn1 = st.sidebar.button("Result")
    if btn1:
        if (reg.isdigit() and rng.isdigit()):
            # pass the arguments to the method:
            df = data.get_data(int(reg), int(rng))
            st.dataframe(df)
        else:
            st.write(
                "Hello {} Input the Registration no. and the range in correct format.".format(name))


if __name__ == "__main__":
    main()
