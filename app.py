import streamlit as st

st.set_page_config(
    page_title="BH Student Wellness App",
    page_icon="🌿",
    layout="wide"
)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
}
[data-testid="stSidebar"] * {
    color: white !important;
}
.sidebar-logo {
    text-align: center;
    padding: 20px 10px 10px 10px;
    border-bottom: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 20px;
}
.sidebar-logo h2 {
    color: white !important;
    font-size: 1.4em;
    margin: 8px 0 4px 0;
}
.sidebar-logo p {
    color: rgba(255,255,255,0.6) !important;
    font-size: 0.82em;
    margin: 0;
}
.nav-button {
    display: block;
    width: 100%;
    padding: 12px 16px;
    margin-bottom: 6px;
    border-radius: 10px;
    border: none;
    background: transparent;
    color: rgba(255,255,255,0.75) !important;
    font-size: 0.95em;
    text-align: left;
    cursor: pointer;
    transition: all 0.2s ease;
}
.nav-button:hover {
    background: rgba(255,255,255,0.12);
    color: white !important;
}
.nav-button.active {
    background: rgba(255,255,255,0.2);
    color: white !important;
    font-weight: 600;
    border-left: 3px solid #43cea2;
}
.sidebar-footer {
    position: fixed;
    bottom: 20px;
    left: 0;
    width: 18rem;
    text-align: center;
    padding: 12px;
    border-top: 1px solid rgba(255,255,255,0.15);
}
.sidebar-footer p {
    color: rgba(255,255,255,0.45) !important;
    font-size: 0.78em;
    margin: 0;
}
div[data-testid="stSidebar"] .stRadio > label {
    display: none;
}
div[data-testid="stSidebar"] .stRadio > div {
    gap: 4px;
}
div[data-testid="stSidebar"] .stRadio div[role="radio"] {
    background: transparent;
    border: none;
    border-radius: 10px;
    padding: 10px 16px;
    color: rgba(255,255,255,0.75) !important;
    font-size: 0.95em;
    transition: all 0.2s ease;
    cursor: pointer;
}
div[data-testid="stSidebar"] .stRadio div[role="radio"]:hover {
    background: rgba(255,255,255,0.1);
    color: white !important;
}
div[data-testid="stSidebar"] .stRadio div[role="radio"][aria-checked="true"] {
    background: rgba(255,255,255,0.18);
    color: white !important;
    font-weight: 600;
    border-left: 3px solid #43cea2;
    border-radius: 0 10px 10px 0;
}
div[data-testid="stSidebar"] .stRadio div[role="radio"] p {
    color: inherit !important;
    font-size: 1em;
}
div[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: rgba(255,255,255,0.45) !important;
    font-size: 0.78em;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="sidebar-logo">
    <div style="font-size: 2.4em;">🌿</div>
    <h2>BH Wellness</h2>
    <p>Your daily college companion</p>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "",
    [
        "🏠 Home",
        "📋 Daily Check-In",
        "🌱 8 Wellness Pillars",
        "⚡ Stressor Topics",
        "🧘 Yoga and Meditation",
        "📚 Resource Hub",
        "📈 Progress Tracker"
    ]
)

