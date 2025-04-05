import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮")

st.title("✂️ Rock Paper Scissors Game 🪨")

st.write("Play against the computer! Choose Rock, Paper, or Scissors below:")

choices = ["Rock", "Paper", "Scissors"]
user_choice = st.selectbox("Your choice:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write(f"🤖 Computer chose: **{computer_choice}**")

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You win!"
    else:
        result = "😢 You lose!"

    st.subheader(result)

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
