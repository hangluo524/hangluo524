import streamlit as st

# Set page config
st.set_page_config(page_title="Co-STORM", layout="wide")

# Sidebar
st.sidebar.title("Co-STORM")
st.sidebar.markdown("**Navigation**", unsafe_allow_html=True)
st.sidebar.button("New Session")
st.sidebar.button("Discover")
st.sidebar.button("My Library")
st.sidebar.markdown("---")
st.sidebar.markdown("[Contact Us](#)", unsafe_allow_html=True)
st.sidebar.markdown("[Bug Report](#)", unsafe_allow_html=True)

# Header and main content
st.markdown("<h1 style='text-align: center; color: black;'>Start a Roundtable Conversation</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>Enter a topic to start a meaningful discussion.</p>", unsafe_allow_html=True)


# Input field for topic with modern design
topic_input = st.text_input("Enter the topic (English only)", "", key="topic_input", placeholder="Type a topic...",
                            max_chars=100)


# Define a function for suggested topics with fixed-size textboxes
def display_suggested_topics():
    st.write("### Suggested Topics")

    # Create a container with centered alignment
    container = st.container()

    # Create 3 buttons with fixed size and blue background for suggested topics
    with container:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.text_area("2024 Federal Reserve reduce interest rates", height=100, max_chars=100, key="topic1",
                         disabled=True)
        with col2:
            st.text_area("AI's environmental impact on the whole planet", height=100, max_chars=100, key="topic2",
                         disabled=True)
        with col3:
            st.text_area("Human AI collaboration writing like OpenAI canvas", height=100, max_chars=100, key="topic3",
                         disabled=False)


# Display the topic input and suggested topics
if topic_input:
    st.write(f"### Roundtable Topic: {topic_input}")
else:
    display_suggested_topics()

# Footer links
st.markdown("---")
st.markdown("<p style='text-align: center;'>[arXiv (Co-STORM)](https://arxiv.org/)</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>[GitHub](https://github.com/)</p>", unsafe_allow_html=True)

# Styling to enhance the look and feel
st.markdown("""
    <style>
        /* General layout and background */
        .css-18e3th9 {
            background-color: #F5F5F5;  /* Light background */
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #FFFFFF;
            padding-top: 20px;
            padding-right: 10px;
            color: #000000;  /* Set the sidebar text color to black */
        }
        .sidebar .sidebar-header {
            font-size: 22px;
            font-weight: bold;
            color: #000000;  /* Set sidebar header text to black */
        }

        /* Title and text styling */
        .stTitle {
            color: #333;
            font-family: 'Arial', sans-serif;
            font-size: 28px;
            font-weight: 600;
            text-align: center;  /* Center align the title */
        }

        /* Text input field styling */
        .stTextInput input {
            font-size: 18px;
            padding: 12px;
            border-radius: 10px;
            border: 2px solid #0066FF;  /* Bright blue border for contrast */
            background-color: #ffffff;
            color: #333;
            width: 50%;  /* Ensure the input is centered */
            display: block;
            margin: 0 auto;
        }

        .stTextInput input:focus {
            border-color: #0066FF;
            background-color: #f7faff;
        }

        /* Button styling */
        .stButton button {
            background-color: #0066FF;
            color: white;
            font-size: 16px;
            padding: 12px;
            border-radius: 8px;
            width: 100%;
            font-weight: 500;
        }

        .stButton button:hover {
            background-color: #0052CC;
        }

        /* Suggested topics text areas */
        .stTextArea textarea {
            background-color: #0066FF;  /* Sci-fi blue color */
            color: white;
            font-size: 16px;
            padding: 12px;
            border-radius: 10px;
            border: 2px solid #0066FF;
            width: 100%;  /* Full width for consistent alignment */
            text-align: center;  /* Center the text */
        }

        .stTextArea textarea:focus {
            border-color: #0052CC;
            background-color: #0052CC;
        }

        /* Footer styling */
        .stMarkdown {
            font-family: 'Arial', sans-serif;
            font-size: 14px;
            color: #0066FF;
        }

        .stMarkdown a {
            color: #0066FF;
        }
        .stMarkdown a:hover {
            color: #0052CC;
        }
    </style>
""", unsafe_allow_html=True)
