import streamlit as st
from src.password_generator import (
    PincodeGenerator,
    RandomPasswordGenerator,
    MemorablePasswordGenerator
)

st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

st.title("🔐 Password Generator")
option = st.selectbox("Choose Password Type", ["Random Password", "Memorable Password", "PIN Code"])

# ---------------- PIN CODE ----------------
if option == "PIN Code":
    st.header("🔢 PIN Code Generator")
    length = st.slider("Length", 4, 12, 6)
    if st.button("Generate PIN Code"):
        generator = PincodeGenerator(length)
        pin = generator.generate_password()
        st.success(f"✅ Generated PIN: `{pin}`")

# ---------------- RANDOM PASSWORD ----------------
elif option == "Random Password":
    st.header("🔑 Random Password Generator")
    length = st.slider("Length", 6, 24, 12)
    symbol = st.checkbox("Include Symbols", True)
    number = st.checkbox("Include Numbers", True)
    if st.button("Generate Random Password"):
        generator = RandomPasswordGenerator(length, symbol, number)
        password = generator.generate_password()
        st.success(f"✅ Generated Password:\n\n`{password}`")

# ---------------- MEMORABLE PASSWORD ----------------
else:
    st.header("🧠 Memorable Password Generator")
    word_count = st.slider("Word Count", 2, 6, 4)
    separator = st.text_input("Separator", "-")
    capitalize = st.checkbox("Capitalize Words", True)
    if st.button("Generate Memorable Password"):
        generator = MemorablePasswordGenerator(word_count, separator, capitalize)
        password = generator.generate_password()
        st.success(f"✅ Generated Password:\n\n`{password}`")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("👨‍💻 Developed by **Amirmohammad Barari**")
st.caption("Built with ❤️ using Streamlit and Python 3.9+")
