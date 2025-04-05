import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="🎮")

st.title("✂️ Rock Paper Scissors Game 🪨")
st.write("Choose Rock, Paper, or Scissors and see who wins!")

# Images for each choice
emoji_map = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

choices = list(emoji_map.keys())
user_choice = st.selectbox("Your choice:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    
    st.markdown(f"### 🤖 Computer chose:")
    st.markdown(f"<div style='font-size:60px'>{emoji_map[computer_choice]}</div>", unsafe_allow_html=True)

    st.markdown(f"### 🧑 You chose:")
    st.markdown(f"<div style='font-size:60px'>{emoji_map[user_choice]}</div>", unsafe_allow_html=True)

    # Game logic
    if user_choice == computer_choice:
        result = "😐 It's a tie!"
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


   
