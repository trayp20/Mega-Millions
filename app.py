import streamlit as st
import numpy as np
import tensorflow as tf

# --- 1. Load model once at start
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("megaball_model.keras")

model = load_model()

st.title("🎲 Mega Millions Mega Ball Predictor")

# --- 2. User input: select exactly 5 white balls
st.sidebar.header("Pick 5 white balls")
white_balls = st.sidebar.multiselect(
    "Select exactly five numbers (1–75):",
    list(range(1, 76)),
    default=[1, 2, 3, 4, 5]
)

# Disable predict button until input valid
predict = st.sidebar.button("Predict Mega Ball")

if predict:
    if len(white_balls) != 5:
        st.error("❗️ Please select exactly 5 white-ball numbers.")
    else:
        # --- 3. Build multi-hot input
        max_white = 75
        x = np.zeros((1, max_white), dtype=int)
        for n in white_balls:
            x[0, n-1] = 1

        # --- 4. Predict
        probs = model.predict(x)[0]         # shape (num_mega,)
        pred_idx = np.argmax(probs)         # 0-based
        pred_ball = pred_idx + 1            # back to 1–num_mega

        # --- 5. Display results
        st.subheader(f"🔮 Predicted Mega Ball: {pred_ball}")
        st.write("Probability distribution:")
        st.bar_chart(probs)