st.sidebar.markdown("""
<div class="sidebar-footer">
    <p>Made for BH Students</p>
    <p style="margin-top: 4px;">Powered by Python</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.info("Built for BH Students by BH Students")

if page == "🏠 Home":

    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
        border-radius: 20px;
        padding: 50px 40px;
        text-align: center;
        margin-bottom: 30px;
    }
    .hero h1 { color: white; font-size: 2.8em; margin-bottom: 10px; }
    .hero p { color: rgba(255,255,255,0.85); font-size: 1.2em; margin: 0; }
    .nav-card {
        background: #f8fafc;
        border-radius: 16px;
        padding: 24px 20px;
        border: 1px solid #e2e8f0;
        text-align: center;
        height: 100%;
        transition: all 0.2s ease;
    }
    .nav-card h4 { margin: 12px 0 8px 0; font-size: 1.1em; color: #1a1a2e; }
    .nav-card p { color: #666; font-size: 0.9em; margin: 0; }
    .nav-icon { font-size: 2.2em; }
    .quote-box {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 16px;
        padding: 30px 36px;
        text-align: center;
        margin-top: 10px;
    }
    .quote-box p { color: white; font-size: 1.2em; font-style: italic; margin: 0; }
    .quote-box span { color: rgba(255,255,255,0.75); font-size: 0.9em; margin-top: 10px; display: block; }
    .section-label {
        font-size: 1.4em;
        font-weight: 700;
        color: #1a1a2e;
        margin: 30px 0 16px 0;
    }
    .welcome-card {
        background: #f0f7ff;
        border-left: 6px solid #4a90d9;
        border-radius: 12px;
        padding: 24px 28px;
        margin-bottom: 30px;
    }
    .welcome-card p { color: #1a1a2e; font-size: 1.05em; line-height: 1.7; margin: 0; }
    </style>

    <div class="hero">
        <h1>🌿 BH Student Wellness App</h1>
        <p>Your daily guide to thriving in college — mind, body, and beyond.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="welcome-card">
        <p>
        College can be exciting, overwhelming, and everything in between.
        This app was built specifically for <strong>BH students</strong> to help you manage stress,
        build healthy habits, and find balance across all areas of your life.
        Whether you are just starting out, navigating student organizations, or preparing for
        internships — <strong>you have got support here.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">🗺️ What would you like to do today?</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-icon">📋</div>
            <h4>Daily Check-In</h4>
            <p>Log your mood and set a wellness focus for today.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(" ")
        if st.button("Go to Check-In", use_container_width=True):
            st.info("Select Daily Check-In from the sidebar!")

    with col2:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-icon">🌱</div>
            <h4>8 Wellness Pillars</h4>
            <p>Explore tips across all 8 dimensions of wellness.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(" ")
        if st.button("Explore Wellness", use_container_width=True):
            st.info("Select 8 Wellness Pillars from the sidebar!")

    with col3:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-icon">🧘</div>
            <h4>Yoga and Meditation</h4>
            <p>Find guided sessions to calm your mind and body.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(" ")
        if st.button("Start a Session", use_container_width=True):
            st.info("Select Yoga and Meditation from the sidebar!")

    st.markdown(" ")
    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-icon">⚡</div>
            <h4>Stressor Topics</h4>
            <p>Get actionable tips for your specific college challenges.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(" ")
        if st.button("View Stressors", use_container_width=True):
            st.info("Select Stressor Topics from the sidebar!")

    with col5:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-icon">📚</div>
            <h4>Resource Hub</h4>
            <p>Find campus resources, contacts, and support links.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(" ")
        if st.button("Find Resources", use_container_width=True):
            st.info("Select Resource Hub from the sidebar!")

    with col6:
        st.markdown("""
        <div class="nav-card">
            <div class="nav-icon">📈</div>
            <h4>Progress Tracker</h4>
            <p>View your wellness streaks and mood over time.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(" ")
        if st.button("See My Progress", use_container_width=True):
            st.info("Select Progress Tracker from the sidebar!")

    st.markdown(" ")
    st.markdown("""
    <div class="quote-box">
        <p>"You don't have to be perfect to be amazing. Take it one day at a time."</p>
        <span>— Daily Reminder for BH Students 🌟</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(" ")
    st.caption("BH Student Wellness App · Made with care for BH Students")

elif page == "📋 Daily Check-In":

    st.markdown("""
    <style>
    .checkin-hero {
        background: linear-gradient(135deg, #f093fb, #f5576c);
        border-radius: 20px;
        padding: 36px 40px;
        margin-bottom: 28px;
        text-align: center;
    }
    .checkin-hero h1 { color: white; font-size: 2.2em; margin: 0 0 8px 0; }
    .checkin-hero p { color: rgba(255,255,255,0.9); font-size: 1.1em; margin: 0; }
    .checkin-card {
        background: #f8fafc;
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    .checkin-card h3 { margin-top: 0; color: #1a1a2e; font-size: 1.15em; }
    .mood-display {
        border-radius: 12px;
        padding: 16px 20px;
        margin-top: 12px;
        font-weight: 600;
        text-align: center;
        font-size: 1.05em;
    }
    .save-banner {
        background: linear-gradient(135deg, #43cea2, #185a9d);
        border-radius: 14px;
        padding: 24px 28px;
        text-align: center;
        color: white;
        margin-top: 10px;
    }
    .save-banner h3 { color: white; margin: 0 0 6px 0; }
    .save-banner p { color: rgba(255,255,255,0.9); margin: 0; font-size: 0.95em; }
    </style>

    <div class="checkin-hero">
        <h1>📋 Daily Check-In</h1>
        <p>Take a moment to check in with yourself. You deserve it.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="checkin-card">
        <h3>😊 How is your mood right now?</h3>
        <p style="color: #666; margin: 0 0 12px 0;">Slide to rate your current mood honestly — no wrong answers.</p>
    </div>
    """, unsafe_allow_html=True)

    mood = st.slider("Rate your mood from 1 (struggling) to 5 (great)", 1, 5, 3)

    mood_config = {
        1: ("#fee2e2", "#991b1b", "😔  That sounds really tough. Let's find something to help you today."),
        2: ("#fef3c7", "#92400e", "😟  Hang in there. Small steps make a big difference."),
        3: ("#e0f2fe", "#0369a1", "😐  Not bad! Let's help you make today a little better."),
        4: ("#dcfce7", "#166534", "😊  Doing well! Keep that momentum going."),
        5: ("#f0fdf4", "#14532d", "🌟  Amazing! Let's keep that energy up today.")
    }

    bg, color, message = mood_config[mood]
    st.markdown(f"""
    <div class="mood-display" style="background: {bg}; color: {color};">
        {message}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown("""
    <div class="checkin-card">
        <h3>🎯 What is your biggest focus today?</h3>
        <p style="color: #666; margin: 0;">Pick the wellness area you want to prioritize. We will pull up personalized tips for you.</p>
    </div>
    """, unsafe_allow_html=True)

    focus = st.selectbox("Pick one area:", [
        "Physical wellness",
        "Emotional wellness",
        "Social wellness",
        "Intellectual wellness",
        "Occupational wellness",
        "Spiritual wellness",
        "Environmental wellness",
        "Financial wellness"
    ])

    st.markdown(" ")
    st.markdown("""
    <div class="checkin-card">
        <h3>✏️ Set one small goal for today</h3>
        <p style="color: #666; margin: 0;">Keep it simple and achievable — one meaningful step is enough.</p>
    </div>
    """, unsafe_allow_html=True)

    goal = st.text_input("My goal today is...")

    st.markdown(" ")

    if st.button("Save My Check-In", use_container_width=True):
        if goal == "":
            st.warning("Please enter a goal before saving!")
        else:
            import json
            import os
            from datetime import date

            entry = {
                "date": str(date.today()),
                "mood": mood,
                "focus": focus,
                "goal": goal
            }

            filepath = "data/checkins.json"

            if os.path.exists(filepath):
                with open(filepath, "r") as f:
                    all_entries = json.load(f)
            else:
                all_entries = []

            all_entries.append(entry)

            with open(filepath, "w") as f:
                json.dump(all_entries, f, indent=4)

            pillar_map = {
                "Physical wellness": "Physical",
                "Emotional wellness": "Emotional",
                "Social wellness": "Social",
                "Intellectual wellness": "Intellectual",
                "Occupational wellness": "Occupational",
                "Spiritual wellness": "Spiritual",
                "Environmental wellness": "Environmental",
                "Financial wellness": "Financial"
            }

            st.session_state["wellness_pillar"] = pillar_map[focus]

            st.markdown("""
            <div class="save-banner">
                <h3>Check-in saved!</h3>
                <p>Great job showing up for yourself today. Head to 8 Wellness Pillars in the sidebar for your personalized tips.</p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()

elif page == "🌱 8 Wellness Pillars":
    st.title("8 Wellness Pillars")

    CARD_STYLE = """
    <style>
    .pillar-header {
        border-radius: 16px;
        padding: 30px;
        color: white;
        margin-bottom: 24px;
    }
    .pillar-header h1 { color: white; margin: 0; font-size: 2em; }
    .pillar-header p { color: rgba(255,255,255,0.9); margin: 8px 0 0 0; font-size: 1.1em; }
    .section-card {
        background: #f8fafc;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    .section-card h3 { margin-top: 0; }
    .tip-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px; }
    .tip-item {
        background: white;
        border-radius: 10px;
        padding: 14px 16px;
        border: 1px solid #e2e8f0;
        font-size: 0.95em;
        display: flex;
        align-items: flex-start;
        gap: 10px;
    }
    .tip-icon { font-size: 1.3em; flex-shrink: 0; }
    .quick-win {
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 20px;
    }
    .quick-win h3 { margin-top: 0; }
    .resource-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px; }
    .resource-card {
        background: white;
        border-radius: 10px;
        padding: 14px 16px;
        border: 1px solid #e2e8f0;
    }
    .resource-card a { font-weight: 600; text-decoration: none; font-size: 0.95em; }
    .resource-card p { color: #666; font-size: 0.85em; margin: 4px 0 0 0; }
    </style>
    """
    st.markdown(CARD_STYLE, unsafe_allow_html=True)

    st.subheader("Choose a pillar to explore tips, strategies, and resources.")
    st.markdown("---")

    st.markdown("""
    <style>
    div.stButton > button {
        background-color: #f0f4f8;
        color: #1a1a2e;
        border: 2px solid #c9d6df;
        border-radius: 12px;
        padding: 18px 10px;
        font-size: 15px;
        font-weight: 600;
        transition: all 0.2s ease;
        margin-bottom: 10px;
    }
    div.stButton > button:hover {
        background-color: #4a90d9;
        color: white;
        border-color: #4a90d9;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(74, 144, 217, 0.3);
    }
    div.stButton > button:active {
        background-color: #357abd;
        transform: translateY(0px);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("### Select a Wellness Pillar:")
    st.markdown(" ")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🏃 Physical", use_container_width=True):
            st.session_state["pillar"] = "Physical"
        if st.button("🤝 Social", use_container_width=True):
            st.session_state["pillar"] = "Social"
    with col2:
        if st.button("💛 Emotional", use_container_width=True):
            st.session_state["pillar"] = "Emotional"
        if st.button("💡 Intellectual", use_container_width=True):
            st.session_state["pillar"] = "Intellectual"
    with col3:
        if st.button("💼 Occupational", use_container_width=True):
            st.session_state["pillar"] = "Occupational"
        if st.button("🌿 Environmental", use_container_width=True):
            st.session_state["pillar"] = "Environmental"
    with col4:
        if st.button("🕊️ Spiritual", use_container_width=True):
            st.session_state["pillar"] = "Spiritual"
        if st.button("💰 Financial", use_container_width=True):
            st.session_state["pillar"] = "Financial"

    st.markdown("---")

    if "wellness_pillar" in st.session_state:
        pillar = st.session_state["wellness_pillar"]
        del st.session_state["wellness_pillar"]
    elif "pillar" in st.session_state:
        pillar = st.session_state["pillar"]
    else:
        pillar = None

    if pillar is None:
        st.info("Select a pillar above to get started!")
        st.stop()

    if "wellness_pillar" in st.session_state:
        pillar = st.session_state["wellness_pillar"]
        del st.session_state["wellness_pillar"]

    st.markdown("---")

    if pillar == "Physical":
        st.markdown("""
        <div class="pillar-header" style="background: linear-gradient(135deg, #43cea2, #185a9d);">
            <h1>🏃 Physical Wellness</h1>
            <p>Take care of your body through movement, sleep, and nutrition.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #185a9d;">Why it matters</h3>
            <p>Regular physical activity reduces stress hormones like cortisol, improves sleep quality,
            boosts energy, and sharpens focus. Even small amounts of movement make a measurable
            difference in how you feel day to day.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #185a9d;">Tips for BH Students</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">🚶</span><span>Aim for 30 minutes of movement per day — a walk between classes counts.</span></div>
                <div class="tip-item"><span class="tip-icon">🏋️</span><span>Use the campus rec center during off-peak hours to avoid crowds.</span></div>
                <div class="tip-item"><span class="tip-icon">😴</span><span>Sleep 7 to 9 hours per night. Poor sleep makes every stressor worse.</span></div>
                <div class="tip-item"><span class="tip-icon">💧</span><span>Stay hydrated — keep a water bottle with you during class.</span></div>
                <div class="tip-item"><span class="tip-icon">🥗</span><span>Eat at least one balanced meal per day even on your busiest days.</span></div>
                <div class="tip-item"><span class="tip-icon">🧘</span><span>Stretch for 5 to 10 minutes before bed to release tension.</span></div>
                <div class="tip-item"><span class="tip-icon">🚪</span><span>Take stairs and walk to class instead of driving when possible.</span></div>
                <div class="tip-item"><span class="tip-icon">📵</span><span>Set a no-phone rule 30 minutes before bed to improve sleep quality.</span></div>
            </div>
        </div>

        <div class="quick-win" style="background: linear-gradient(135deg, #f6d365, #fda085); color: #4a1a00;">
            <h3 style="color: #4a1a00;">⚡ Quick Win You Can Do Right Now</h3>
            <p>Take a 10 minute walk outside. Get off your phone, notice your surroundings, and breathe deeply. That is it — you just did something great for your body.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #185a9d;">Helpful Resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://www.cdc.gov/physicalactivity" target="_blank">CDC Physical Activity Guidelines</a><p>Official movement guidelines for young adults</p></div>
                <div class="resource-card"><a href="https://www.sleepfoundation.org/teens-and-sleep" target="_blank">Sleep Foundation</a><p>College students and sleep research</p></div>
                <div class="resource-card"><a href="https://www.myfitnesspal.com" target="_blank">MyFitnessPal</a><p>Free nutrition and activity tracker</p></div>
                <div class="resource-card"><a href="https://www.nike.com/ntc-app" target="_blank">Nike Training Club</a><p>Free guided workout app for all levels</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif pillar == "Emotional":
        st.markdown("""
        <div class="pillar-header" style="background: linear-gradient(135deg, #f093fb, #f5576c);">
            <h1>💛 Emotional Wellness</h1>
            <p>Understand, express, and manage your feelings in a healthy way.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #f5576c;">Why it matters</h3>
            <p>Students who develop emotional awareness are better equipped to handle academic pressure,
            relationship conflicts, and major life transitions. Ignoring your emotional health leads to
            burnout, isolation, and long-term mental health struggles.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #f5576c;">Tips for BH Students</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">🗣️</span><span>Name your emotions instead of suppressing them — awareness is the first step.</span></div>
                <div class="tip-item"><span class="tip-icon">📓</span><span>Journal for 5 minutes each day — just write what is on your mind.</span></div>
                <div class="tip-item"><span class="tip-icon">👥</span><span>Talk to someone you trust when something is bothering you.</span></div>
                <div class="tip-item"><span class="tip-icon">🚧</span><span>Set boundaries with people and commitments that drain your energy.</span></div>
                <div class="tip-item"><span class="tip-icon">💬</span><span>Practice self-compassion — talk to yourself like you would a close friend.</span></div>
                <div class="tip-item"><span class="tip-icon">🛑</span><span>Recognize when you are overwhelmed and give yourself permission to pause.</span></div>
                <div class="tip-item"><span class="tip-icon">📵</span><span>Limit social media if it makes you feel worse about yourself.</span></div>
                <div class="tip-item"><span class="tip-icon">🎨</span><span>Express yourself creatively — art, music, and writing all support emotional health.</span></div>
            </div>
        </div>

        <div class="quick-win" style="background: linear-gradient(135deg, #fbc2eb, #a18cd1); color: #2d004f;">
            <h3 style="color: #2d004f;">⚡ Quick Win You Can Do Right Now</h3>
            <p>Write down three things you are feeling right now without judging them. Then write one thing you are grateful for. This takes less than two minutes and shifts your mindset.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #f5576c;">Helpful Resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://www.crisistextline.org" target="_blank">Crisis Text Line</a><p>Text HOME to 741741 for free crisis support</p></div>
                <div class="resource-card"><a href="https://988lifeline.org" target="_blank">988 Suicide and Crisis Lifeline</a><p>Call or text 988 anytime</p></div>
                <div class="resource-card"><a href="https://www.calm.com" target="_blank">Calm App</a><p>Mood tracking and emotional wellness tools</p></div>
                <div class="resource-card"><a href="https://www.betterhelp.com" target="_blank">BetterHelp</a><p>Affordable online therapy for students</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif pillar == "Social":
        st.markdown("""
        <div class="pillar-header" style="background: linear-gradient(135deg, #4facfe, #00f2fe);">
            <h1>🤝 Social Wellness</h1>
            <p>Build meaningful relationships and feel connected to your community.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #0077cc;">Why it matters</h3>
            <p>Strong social connections are one of the biggest predictors of overall happiness and
            resilience. Students who feel socially connected perform better academically and are more
            likely to persist through challenges.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #0077cc;">Tips for BH Students</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">👋</span><span>Introduce yourself to at least one new person per week — a classmate or club member.</span></div>
                <div class="tip-item"><span class="tip-icon">🎯</span><span>Join one student organization that genuinely interests you.</span></div>
                <div class="tip-item"><span class="tip-icon">📅</span><span>Be consistent — show up to events even when you do not feel like it.</span></div>
                <div class="tip-item"><span class="tip-icon">📱</span><span>Put your phone down during meals and social situations.</span></div>
                <div class="tip-item"><span class="tip-icon">💌</span><span>Reach out to old friends and family regularly — do not let those bonds fade.</span></div>
                <div class="tip-item"><span class="tip-icon">🤲</span><span>Learn to resolve conflict directly and calmly rather than avoiding it.</span></div>
                <div class="tip-item"><span class="tip-icon">🧠</span><span>Do not compare your social life to what you see on social media.</span></div>
                <div class="tip-item"><span class="tip-icon">☕</span><span>Invite a classmate to study or grab coffee — small efforts build big friendships.</span></div>
            </div>
        </div>

        <div class="quick-win" style="background: linear-gradient(135deg, #4facfe, #00f2fe); color: #003366;">
            <h3 style="color: #003366;">⚡ Quick Win You Can Do Right Now</h3>
            <p>Text or call one friend or family member you have not talked to in a while. It takes two minutes and means more than you know.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #0077cc;">Helpful Resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://www.meetup.com" target="_blank">Meetup</a><p>Find local interest groups and events</p></div>
                <div class="resource-card"><a href="https://bumble.com/bff" target="_blank">Bumble BFF</a><p>Make new friends in your area</p></div>
                <div class="resource-card"><a href="https://greatergood.berkeley.edu" target="_blank">Greater Good Science Center</a><p>Research on social connection and happiness</p></div>
                <div class="resource-card"><a href="https://www.shortform.com/summary/how-to-win-friends-and-influence-people-summary" target="_blank">How to Win Friends — Summary</a><p>Dale Carnegie classic condensed</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif pillar == "Intellectual":
        st.markdown("""
        <div class="pillar-header" style="background: linear-gradient(135deg, #a18cd1, #fbc2eb);">
            <h1>💡 Intellectual Wellness</h1>
            <p>Engage your mind in creative, stimulating, and meaningful ways.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #6a0dad;">Why it matters</h3>
            <p>Students who pursue intellectual engagement outside of required coursework are more
            motivated, more creative, and better at problem solving. Intellectual wellness prevents
            academic burnout by making learning feel meaningful again.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #6a0dad;">Tips for BH Students</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">📚</span><span>Read something for fun every week — even 10 pages of a book you enjoy.</span></div>
                <div class="tip-item"><span class="tip-icon">🎙️</span><span>Listen to podcasts on topics completely outside your major.</span></div>
                <div class="tip-item"><span class="tip-icon">🎤</span><span>Attend a campus lecture or panel event at least once a month.</span></div>
                <div class="tip-item"><span class="tip-icon">🧠</span><span>Challenge yourself to form your own opinions rather than accepting what you are told.</span></div>
                <div class="tip-item"><span class="tip-icon">🛠️</span><span>Learn one new skill per semester unrelated to your coursework.</span></div>
                <div class="tip-item"><span class="tip-icon">✏️</span><span>Write, draw, or create something regularly — creativity is intellectual exercise.</span></div>
                <div class="tip-item"><span class="tip-icon">💬</span><span>Debate ideas with friends in a respectful and open-minded way.</span></div>
                <div class="tip-item"><span class="tip-icon">🌍</span><span>Explore topics from other cultures and perspectives intentionally.</span></div>
            </div>
        </div>

        <div class="quick-win" style="background: linear-gradient(135deg, #a18cd1, #fbc2eb); color: #2d004f;">
            <h3 style="color: #2d004f;">⚡ Quick Win You Can Do Right Now</h3>
            <p>Watch one TED Talk on a topic you know nothing about. Spend 5 minutes afterward writing down what surprised you most.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #6a0dad;">Helpful Resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://www.ted.com" target="_blank">TED Talks</a><p>Ideas worth spreading — free and vast library</p></div>
                <div class="resource-card"><a href="https://www.coursera.org" target="_blank">Coursera</a><p>Free online courses from top universities</p></div>
                <div class="resource-card"><a href="https://www.khanacademy.org" target="_blank">Khan Academy</a><p>Free learning on virtually any topic</p></div>
                <div class="resource-card"><a href="https://libbyapp.com" target="_blank">Libby App</a><p>Free ebooks and audiobooks via your library card</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif pillar == "Occupational":
        st.markdown("""
        <div class="pillar-header" style="background: linear-gradient(135deg, #f7971e, #ffd200);">
            <h1>💼 Occupational Wellness</h1>
            <p>Find purpose and build toward a career that aligns with your values.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #b35a00;">Why it matters</h3>
            <p>Students who develop occupational wellness early are more confident in interviews,
            more intentional about their choices, and less likely to experience post-graduation panic.
            Your time in college is your biggest opportunity to explore and build.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #b35a00;">Tips for BH Students</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">🏢</span><span>Visit your campus career center at least once per semester.</span></div>
                <div class="tip-item"><span class="tip-icon">📄</span><span>Update your resume and LinkedIn every time you gain a new experience.</span></div>
                <div class="tip-item"><span class="tip-icon">📬</span><span>Apply for internships early — many deadlines are in the fall for next summer.</span></div>
                <div class="tip-item"><span class="tip-icon">🤝</span><span>Say yes to informational interviews — they cost nothing and teach you everything.</span></div>
                <div class="tip-item"><span class="tip-icon">🧭</span><span>Find a mentor — a professor, advisor, or professional in your field.</span></div>
                <div class="tip-item"><span class="tip-icon">🔍</span><span>Explore multiple career paths rather than locking in too early.</span></div>
                <div class="tip-item"><span class="tip-icon">📧</span><span>Learn professional skills like email etiquette and public speaking now.</span></div>
                <div class="tip-item"><span class="tip-icon">🌐</span><span>Build an online presence that reflects your professional goals.</span></div>
            </div>
        </div>

        <div class="quick-win" style="background: linear-gradient(135deg, #f7971e, #ffd200); color: #3d1f00;">
            <h3 style="color: #3d1f00;">⚡ Quick Win You Can Do Right Now</h3>
            <p>Update your LinkedIn profile with your current school, major, and one extracurricular activity. Add a professional photo. It takes 10 minutes and opens real doors.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #b35a00;">Helpful Resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://www.linkedin.com" target="_blank">LinkedIn</a><p>Professional networking and job search</p></div>
                <div class="resource-card"><a href="https://joinhandshake.com" target="_blank">Handshake</a><p>College student internship and job platform</p></div>
                <div class="resource-card"><a href="https://biginterview.com" target="_blank">Big Interview</a><p>Practice your interview skills for free</p></div>
                <div class="resource-card"><a href="https://www.canva.com/resumes" target="_blank">Canva Resume Builder</a><p>Free professional resume templates</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif pillar == "Spiritual":
        st.markdown("""
        <div class="pillar-header" style="background: linear-gradient(135deg, #89f7fe, #66a6ff);">
            <h1>🕊️ Spiritual Wellness</h1>
            <p>Find meaning, purpose, and values that guide your daily life.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #0047ab;">Why it matters</h3>
            <p>Students with a strong sense of purpose are more resilient in the face of difficulty,
            more motivated in their studies, and more grounded during times of uncertainty.
            Spiritual wellness gives you an anchor when everything else feels chaotic.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #0047ab;">Tips for BH Students</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">🧭</span><span>Spend time identifying your core values — what matters most to you in life.</span></div>
                <div class="tip-item"><span class="tip-icon">🤲</span><span>Volunteer or give back in a way that feels meaningful to you.</span></div>
                <div class="tip-item"><span class="tip-icon">🧘</span><span>Practice mindfulness or meditation even for just 5 minutes a day.</span></div>
                <div class="tip-item"><span class="tip-icon">📖</span><span>Explore different philosophies and worldviews with an open mind.</span></div>
                <div class="tip-item"><span class="tip-icon">🌿</span><span>Spend time in nature — it naturally grounds your sense of perspective.</span></div>
                <div class="tip-item"><span class="tip-icon">🔄</span><span>Reflect on whether your daily actions align with your values and goals.</span></div>
                <div class="tip-item"><span class="tip-icon">✨</span><span>Surround yourself with people who inspire and challenge you to grow.</span></div>
                <div class="tip-item"><span class="tip-icon">🙏</span><span>Create a morning or evening ritual that helps you feel centered and grounded.</span></div>
            </div>
        </div>

        <div class="quick-win" style="background: linear-gradient(135deg, #89f7fe, #66a6ff); color: #002366;">
            <h3 style="color: #002366;">⚡ Quick Win You Can Do Right Now</h3>
            <p>Write down your top five personal values. Then ask yourself honestly — did my actions today reflect those values? No judgment, just awareness.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #0047ab;">Helpful Resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://insighttimer.com" target="_blank">Insight Timer</a><p>Free meditation and mindfulness app</p></div>
                <div class="resource-card"><a href="https://www.volunteermatch.org" target="_blank">Volunteer Match</a><p>Find meaningful volunteer opportunities</p></div>
                <div class="resource-card"><a href="https://www.theschooloflife.com" target="_blank">The School of Life</a><p>Resources on purpose and meaning</p></div>
                <div class="resource-card"><a href="https://ggia.berkeley.edu" target="_blank">Greater Good in Action</a><p>Science-based practices for finding meaning</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif pillar == "Environmental":
        st.markdown("""
        <div class="pillar-header" style="background: linear-gradient(135deg, #56ab2f, #a8e063);">
            <h1>🌿 Environmental Wellness</h1>
            <p>Create spaces around you that support your peace and productivity.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #2d6a00;">Why it matters</h3>
            <p>Cluttered, noisy, or unhealthy environments increase stress and reduce your ability to
            focus. Students who take ownership of their physical spaces feel more in control,
            more productive, and more at peace day to day.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #2d6a00;">Tips for BH Students</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">🧹</span><span>Keep your living space clean — even a quick tidy-up each morning sets a positive tone.</span></div>
                <div class="tip-item"><span class="tip-icon">🪴</span><span>Personalize your space with things that make you feel calm and inspired.</span></div>
                <div class="tip-item"><span class="tip-icon">📚</span><span>Find your best study environment and use it consistently.</span></div>
                <div class="tip-item"><span class="tip-icon">☀️</span><span>Spend at least 15 minutes outside each day — sunlight improves your mood.</span></div>
                <div class="tip-item"><span class="tip-icon">🗑️</span><span>Reduce clutter — physical clutter creates mental clutter.</span></div>
                <div class="tip-item"><span class="tip-icon">♻️</span><span>Be mindful of your environmental impact — recycle and reduce waste.</span></div>
                <div class="tip-item"><span class="tip-icon">🔊</span><span>Use noise-canceling headphones or white noise if your dorm is loud.</span></div>
                <div class="tip-item"><span class="tip-icon">💡</span><span>Use warm lighting in the evening to help your body wind down naturally.</span></div>
            </div>
        </div>

        <div class="quick-win" style="background: linear-gradient(135deg, #56ab2f, #a8e063); color: #0f2d00;">
            <h3 style="color: #0f2d00;">⚡ Quick Win You Can Do Right Now</h3>
            <p>Spend 10 minutes cleaning and organizing your desk or study space right now. Notice how your mind feels afterward — clearer space creates a clearer mind.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #2d6a00;">Helpful Resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://www.apartmenttherapy.com" target="_blank">Apartment Therapy</a><p>Small space organization and decor tips</p></div>
                <div class="resource-card"><a href="https://www.youtube.com/@LofiGirl" target="_blank">Lofi Girl</a><p>Free focus music for studying</p></div>
                <div class="resource-card"><a href="https://www.earthday.org" target="_blank">Earth Day Network</a><p>Environmental awareness and action</p></div>
                <div class="resource-card"><a href="https://www.inaturalist.org" target="_blank">iNaturalist</a><p>Connect with and explore the natural world</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif pillar == "Financial":
        st.markdown("""
        <div class="pillar-header" style="background: linear-gradient(135deg, #11998e, #38ef7d);">
            <h1>💰 Financial Wellness</h1>
            <p>Understand your money and build habits that set you up for stability.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #0a5c52;">Why it matters</h3>
            <p>Financial stress bleeds into every area of your life. Students who develop basic
            financial literacy in college graduate with less debt, more savings, and significantly
            less anxiety about their future.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #0a5c52;">Tips for BH Students</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">📊</span><span>Build a monthly budget using the 50/30/20 rule — needs, wants, savings.</span></div>
                <div class="tip-item"><span class="tip-icon">🧾</span><span>Track every purchase for one week — most people are shocked by what they find.</span></div>
                <div class="tip-item"><span class="tip-icon">🎓</span><span>Apply for every scholarship you are eligible for — thousands go unclaimed yearly.</span></div>
                <div class="tip-item"><span class="tip-icon">💳</span><span>Avoid credit card debt — if you use one, pay it off in full every month.</span></div>
                <div class="tip-item"><span class="tip-icon">🍳</span><span>Cook your own meals when possible — eating out drains a college budget fast.</span></div>
                <div class="tip-item"><span class="tip-icon">🏦</span><span>Build an emergency fund — even 500 dollars saved is a meaningful cushion.</span></div>
                <div class="tip-item"><span class="tip-icon">🏫</span><span>Talk to your financial aid office if you are struggling — they have options most students never ask about.</span></div>
                <div class="tip-item"><span class="tip-icon">📈</span><span>Open a savings account now and set up automatic transfers even if it is just 10 dollars a month.</span></div>
            </div>
        </div>

        <div class="quick-win" style="background: linear-gradient(135deg, #11998e, #38ef7d); color: #002d27;">
            <h3 style="color: #002d27;">⚡ Quick Win You Can Do Right Now</h3>
            <p>Download a free budgeting app and enter your income and three biggest monthly expenses. Just seeing the numbers clearly is the first and most important step.</p>
        </div>

        <div class="section-card">
            <h3 style="color: #0a5c52;">Helpful Resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://mint.intuit.com" target="_blank">Mint</a><p>Free budgeting and expense tracking app</p></div>
                <div class="resource-card"><a href="https://www.ynab.com" target="_blank">YNAB</a><p>You Need a Budget — popular student tool</p></div>
                <div class="resource-card"><a href="https://www.scholarships.com" target="_blank">Scholarships.com</a><p>Search thousands of available scholarships</p></div>
                <div class="resource-card"><a href="https://www.nerdwallet.com/college-finance" target="_blank">NerdWallet</a><p>Student financial guides and advice</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif page == "⚡ Stressor Topics":

    st.markdown("""
    <style>
    .stressor-hero {
        background: linear-gradient(135deg, #f7971e, #ffd200);
        border-radius: 20px;
        padding: 36px 40px;
        margin-bottom: 28px;
        text-align: center;
    }
    .stressor-hero h1 { color: #3d1f00; font-size: 2.2em; margin: 0 0 8px 0; }
    .stressor-hero p { color: rgba(61,31,0,0.8); font-size: 1.1em; margin: 0; }
    .stressor-section {
        background: #f8fafc;
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    .stressor-section h3 { margin-top: 0; font-size: 1.15em; }
    .tip-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-top: 12px;
    }
    .tip-item {
        background: white;
        border-radius: 10px;
        padding: 14px 16px;
        border: 1px solid #e2e8f0;
        font-size: 0.95em;
        display: flex;
        align-items: flex-start;
        gap: 10px;
        line-height: 1.5;
    }
    .tip-icon { font-size: 1.3em; flex-shrink: 0; }
    .highlight-box {
        border-radius: 14px;
        padding: 22px 26px;
        margin-bottom: 20px;
    }
    .highlight-box h3 { margin-top: 0; }
    .resource-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-top: 12px;
    }
    .resource-card {
        background: white;
        border-radius: 10px;
        padding: 14px 16px;
        border: 1px solid #e2e8f0;
    }
    .resource-card a { font-weight: 600; text-decoration: none; font-size: 0.95em; }
    .resource-card p { color: #666; font-size: 0.85em; margin: 4px 0 0 0; }
    .topic-btn-active {
        border-left: 3px solid #f7971e;
    }
    </style>

    <div class="stressor-hero">
        <h1>⚡ Stressor Topics</h1>
        <p>Real advice for the real challenges Business Honors students face at Texas A&M.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Select a topic:")
    st.markdown(" ")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🎒  First Week of College", use_container_width=True):
            st.session_state["stressor"] = "firstweek"
    with col2:
        if st.button("💼  Internship Recruiting", use_container_width=True):
            st.session_state["stressor"] = "internship"
    with col3:
        if st.button("🤝  Student Organizations", use_container_width=True):
            st.session_state["stressor"] = "orgs"

    st.markdown("---")

    if "stressor" not in st.session_state:
        st.markdown("""
        <div style="text-align:center; padding: 40px 20px; color: #888;">
            <div style="font-size: 2.5em;">👆</div>
            <p style="font-size: 1.05em; margin-top: 12px;">Select a topic above to get started.</p>
        </div>
        """, unsafe_allow_html=True)
        st.stop()

    topic = st.session_state["stressor"]

    if topic == "firstweek":

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">🎒 Your First Week as a Business Honors Aggie</h3>
            <p>
            Welcome to Texas A&M, one of the most tight knit and spirited universities in the country.
            Aggie culture is built on a deep sense of community, tradition, and genuine care for one another.
            You will quickly learn that being an Aggie means something special, and that extends directly
            into the Business Honors program. Your cohort of 80 to 100 fellow BH students will become
            some of your closest friends, study partners, and professional connections over the next four years.
            The first week sets the tone, so here is how to make the most of it.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">The most important thing you can do this week</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">🙋</span><span>Say yes to everything in the first month or two. Events, hangouts, study sessions, all of it. You can narrow down what you enjoy after you have actually tried things. The students who get the most out of BH are the ones who show up.</span></div>
                <div class="tip-item"><span class="tip-icon">🤝</span><span>Introduce yourself to as many cohort members as possible. These are the people you will be in classes and organizations with for the next four years. Investing in those relationships early pays off more than you can imagine right now.</span></div>
                <div class="tip-item"><span class="tip-icon">📚</span><span>Take BUSN 125 seriously. This class puts you in a small group with two upperclassman Peer Leaders and about twelve fellow freshman BHers. It is one of the best tools you have for making real friends and understanding what BH is actually about.</span></div>
                <div class="tip-item"><span class="tip-icon">🏢</span><span>Get comfortable in the Wehner building early. This is where your classes, professor office hours, help desks for your courses, and the Business Honors office are all located. Knowing where everything is removes a lot of unnecessary stress.</span></div>
                <div class="tip-item"><span class="tip-icon">🗓️</span><span>Attend every BH professional development event you can. These events are specifically designed to help freshman meet other BH students and start building professionally. They are low pressure and incredibly valuable.</span></div>
                <div class="tip-item"><span class="tip-icon">🎯</span><span>Go to the Mays Freshman Career Fair. This is a career fair exclusively for freshman, which means less competition and more opportunity to practice talking to recruiters in a lower stakes setting.</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="highlight-box" style="background: linear-gradient(135deg, #ffecd2, #fcb69f); color: #4a1a00;">
            <h3 style="color: #4a1a00;">Imposter Syndrome</h3>
            <p style="line-height: 1.75;">
            This is something nearly every Business Honors student experiences and very few talk about openly.
            When you are surrounded by 80 to 100 incredibly talented and driven people, it is easy to look around
            and feel like everyone else has it more figured out than you do. They do not. Everyone in that cohort
            is navigating the same uncertainty, the same nerves, and the same learning curve.
            You were selected for this program because you belong here. Confidence is not about having all the
            answers. It is about trusting that you are capable of figuring things out, and that is exactly what
            got you here in the first place. Lean on your cohort, ask for help without hesitation, and remember
            that the BH culture is cooperative, not competitive. Everyone wants to see you succeed.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">Know your resources inside Wehner</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">🏫</span><span>The Business Honors office is your home base. Your specialized BH advisor can help with course selection, career planning, and navigating the program. Do not wait until something goes wrong to visit.</span></div>
                <div class="tip-item"><span class="tip-icon">📖</span><span>Course help desks are available for many of your business classes and are staffed by students who have already taken the courses. Use them early and often, not just before exams.</span></div>
                <div class="tip-item"><span class="tip-icon">🧑‍🏫</span><span>Professor office hours are one of the most underused resources in college. Going to office hours, even just to introduce yourself, builds relationships that can lead to mentorship, research opportunities, and strong recommendation letters.</span></div>
                <div class="tip-item"><span class="tip-icon">📅</span><span>Priority registration is one of the best perks of being in BH. Plan your course schedule early each semester so you can take full advantage of it and get the classes and professors you actually want.</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">Helpful resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://mays.tamu.edu/business-honors/" target="_blank">Mays Business Honors Program</a><p>Official program page with key information and contacts</p></div>
                <div class="resource-card"><a href="https://hireaggies.com" target="_blank">HireAggies</a><p>Texas A&M career portal for internships and jobs</p></div>
                <div class="resource-card"><a href="https://studentactivities.tamu.edu" target="_blank">Texas A&M Student Activities</a><p>Find clubs, events, and involvement opportunities</p></div>
                <div class="resource-card"><a href="https://mays.tamu.edu/career-management-center/" target="_blank">Mays Career Management Center</a><p>Career advising, recruiting resources, and more</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif topic == "internship":

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">💼 Starting Your Internship Recruiting Journey</h3>
            <p>
            Every Business Honors student is required to complete at least one internship before graduating,
            and most students complete theirs during the summer after their sophomore or junior year.
            But the recruiting process starts much earlier than most freshman expect. Texas A&M has
            a strong recruiting presence across accounting, finance, oil and gas, consulting, and technology,
            and companies actively come to campus looking for Aggie talent. Here is how to get ahead of it.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">When to start and what to expect</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">🗓️</span><span>Many BH students begin recruiting as early as the fall of their freshman year. Even if you do not land an internship right away, the practice of applying, interviewing, and networking is invaluable and will make you significantly more prepared when it counts.</span></div>
                <div class="tip-item"><span class="tip-icon">🏁</span><span>Do not wait until you feel ready. There is no perfect moment to start. Getting into the process early means you make your mistakes when the stakes are lower, so that by the time your target recruiting season arrives you are genuinely competitive.</span></div>
                <div class="tip-item"><span class="tip-icon">📊</span><span>The recruiting timeline varies a lot by industry. Accounting and finance tend to recruit earlier, sometimes over a year in advance. Consulting and tech can vary widely. Talk to upperclassmen in your cohort about timelines specific to your field of interest.</span></div>
                <div class="tip-item"><span class="tip-icon">🎓</span><span>Attend the Mays Freshman Career Fair in your first semester. It is designed specifically for freshman and gives you a chance to practice talking to recruiters in a lower pressure setting before the bigger career fairs open up to everyone.</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">How to actually start recruiting</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">💻</span><span>Create your HireAggies profile as soon as possible. This is the official Texas A&M recruiting portal and is where many companies post internship and job opportunities specifically for Aggie students. Keep it updated as you gain new experiences.</span></div>
                <div class="tip-item"><span class="tip-icon">📄</span><span>Build your resume now, even if it feels thin. Include your high school achievements, any leadership roles, relevant coursework, and skills. Your BH advisor and the Mays Career Management Center can review it and help you strengthen it.</span></div>
                <div class="tip-item"><span class="tip-icon">🔗</span><span>Set up your LinkedIn profile early and connect with your BH cohort, peer leaders, and any professionals you meet at events. A complete and professional LinkedIn is often the first thing a recruiter looks at before an interview.</span></div>
                <div class="tip-item"><span class="tip-icon">🗣️</span><span>Practice your elevator pitch. Be able to clearly and confidently explain who you are, what you are studying, and what kind of opportunities you are looking for in about 60 seconds. You will use this at every career fair and networking event you attend.</span></div>
                <div class="tip-item"><span class="tip-icon">📬</span><span>Do not underestimate cold outreach. Finding a Mays or BH alum working at a company you are interested in and reaching out for a 15 minute informational interview is one of the most effective recruiting strategies there is. Most people are happy to help a fellow Aggie.</span></div>
                <div class="tip-item"><span class="tip-icon">🤝</span><span>Use your cohort as a resource. Upperclassmen in BH have gone through this exact process and are very willing to share what worked for them. Ask them about their experience, request resume feedback, and do mock interviews with each other.</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="highlight-box" style="background: linear-gradient(135deg, #f7971e, #ffd200); color: #3d1f00;">
            <h3 style="color: #3d1f00;">💡 A word of encouragement</h3>
            <p style="line-height: 1.75;">
            Recruiting can feel intimidating when you are surrounded by cohort members who seem to have
            everything figured out. Remember that almost everyone is figuring it out as they go.
            The students who succeed in recruiting are not always the most qualified on paper.
            They are the ones who start early, stay consistent, and are not afraid to put themselves out there
            even when it feels uncomfortable. Confidence and preparation go a long way, and being a Business
            Honors Aggie already says a lot about who you are.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">Helpful resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://hireaggies.com" target="_blank">HireAggies</a><p>Texas A&M official internship and job recruiting portal</p></div>
                <div class="resource-card"><a href="https://mays.tamu.edu/career-management-center/" target="_blank">Mays Career Management Center</a><p>Resume reviews, interview prep, and career advising</p></div>
                <div class="resource-card"><a href="https://www.linkedin.com" target="_blank">LinkedIn</a><p>Build your professional profile and connect with Aggie alumni</p></div>
                <div class="resource-card"><a href="https://biginterview.com" target="_blank">Big Interview</a><p>Free interview practice tool used by many college students</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif topic == "orgs":

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">🤝 Getting Involved in Student Organizations</h3>
            <p>
            One of the best things about Texas A&M is how much there is to get involved in.
            The campus culture is built around participation, community, and showing up for one another.
            For Business Honors students specifically, student organizations are one of the most powerful
            ways to build your professional network, develop leadership skills, and find your people outside
            of the classroom. Here is how to approach it.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">Where to start</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">🏛️</span><span>Go to the MSC Open House during the first weekend of the semester. This is a campus wide fair where every club and organization sets up a table. It is the single best way to get a broad picture of what is available before committing to anything.</span></div>
                <div class="tip-item"><span class="tip-icon">🌱</span><span>Consider joining a Freshman Leadership Organization, also known as a FLO. These are specifically designed for first year students and are one of the best ways to meet people across campus. The business FLO is called FRWD, which stands for Freshman Reflecting While Developing.</span></div>
                <div class="tip-item"><span class="tip-icon">🤝</span><span>Get involved with the Business Honors Association. This is the only organization exclusively for BH students and exists to build community within the cohort through events and programming. It is a natural starting point because everyone in the room is in your program.</span></div>
                <div class="tip-item"><span class="tip-icon">🎯</span><span>A good rule of thumb for freshman is to join three organizations: one that is academically or professionally focused, one that is social, and one that involves service. This gives you a well rounded experience without spreading yourself too thin.</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">Business organizations with strong BH communities</h3>
            <div class="tip-grid">
                <div class="tip-item"><span class="tip-icon">🏆</span><span>Business Fellows is one of the most prestigious business organizations at A&M and has a highly selective application and interview process. It is the most competitive of the organizations listed here, so prepare thoroughly if you plan to apply.</span></div>
                <div class="tip-item"><span class="tip-icon">📈</span><span>Titans of Investing and TRIP (Trading Risk and Investment Programs) are great options for students interested in finance and investing. Both have application and interview processes and attract a lot of BH students interested in financial careers.</span></div>
                <div class="tip-item"><span class="tip-icon">💡</span><span>Aggies in Consulting is a strong choice for students exploring management consulting. Like the others, it has a competitive application process, so getting your resume in shape and doing your research on consulting before applying will help you stand out.</span></div>
                <div class="tip-item"><span class="tip-icon">💻</span><span>Aggies in Tech is a great fit for BH students interested in the technology space, whether that is product, software, or tech strategy. It broadens your network beyond traditional business fields and is valuable no matter what industry you end up in.</span></div>
                <div class="tip-item"><span class="tip-icon">🏫</span><span>Business Student Council is a strong option for students interested in representing and serving the broader business student community at Mays. It offers leadership experience and visibility within the college.</span></div>
                <div class="tip-item"><span class="tip-icon">⚠️</span><span>All of the professional organizations listed here have competitive application and interview processes. Do not let that discourage you from applying as a freshman. Use the process as practice, get feedback, and try again. Many BH students do not get in on their first attempt.</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="highlight-box" style="background: linear-gradient(135deg, #43cea2, #185a9d); color: white;">
            <h3 style="color: white;">⚖️ Quality over quantity</h3>
            <p style="line-height: 1.75; color: rgba(255,255,255,0.92);">
            It is tempting to join as many organizations as possible when you first arrive, especially
            when everything sounds exciting and you want to be involved. But being deeply engaged in
            two or three organizations is far more valuable than having your name on six email lists.
            Recruiters and future employers care about the depth of your involvement and the leadership
            you developed, not the length of your list. If something is not adding value to your life
            after giving it a genuine chance, it is okay to step back and make room for something that does.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="stressor-section">
            <h3 style="color: #b35a00;">Helpful resources</h3>
            <div class="resource-grid">
                <div class="resource-card"><a href="https://studentactivities.tamu.edu" target="_blank">Texas A&M Student Activities</a><p>Full directory of organizations and campus involvement</p></div>
                <div class="resource-card"><a href="https://mays.tamu.edu" target="_blank">Mays Business School</a><p>Information on business specific organizations and events</p></div>
                <div class="resource-card"><a href="https://linktr.ee/tamu_frwd" target="_blank">FRWD Freshman Leadership Org</a><p>The business freshman leadership organization at A&M</p></div>
                <div class="resource-card"><a href="https://hireaggies.com" target="_blank">HireAggies</a><p>Career portal to complement your org involvement with recruiting</p></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

elif page == "🧘 Yoga and Meditation":

    st.markdown("""
    <style>
    .yoga-hero {
        background: linear-gradient(135deg, #3b1f6b, #1a6b5e);
        border-radius: 20px;
        padding: 36px 40px;
        margin-bottom: 28px;
        text-align: center;
    }
    .yoga-hero h1 { color: white; font-size: 2.2em; margin: 0 0 8px 0; }
    .yoga-hero p { color: rgba(255,255,255,0.85); font-size: 1.1em; margin: 0; }
    .yoga-section {
        background: #f8fafc;
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    .yoga-section h3 { margin-top: 0; }
    .pose-card {
        background: white;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
    }
    .pose-card h4 { margin: 10px 0 6px 0; color: #3b1f6b; font-size: 1em; }
    .pose-card p { color: #555; font-size: 0.9em; margin: 0; line-height: 1.6; }
    .pose-card img { width: 100%; border-radius: 8px; object-fit: cover; height: 180px; }
    .pose-timer {
        background: #f0f4ff;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 0.85em;
        color: #3b1f6b;
        margin-top: 8px;
        font-weight: 600;
    }
    .breathing-circle {
        width: 160px;
        height: 160px;
        border-radius: 50%;
        background: linear-gradient(135deg, #89f7fe, #66a6ff);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        font-size: 1.1em;
        font-weight: 700;
        color: white;
        text-align: center;
        transition: transform 4s ease-in-out;
    }
    .mindfulness-card {
        background: white;
        border-radius: 10px;
        padding: 14px 16px;
        border: 1px solid #e2e8f0;
        display: flex;
        align-items: flex-start;
        gap: 10px;
        margin-bottom: 10px;
        font-size: 0.95em;
        line-height: 1.6;
    }
    .mindfulness-icon { font-size: 1.3em; flex-shrink: 0; }
    </style>

    <div class="yoga-hero">
        <h1>🧘 Yoga and Meditation</h1>
        <p>Slow down, breathe, and take care of your mind and body.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🧘 Yoga Flows", "🌬️ Breathing and Meditation", "🌿 Daily Mindfulness"])

    with tab1:
        st.markdown(" ")
        st.markdown("### Select a Yoga Style:")
        st.markdown(" ")

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            if st.button("🌱 Beginner", use_container_width=True):
                st.session_state["yoga"] = "beginner"
        with col2:
            if st.button("😮‍💨 Stress Relief", use_container_width=True):
                st.session_state["yoga"] = "stress"
        with col3:
            if st.button("☀️ Morning Energy", use_container_width=True):
                st.session_state["yoga"] = "morning"
        with col4:
            if st.button("🌙 Bedtime", use_container_width=True):
                st.session_state["yoga"] = "bedtime"
        with col5:
            if st.button("💺 Desk Stretches", use_container_width=True):
                st.session_state["yoga"] = "desk"

        st.markdown("---")

        if "yoga" not in st.session_state:
            st.markdown("""
            <div style="text-align:center; padding: 40px 20px; color: #888;">
                <div style="font-size: 2.5em;">👆</div>
                <p style="font-size: 1.05em; margin-top: 12px;">Select a yoga style above to get started.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            yoga_flows = {
                "beginner": {
                    "title": "🌱 Beginner Yoga",
                    "description": "Perfect if you have never done yoga before. These foundational poses build body awareness, flexibility, and calm. Move slowly and focus on your breath throughout.",
                    "duration": "20 to 30 minutes",
                    "poses": [
                        {
                            "name": "Mountain Pose",
                            "image": "assets/mountain_pose.jpg",
                            "hold": "30 seconds",
                            "instructions": "Stand tall with feet together, arms at your sides. Press all four corners of your feet into the ground, engage your thighs, and relax your shoulders down away from your ears. Breathe deeply and feel grounded."
                        },
                        {
                            "name": "Cat Cow Pose",
                            "image": "assets/cat_cow_pose.jpg",
                            "hold": "60 seconds",
                            "instructions": "Start on hands and knees. On an inhale, drop your belly, lift your chest and tailbone upward (cow). On an exhale, round your spine toward the ceiling and tuck your chin (cat). Flow between the two with your breath."
                        },
                        {
                            "name": "Child's Pose",
                            "image": "assets/childs_pose.jpg",
                            "hold": "45 seconds",
                            "instructions": "From hands and knees, sit your hips back toward your heels and stretch your arms forward on the mat. Rest your forehead down and breathe into your back. This is your resting pose and you can return to it anytime."
                        },
                        {
                            "name": "Downward Dog",
                            "image": "assets/downward_dog.jpg",
                            "hold": "45 seconds",
                            "instructions": "From hands and knees, tuck your toes and lift your hips up and back, forming an inverted V shape. Press your palms firmly into the mat, keep a slight bend in your knees, and let your head hang naturally."
                        },
                        {
                            "name": "Warrior One",
                            "image": "assets/warrior_one.jpg",
                            "hold": "30 seconds each side",
                            "instructions": "Step your right foot forward between your hands and rise up. Bend your front knee to 90 degrees, keep your back leg straight, and raise your arms overhead. Square your hips forward and breathe steadily. Repeat on the left side."
                        }
                    ]
                },
                "stress": {
                    "title": "😮‍💨 Stress Relief Yoga",
                    "description": "Designed specifically to release the tension that builds up from long study sessions, screens, and a busy schedule. These poses target the areas where stress lives in your body.",
                    "duration": "25 to 35 minutes",
                    "poses": [
                        {
                            "name": "Standing Forward Fold",
                            "image": "assets/forward_fold.jpg",
                            "hold": "60 seconds",
                            "instructions": "Stand with feet hip width apart and slowly hinge forward at the hips, letting your upper body hang heavy. Bend your knees generously if needed. Let your head and arms dangle and breathe into the stretch in your back and hamstrings."
                        },
                        {
                            "name": "Seated Spinal Twist",
                            "image": "assets/spinal_twist.jpg",
                            "hold": "45 seconds each side",
                            "instructions": "Sit on the floor with legs extended. Bend your right knee and cross it over your left leg, placing your foot flat on the floor. Place your right hand behind you and hook your left elbow outside your right knee. Gently twist to the right and breathe deeply."
                        },
                        {
                            "name": "Pigeon Pose",
                            "image": "assets/pigeon_pose.jpg",
                            "hold": "90 seconds each side",
                            "instructions": "From downward dog, bring your right knee forward and place it behind your right wrist at an angle. Extend your left leg straight back. Lower your hips toward the floor and fold forward over your front leg. This deeply releases the hips where a lot of stress is stored."
                        },
                        {
                            "name": "Legs Up The Wall",
                            "image": "assets/legs_up_wall.jpg",
                            "hold": "3 to 5 minutes",
                            "instructions": "Sit sideways next to a wall and swing your legs up as you lie back. Let your legs rest against the wall and your arms relax at your sides. Close your eyes and breathe slowly. This pose calms the nervous system and is one of the most restorative poses you can do."
                        },
                        {
                            "name": "Corpse Pose",
                            "image": "assets/corpse_pose.jpg",
                            "hold": "3 to 5 minutes",
                            "instructions": "Lie flat on your back with arms slightly away from your body, palms facing up. Close your eyes and let your body completely relax into the floor. Breathe naturally and allow your mind to settle. Do not skip this pose as it is where your body integrates the practice."
                        }
                    ]
                },
                "morning": {
                    "title": "☀️ Morning Energy Yoga",
                    "description": "A short and energizing flow to wake up your body and set a positive tone for the day. You do not need to be a morning person to benefit from this sequence.",
                    "duration": "15 to 20 minutes",
                    "poses": [
                        {
                            "name": "Sun Salutation",
                            "image": "assets/sun_salutation.jpg",
                            "hold": "Flow through 3 rounds",
                            "instructions": "Begin standing, inhale arms overhead, exhale fold forward, step back to plank, lower to the floor, inhale into cobra, exhale to downward dog, step forward, inhale rise up, exhale hands to heart. This sequence warms up your entire body and is the foundation of many yoga practices."
                        },
                        {
                            "name": "Cobra Pose",
                            "image": "assets/cobra_pose.jpg",
                            "hold": "30 seconds",
                            "instructions": "Lie face down with hands under your shoulders. Press into your palms and lift your chest off the floor, keeping your elbows slightly bent and your shoulders away from your ears. Open your chest and breathe into the front of your body."
                        },
                        {
                            "name": "Low Lunge",
                            "image": "assets/low_lunge.jpg",
                            "hold": "45 seconds each side",
                            "instructions": "Step your right foot forward between your hands and lower your left knee to the floor. Sink your hips forward and down while lifting your chest and sweeping your arms overhead. Feel the stretch through your hip flexors which tighten from long hours of sitting."
                        },
                        {
                            "name": "Warrior Two",
                            "image": "assets/warrior_two.jpg",
                            "hold": "45 seconds each side",
                            "instructions": "Step your feet wide apart. Turn your right foot out 90 degrees and bend that knee to 90 degrees. Extend your arms out to the sides at shoulder height and gaze over your front hand. Feel strong, rooted, and energized."
                        },
                        {
                            "name": "Upward Dog",
                            "image": "assets/upward_dog.jpg",
                            "hold": "30 seconds",
                            "instructions": "Lie face down, place hands under shoulders, and press up to straighten your arms while lifting your thighs off the floor. Roll your shoulders back, open your chest wide, and gaze forward or slightly upward. This is a powerful chest and spine opener."
                        }
                    ]
                },
                "bedtime": {
                    "title": "🌙 Bedtime and Restorative Yoga",
                    "description": "Gentle poses to help you unwind, release the day, and prepare your body and mind for deep sleep. Move slowly and let gravity do the work.",
                    "duration": "20 to 30 minutes",
                    "poses": [
                        {
                            "name": "Seated Forward Bend",
                            "image": "assets/seated_forward_bend.jpg",
                            "hold": "90 seconds",
                            "instructions": "Sit with legs extended straight in front of you. Inhale to lengthen your spine, then exhale and slowly fold forward, reaching toward your feet. Do not force it. Let your back round and your head hang heavy. Breathe into the backs of your legs and lower back."
                        },
                        {
                            "name": "Supine Spinal Twist",
                            "image": "assets/supine_twist.jpg",
                            "hold": "90 seconds each side",
                            "instructions": "Lie on your back, hug your right knee to your chest, then guide it across your body to the left while extending your right arm out to the side. Look right if comfortable. Let gravity gently deepen the twist with each exhale. Switch sides."
                        },
                        {
                            "name": "Happy Baby",
                            "image": "assets/happy_baby.jpg",
                            "hold": "60 seconds",
                            "instructions": "Lie on your back and hug both knees to your chest. Grab the outer edges of your feet and open your knees toward your armpits. Gently rock side to side if that feels good. This releases the hips and lower back beautifully."
                        },
                        {
                            "name": "Butterfly Pose",
                            "image": "assets/butterfly_pose.jpg",
                            "hold": "2 minutes",
                            "instructions": "Sit with the soles of your feet together and let your knees fall out to the sides. Hold your feet and slowly fold forward, letting your back round and your head drop. This is a deeply calming hip opener that signals to your body that it is time to rest."
                        },
                        {
                            "name": "Savasana",
                            "image": "assets/savasana.jpg",
                            "hold": "5 minutes",
                            "instructions": "Lie completely flat on your back, arms and legs slightly apart, eyes closed. Let go of any control over your breathing and allow your body to sink into the floor. Scan from your toes to the top of your head and consciously relax each part of your body."
                        }
                    ]
                },
                "desk": {
                    "title": "💺 Quick Desk Stretches",
                    "description": "Five minute stretches you can do right at your desk or between classes without a mat or any equipment. Your body will thank you after long study sessions.",
                    "duration": "5 to 10 minutes",
                    "poses": [
                        {
                            "name": "Neck Side Stretch",
                            "image": "assets/neck_stretch.jpg",
                            "hold": "30 seconds each side",
                            "instructions": "Sit tall in your chair. Drop your right ear toward your right shoulder and hold. You can gently place your right hand on your head for a deeper stretch. Breathe slowly and switch sides. This releases tension from looking at screens."
                        },
                        {
                            "name": "Shoulder Roll",
                            "image": "assets/shoulder_roll.jpg",
                            "hold": "30 seconds",
                            "instructions": "Sit upright and slowly roll both shoulders backward in large circles five times, then forward five times. Follow with a shoulder squeeze, pulling them up toward your ears on an inhale and dropping them down on an exhale."
                        },
                        {
                            "name": "Seated Cat Cow",
                            "image": "assets/seated_cat_cow.jpg",
                            "hold": "60 seconds",
                            "instructions": "Sit at the edge of your chair with feet flat on the floor. Place hands on your knees. On an inhale, arch your back and lift your chest (cow). On an exhale, round your spine and drop your chin (cat). Flow with your breath for 5 to 8 rounds."
                        },
                        {
                            "name": "Wrist Stretch",
                            "image": "assets/wrist_stretch.jpg",
                            "hold": "30 seconds each side",
                            "instructions": "Extend your right arm forward with palm facing up. Use your left hand to gently pull the fingers down and back toward you. Hold and breathe, then switch. Essential for anyone who types for long periods."
                        },
                        {
                            "name": "Seated Spinal Stretch",
                            "image": "assets/seated_spinal_stretch.jpg",
                            "hold": "30 seconds each side",
                            "instructions": "Sit tall in your chair and cross your right leg over your left knee. Place your left hand on your right knee and your right hand on the back of the chair. Inhale to lengthen, exhale to gently twist to the right. Switch sides."
                        }
                    ]
                }
            }

            flow = yoga_flows[st.session_state["yoga"]]

            st.markdown(f"""
            <div class="yoga-section">
                <h3 style="color: #3b1f6b;">{flow["title"]}</h3>
                <p>{flow["description"]}</p>
                <p style="color: #666; font-size: 0.9em;">⏱️ Recommended duration: {flow["duration"]}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Poses in this flow:")
            st.markdown(" ")

            for i, pose in enumerate(flow["poses"]):
                col_img, col_info = st.columns([1, 2])
                with col_img:
                    try:
                        st.image(pose["image"], width=200, caption=pose["name"])
                    except:
                        st.markdown(f"""
                        <div style="background:#e8e8e8; border-radius:10px; height:180px;
                        display:flex; align-items:center; justify-content:center; color:#888;">
                            🧘 {pose["name"]}
                        </div>
                        """, unsafe_allow_html=True)
                with col_info:
                    st.markdown(f"#### {pose['name']}")
                    st.markdown(f"**Hold:** {pose['hold']}")
                    st.write(pose["instructions"])
                    st.info(f"Hold {pose['name']} for {pose['hold']} — Focus on breathing deeply and relaxing into the stretch.")
                st.markdown("---")

    with tab2:
        st.markdown(" ")
        st.markdown("### 🌬️ Breathing Exercise")
        st.markdown(" ")

        st.markdown("""
        <div class="yoga-section">
            <h3 style="color: #1a6b5e;">Choose a breathing pattern</h3>
        </div>
        """, unsafe_allow_html=True)

        breath_type = st.selectbox("Select a pattern:", [
            "Box Breathing (4-4-4-4) — Great for stress and focus",
            "4-7-8 Breathing — Great for falling asleep",
            "Calm Breathing (4-6) — Great for general relaxation"
        ])

        if "Box" in breath_type:
            phases = [("Breathe In", 4), ("Hold", 4), ("Breathe Out", 4), ("Hold", 4)]
            description = "Box breathing is used by athletes and military personnel to stay calm under pressure. Each phase lasts 4 seconds."
        elif "4-7-8" in breath_type:
            phases = [("Breathe In", 4), ("Hold", 7), ("Breathe Out", 8)]
            description = "The 4-7-8 pattern activates your parasympathetic nervous system and is one of the most effective tools for falling asleep quickly."
        else:
            phases = [("Breathe In", 4), ("Breathe Out", 6)]
            description = "Simple and powerful. A longer exhale than inhale naturally slows your heart rate and calms your mind."

        st.info(description)

        rounds = st.slider("How many rounds would you like to complete?", 1, 10, 3)

        if st.button("Start Breathing Exercise", use_container_width=True):
            import time
            total_rounds = rounds
            total_seconds = total_rounds * sum(d for _, d in phases)
            progress_bar = st.progress(0)
            status_box = st.empty()
            circle_box = st.empty()
            elapsed = 0

            for r in range(total_rounds):
                for phase, duration in phases:
                    for second in range(duration):
                        elapsed += 1
                        overall_progress = elapsed / total_seconds if total_seconds > 0 else 0
                        progress_bar.progress(overall_progress)

                        if phase == "Breathe In":
                            size = 120 + int((second / duration) * 80)
                            color = "linear-gradient(135deg, #89f7fe, #66a6ff)"
                        elif phase == "Breathe Out":
                            size = 200 - int((second / duration) * 80)
                            color = "linear-gradient(135deg, #a18cd1, #fbc2eb)"
                        else:
                            size = 160
                            color = "linear-gradient(135deg, #43cea2, #185a9d)"

                        circle_box.markdown(f"""
                        <div style="text-align:center; padding: 20px 0;">
                            <div style="
                                width: {size}px;
                                height: {size}px;
                                border-radius: 50%;
                                background: {color};
                                display: inline-flex;
                                align-items: center;
                                justify-content: center;
                                color: white;
                                font-weight: 700;
                                font-size: 1em;
                                transition: all 1s ease;
                                box-shadow: 0 0 30px rgba(102,166,255,0.4);
                            ">
                                {phase}<br>{duration - second}s
                            </div>
                            <p style="color: #888; margin-top: 16px;">Round {r + 1} of {total_rounds}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        time.sleep(1)

            progress_bar.progress(1.0)
            circle_box.empty()
            status_box.success("Session complete! Take a moment to notice how you feel.")
            st.balloons()

        st.markdown("---")
        st.markdown("### ⏱️ Meditation Timer")
        st.markdown(" ")

        col_left, col_right = st.columns(2)

        with col_left:
            med_minutes = st.slider("Session length in minutes:", 1, 30, 5)

        with col_right:
            sound_choice = st.selectbox("Ambient sound:", [
                "No sound",
                "Rain",
                "Ocean Waves",
                "Forest",
                "White Noise"
            ])

        sound_urls = {
            "Rain": "https://www.soundjay.com/misc/sounds/rain-01.mp3",
            "Ocean Waves": "https://www.soundjay.com/misc/sounds/ocean-wave-1.mp3",
            "Forest": "https://www.soundjay.com/misc/sounds/crickets-1.mp3",
            "White Noise": "https://www.soundjay.com/misc/sounds/white-noise-1.mp3"
        }

        if sound_choice != "No sound" and sound_choice in sound_urls:
            st.markdown(f"""
            <audio autoplay loop>
                <source src="{sound_urls[sound_choice]}" type="audio/mpeg">
            </audio>
            """, unsafe_allow_html=True)

        if st.button("Start Meditation Session", use_container_width=True):
            import time
            total_seconds = med_minutes * 60
            progress_bar = st.progress(0)
            timer_display = st.empty()
 
            for second in range(total_seconds):
                remaining = total_seconds - second
                mins = remaining // 60
                secs = remaining % 60
                progress_bar.progress((second + 1) / total_seconds)
                timer_display.markdown(f"""
                <div style="text-align:center; padding: 30px 0;">
                    <div style="
                        font-size: 3.5em;
                        font-weight: 700;
                        color: #3b1f6b;
                        letter-spacing: 2px;
                    ">{mins:02d}:{secs:02d}</div>
                    <p style="color: #888; font-size: 1em; margin-top: 8px;">
                        Breathe naturally. Let your thoughts pass like clouds.
                    </p>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(1)

            progress_bar.progress(1.0)
            timer_display.empty()
            st.success(f"Your {med_minutes} minute meditation is complete. Well done.")
            st.balloons()

    with tab3:
        st.markdown(" ")
        st.markdown("""
        <div class="yoga-section">
            <h3 style="color: #1a6b5e;">🌿 Daily Mindfulness Habits</h3>
            <p>You do not need a full yoga session to be mindful. These small habits, practiced consistently,
            make a real difference in how you handle stress and show up each day.</p>
        </div>
        """, unsafe_allow_html=True)

        mindfulness_tips = [
            ("🌅", "Start your morning without your phone", "Give yourself the first 5 to 10 minutes of your day before checking notifications. Use that time to breathe, stretch, or just sit quietly. How you start your morning shapes how the rest of your day feels."),
            ("🍽️", "Eat at least one meal without a screen", "Put your phone face down during one meal each day. Notice the taste of your food, slow down, and give your brain a genuine break from stimulation."),
            ("🚶", "Take a mindful walk", "Once a day, walk somewhere on campus without headphones. Notice what is around you, how your feet feel on the ground, and what you can hear. Five minutes of this resets your nervous system."),
            ("📓", "Write three things you are grateful for", "Before bed, write down three specific things that happened today that you are grateful for. They do not have to be big. This practice rewires your brain over time to notice the good more naturally."),
            ("💬", "Check in with yourself at midday", "Around lunch, pause and ask yourself how you are actually feeling and whether your energy and focus are where you want them to be. Awareness is the first step to making any adjustment."),
            ("📵", "Create a phone free wind down", "For the last 30 minutes before sleep, put your phone in another room or face down across the room. Read, stretch, or just breathe. Your sleep quality will improve noticeably within a few days."),
            ("🌬️", "Use the 3 breath reset", "Any time you feel stressed or overwhelmed during the day, take three slow deliberate breaths before responding or reacting. Inhale for 4 counts, exhale for 6. This tiny habit builds enormous resilience over time."),
            ("🎯", "Set one intention each morning", "Before starting your day, decide on one word or one priority that will guide you. It could be focus, patience, energy, or presence. Having a simple intention creates direction and keeps you grounded when things get hectic.")
        ]

        for icon, title, description in mindfulness_tips:
            st.markdown(f"""
            <div class="mindfulness-card">
                <span class="mindfulness-icon">{icon}</span>
                <div>
                    <strong>{title}</strong><br>
                    <span style="color: #555;">{description}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

elif page == "📚 Resource Hub":
    st.title("Resource Hub")
    st.info("This page is coming soon!")

elif page == "📈 Progress Tracker":
    st.title("Progress Tracker")
    st.info("This page is coming soon!")