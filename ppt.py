import streamlit as st

# App configuration
st.set_page_config(page_title="PoliScope", layout="wide", page_icon="📊")

# Session state for navigation
if 'slide' not in st.session_state:
    st.session_state.slide = 1

# Navigation buttons
def next_slide():
    if st.session_state.slide < 8:
        st.session_state.slide += 1

def prev_slide():
    if st.session_state.slide > 1:
        st.session_state.slide -= 1

# Title Slide
if st.session_state.slide == 1:
    st.markdown(
        """
        <div style='text-align:center; background:linear-gradient(90deg,#e3f2fd,#fff); padding:32px; border-radius:16px; box-shadow:0 2px 8px #bbb;'>
            <h1 style='font-size:2em; color:#1565c0; margin-bottom:0.2em;'>📘 Public Services Policy Impact Summarizer</h1>
            <h2 style='font-size:1.5em; color:#263238; margin-top:0;'>Leveraging <span style='color:#1976d2;'>AI</span> to Simplify Policy Impact Analysis</h2>
            <div style='font-size:1.2em; color:#37474f; margin-top:1em;'>
                <b style='color:#1976d2;'>Team Name:</b> AI Fridays - Team12<br>
                <b style='color:#1976d2;'>Members:</b> Sameer, Pranoy, Anirudh, Pankaj, Rakha<br>
                <b style='color:#1976d2;'>Event Date:</b> 19 Sept 2025
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Slide 2 - Problem Context
elif st.session_state.slide == 2:
    st.markdown(
        """
        <div style='background:#f5f5f5; padding:28px; border-radius:14px; box-shadow:0 2px 8px #ccc;'>
            <h2 style='font-size:1.5em; color:#d84315;'>🔍 The Challenge in Policy Analysis</h2>
            <div style='font-size:1.2em; color:#263238;'>
                <span style='color:#1565c0;'>📄</span> Policymakers deal with <span style='color:#d84315;'>overwhelming volumes</span> of documents<br>
                <span style='color:#1565c0;'>⏱️</span> Time-consuming to assess service and stakeholder impacts<br>
                <span style='color:#d84315;'>❗</span> Need for <b style='color:#1976d2;'>clear, concise summaries</b> for faster decisions<br><br>
                <i style='color:#388e3c;'>Why it matters: Efficient policy understanding leads to better public outcomes.</i>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Slide 3 - Solution Overview
elif st.session_state.slide == 3:
    st.markdown(
        """
        <div style='background:#e3f2fd; padding:28px; border-radius:14px; box-shadow:0 2px 8px #bbb;'>
            <h2 style='font-size:1.5em; color:#1976d2;'>💡 Our AI-Powered Solution</h2>
            <div style='font-size:1.2em; color:#263238;'>
                <span style='color:#1976d2;'>🤖</span> <b>Approach:</b> NLP to extract & summarize policy impact<br>
                <span style='color:#1976d2;'>🧠</span> <b>Model:</b> Trained Agent & gpt4o<br>
                <span style='color:#1976d2;'>🛠️</span> <b>Tools:</b> Python, React, LLM<br>
                <span style='color:#1976d2;'>✨</span> <b>Innovation:</b> AI Powered ChatBot for Q&A on policy impacts
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Slide 4 - Demo Walkthrough
elif st.session_state.slide == 4:
    st.markdown(
        """
        <div style='background:#fffde7; padding:28px; border-radius:14px; box-shadow:0 2px 8px #ccc;'>
            <h2 style='font-size:1.5em; color:#fbc02d;'>🚀 Live Demo Flow</h2>
            <div style='font-size:1.2em; color:#263238;'>
                <b style='color:#1976d2;'>1.</b> 📤 Upload policy PDFs<br>
                <b style='color:#1976d2;'>2.</b> 🧠 AI agent analyze document<br>
                <b style='color:#1976d2;'>3.</b> 📝 Outputs key impacts on services & stakeholders<br>
                <b style='color:#1976d2;'>4.</b> 💬 Interactive Q&A module responds to follow-up queries<br><br>
                <i style='color:#388e3c;'>Focus: <b style='color:#1976d2;'>Ease of use</b>, <b style='color:#1976d2;'>Speed</b>, <b style='color:#1976d2;'>Impactful insights</b></i>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Slide 5 - Results & Metrics
elif st.session_state.slide == 5:
    st.markdown(
        """
        <div style='background:#e8f5e9; padding:28px; border-radius:14px; box-shadow:0 2px 8px #bbb;'>
            <h2 style='font-size:1.5em; color:#388e3c;'>📊 Results & Metrics</h2>
            <div style='font-size:1.2em; color:#263238;'>
                <span style='color:#388e3c;'>✅</span> <b>85-90% accuracy</b> on impact extraction (validated sample)<br>
                <span style='color:#388e3c;'>⏳</span> <b>Time saved:</b> up to <b>70%</b> in policy reviews<br>
                <span style='color:#388e3c;'>👍</span> Positive feedback from initial pilot users<br>
                <span style='color:#388e3c;'>📊</span> Stakeholder-level impact analytics<br>
                <span style='color:#388e3c;'>🔗</span> Integration with policy databases
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Slide 6 - Conclusion
elif st.session_state.slide == 6:
    st.markdown(
        """
        <div style='background:#f3e5f5; padding:28px; border-radius:14px; box-shadow:0 2px 8px #bbb;'>
            <h2 style='font-size:1.5em; color:#8e24aa;'>✅ Summary & Future Directions</h2>
            <div style='font-size:1.2em; color:#263238;'>
                <span style='color:#8e24aa;'>🧠</span> Our summarizer simplifies complex policy analysis<br>
                <span style='color:#8e24aa;'>🌐</span> <b>Future Enhancements:</b><br>
                &nbsp;&nbsp;- Easily extendable to multiple policy domains<br>
                &nbsp;&nbsp;- Multilingual policy support<br>
                &nbsp;&nbsp; <br>
                &nbsp;&nbsp; 
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Slide 7 - Q&A
elif st.session_state.slide == 7:
    st.markdown(
        """
        <div style='background:#e1f5fe; padding:28px; border-radius:14px; box-shadow:0 2px 8px #bbb;'>
            <h2 style='font-size:1.5em; color:#0288d1;'>❓ Q&A Time</h2>
            <div style='font-size:1.2em; color:#263238;'>
                We’re happy to take your questions now!<br>
                <hr style='border:1px solid #0288d1;'>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Slide 8 - Thank You
elif st.session_state.slide == 8:
    st.markdown(
        """
        <div style='background:#e8f5e9; padding:36px; border-radius:18px; box-shadow:0 2px 12px #bbb; text-align:center;'>
            <h2 style='font-size:2em; color:#388e3c; margin-bottom:0.5em;'>✅ Thank You :)</h2>
           
        </div>
        """,
        unsafe_allow_html=True
    )

# Navigation Buttons
st.markdown("<br>", unsafe_allow_html=True)  # Add space above the buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    prev_disabled = st.session_state.slide == 1
    st.button("⬅️ Previous", on_click=prev_slide, disabled=prev_disabled)
with col2:
    st.markdown(f"<div style='text-align:center; font-size:1.2em; color:#1976d2;'>Slide {st.session_state.slide} of 8</div>", unsafe_allow_html=True)
with col3:
    next_disabled = st.session_state.slide == 8
    st.button("Next ➡️", on_click=next_slide, disabled=next_disabled)
