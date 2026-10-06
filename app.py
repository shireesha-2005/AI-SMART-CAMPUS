import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Smart Campus",
    page_icon="🏫",
    layout="wide"
)

st.title("🏫 AI Smart Campus")
st.write("Welcome to your intelligent campus management system!")

st.sidebar.title("📌 Smart Campus")

menu = st.sidebar.selectbox(
    "Choose an option",
    [
        "Home",
        "Student Information",
        "Campus Events",
        "Announcements",
        "AI Study Assistant",
        "Campus Transport"
    ]
)

if menu == "Home":
    st.header("🌟 Smart Campus Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👨‍🎓 Students", "2,500")

    with col2:
        st.metric("👨‍🏫 Faculty", "150")

    with col3:
        st.metric("📚 Courses", "45")

    with col4:
        st.metric("🎉 Events", "12")

    st.subheader("💡 About AI Smart Campus")

    st.write("""
    AI Smart Campus is a digital platform designed to make
    college activities easier and smarter.

    Students can check campus events, announcements,
    transportation details and get study assistance.
    """)

elif menu == "Student Information":
    st.header("👨‍🎓 Student Information")

    name = st.text_input("Enter Student Name")
    roll_no = st.text_input("Enter Roll Number")
    branch = st.selectbox(
        "Select Branch",
        ["CSE", "AIML", "ECE", "EEE", "CIVIL", "MECH"]
    )

    if st.button("Submit"):
        if name and roll_no:
            st.success("Student information submitted successfully!")
            st.write("**Name:**", name)
            st.write("**Roll Number:**", roll_no)
            st.write("**Branch:**", branch)
        else:
            st.warning("Please enter all details.")

elif menu == "Campus Events":
    st.header("🎉 Upcoming Campus Events")

    events = {
        "Hackathon": "10 October 2026",
        "Cultural Fest": "15 October 2026",
        "Sports Meet": "20 October 2026",
        "Technical Workshop": "25 October 2026"
    }

    for event, date in events.items():
        st.info(f"🎯 **{event}** — {date}")

elif menu == "Announcements":
    st.header("📢 Campus Announcements")

    st.warning("📌 Internal exams will begin from 12 October.")
    st.success("🎓 Registration for the technical workshop is open.")
    st.info("📚 Library timings have been extended until 8 PM.")


elif menu == "AI Study Assistant":
    st.header("🤖 AI Study Assistant")

    question = st.text_area(
        "Ask your study question:"
    )

    if st.button("Get Answer"):
        if question:
            st.success("AI Assistant")
            st.write(
                "Your question has been received. "
                "This section can be connected to an AI model "
                "to generate intelligent answers."
            )
        else:
            st.warning("Please enter a question.")

elif menu == "Campus Transport":
    st.header("🚌 Campus Transport")

    st.write("### Bus Routes")

    transport = {
        "Route 1": "Hyderabad → Campus",
        "Route 2": "Secunderabad → Campus",
        "Route 3": "Kukatpally → Campus",
        "Route 4": "Miyapur → Campus"
    }

    for route, location in transport.items():
        st.write(f"🚌 **{route}:** {location}")

    st.success("Transport service is available from 7:00 AM to 6:00 PM.")