import streamlit as st
from nltk.chat.util import Chat, reflections

# Define chatbot responses
pairs = [
    [r"(.*)my name is (.*)", ["Hello %2, nice to meet you! How can I assist you today?"]],
    [r"(.*)help(.*)", ["Sure! I'm here to help. What do you need assistance with?"]],
    [r"(.*) your name ?", ["I'm Satyabrata's Chatbot, your virtual assistant!"]],
    [r"how are you (.*) ?", ["I'm just a chatbot, but I'm always here to chat with you!"]],
    [r"(hi|hey|hello|hola)(.*)", ["Hello! How can I assist you today?"]],
    [r"(.*) (location|city) (.*)", ["I don't have a physical location, but you mentioned %3. What would you like to know about it?"]],
    [r"who is the prime minister of india", ["The Prime Minister of India is Narendra Modi."]],
    [r"who is the chief minister of andhra pradesh", ["Sri Nara Chandrababu Naidu"]],
    [r"who is the chief minister of arunachal pradesh", ["Shri Pema Khandu"]],
    [r"who is the chief minister of assam", ["Shri Himanta Biswa Sarma"]],
    [r"who is the chief minister of bihar", ["Shri Nitish Kumar"]],
    [r"who is the chief minister of chhattisgarh", ["Shri Vishnu Deo Sai"]],
    [r"who is the chief minister of goa", ["Shri Pramod Sawant"]],
    [r"who is the chief minister of gujarat", ["Shri Bhupendra Patel"]],
    [r"who is the chief minister of haryana", ["Shri Nayab Singh Saini"]],
    [r"who is the chief minister of himachal pradesh", ["Shri Sukhvinder Singh Sukhu"]],
    [r"who is the chief minister of jammu and kashmir", ["Shri Omar Abdullah"]],
    [r"who is the chief minister of jharkhand", ["Shri Hemant Soren"]],
    [r"who is the chief minister of karnataka", ["Shri Siddaramaiah"]],
    [r"who is the chief minister of kerala", ["Shri Pinarayi Vijayan"]],
    [r"who is the chief minister of madhya pradesh", ["Shri Mohan Yadav"]],
    [r"who is the chief minister of maharashtra", ["Shri Devendra Fadnavis"]],
    [r"who is the chief minister of meghalaya", ["Shri Conrad Kongkal Sangma"]],
    [r"who is the chief minister of mizoram", ["Shri PU Lalduhoma"]],
    [r"who is the chief minister of nagaland", ["Shri Neiphiu Rio"]],
    [r"who is the chief minister of odisha", ["Shri Mohan Charan Majhi"]],
    [r"who is the chief minister of puducherry", ["Shri N. Rangaswamy"]],
    [r"who is the chief minister of punjab", ["Shri Bhagwant Singh Mann"]],
    [r"who is the chief minister of rajasthan", ["Shri Bhajan Lal Sharma"]],
    [r"who is the chief minister of sikkim", ["Shri Prem Singh Tamang (Golay)"]],
    [r"who is the chief minister of tamil nadu", ["Shri M. K. Stalin"]],
    [r"who is the chief minister of telangana", ["Shri A Revanth Reddy"]],
    [r"who is the chief minister of tripura", ["Dr. Manik Saha"]],
    [r"who is the chief minister of uttar pradesh", ["Shri Yogi Aditya Nath"]],
    [r"who is the chief minister of uttarakhand", ["Shri Pushkar Singh Dhami"]],
    [r"who is the chief minister of west bengal", ["Km. Mamata Banerjee"]],
    [r"quit", ["Goodbye! Have a great day!"]],
    [r"(.*)", ["I'm not sure about that. Can you ask in a different way?"]],
]

# Initialize chatbot
chat = Chat(pairs, reflections)

def main():
    st.set_page_config(page_title="Satyabrata's Chatbot", page_icon="💬")
    st.markdown("""
        <style>
        body {
            background-color: #e0f7fa;
        }
        .chat-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            position: relative;
        }
        .chat-container::before {
            content: "✦ ✧ ✦ ✧ ✦";
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 20px;
            color: #aaa;
        }
        .user-message {
            text-align: right;
            color: blue;
        }
        .bot-message {
            text-align: left;
            color: green;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='chat-container'><h2>🤖 Chat with Satyabrata's Chatbot</h2></div>", unsafe_allow_html=True)
    
    user_input = st.text_input("You:", "", key="user_input", on_change=lambda: st.session_state.update(response=chat.respond(st.session_state.user_input)))
    
    if "response" in st.session_state and st.session_state.response:
        st.markdown(f"<p class='user-message'><b>You:</b> {st.session_state.user_input}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='bot-message'><b>Chatbot:</b> {st.session_state.response}</p>", unsafe_allow_html=True)
        st.session_state.response = ""

if __name__ == "__main__":
    main()
