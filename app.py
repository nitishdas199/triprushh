import streamlit as st
import gem as travel_planner  # Replace with actual module name

# Add background image and sidebar color using custom CSS
def add_custom_css():
    st.markdown(
         f"""
         <style>
         /* Set background image for the app */
         .stApp {{
             background-image: url("https://raw.githubusercontent.com/nitishdas199/triprush/refs/heads/main/bg.jpg");
             background-size: cover;
             background-position: center;
         }}
         
         /* Customize the sidebar background and text color */
         [data-testid="stSidebar"] {{
             background-color: #4B8BBE; /* Change this to your desired sidebar background color */
         }}
         
         /* Customize sidebar elements */
         [data-testid="stSidebar"] .css-1lcbmhc {{
             color: white;  /* Change sidebar text color */
         }}

         /* Change color of input labels and text in the sidebar */
         [data-testid="stSidebar"] .css-1v0mbdj p {{
             color: white;  /* Label text color */
         }}

         /* Customize selectbox, button, etc. in sidebar */
         [data-testid="stSidebar"] .css-1n543e5 {{
             color: black;  /* Text color for dropdowns, buttons, etc. */
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Home Page Content
def home_page():
    st.title("Travel Itinerary Generator")

    # Input fields
    departure_location = st.text_input("Departure Location:")
    location = st.text_input("Destination:")
    people_count = st.number_input("Number of People:", min_value=1)
    travel_days = st.number_input("Travel Days:", min_value=1)
    travel_month = st.selectbox("Travel Month:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    audience_choice = st.selectbox("Audience Choice:", ["Adventure", "Family", "Elderly"])
    budget = st.number_input("Budget (USD):", min_value=1)

    # Generate Itinerary Button
    if st.button("Generate Itinerary"):
        itinerary = travel_planner.generate_itinerary(departure_location, location, people_count, travel_days, travel_month, audience_choice, budget)
        st.success(f"Itinerary:\n{itinerary}")

# About Us Page Content
def about_page():
    st.title("About Us")
    st.write("""
    Welcome to TripRush! We are a team of passionate travelers dedicated to helping you plan the perfect trip.

    Our team:
    """)

    team_members = [
        {"name": "**Nitish Kumar**", "title": "Biomedical Engineer, Developer", "linkedin": "https://www.linkedin.com/in/nitishdas199/", "img": "https://raw.githubusercontent.com/nitishdas199/triprushh/refs/heads/main/nick.jpeg"},
        {"name": "**Anjana Krishna**", "title": "Data Scientiest", "linkedin": "https://www.linkedin.com/in/anjana-krishnakumar99/", "img": "https://raw.githubusercontent.com/nitishdas199/triprushh/refs/heads/main/anjana.jpeg"},
        {"name": "**Dheeraj Bhureshwar**", "title": "Robotics Engineer", "linkedin": "https://www.linkedin.com/in/dheerajbhurewar/", "img": "https://raw.githubusercontent.com/nitishdas199/triprushh/refs/heads/main/dheeraj.jpeg"},
        {"name": "**Vanshita**", "title": "IT Engineer", "linkedin": "https://www.linkedin.com/in/vanshitarawat", "img": "https://raw.githubusercontent.com/nitishdas199/triprushh/refs/heads/main/1725380768795.jpeg"},
        {"name": "**Akhil**", "title": "IT Engineer", "linkedin": "https://www.linkedin.com/in/akhil-dasari017/", "img": "https://raw.githubusercontent.com/nitishdas199/triprushh/refs/heads/main/akhil.jpeg"}
    ]

    for member in team_members:
        st.write(f"""
        -  <a href="{member['linkedin']}" target="_blank"><img src="{member['img']}" alt="LinkedIn" style="width:40px; height:40px;"></a>  {member['name']}    - {member['title']}  
          
        """, unsafe_allow_html=True)

    st.write("""
    Guided by **Harri Prasad**, we aim to provide personalized travel recommendations to make your journey unforgettable.
    """)

    # About Us specific button
    if st.button("Meet the Team"):
        st.write("Team details are already listed above!")

# Contact Us Page Content
def contact_page():
    st.title("Contact Us")
    st.write("""
    We'd love to hear from you! Feel free to reach out to us via the following channels:
    
    - **Email:** nitishdas199@gmail.com
    
    Follow us on social media for travel inspiration and updates!
    """)

    # Contact Us specific button
    if st.button("Get in Touch"):
        st.write("We'll get back to you soon! Thank you for reaching out.")

# Main function to handle navigation
def main():
    # Apply custom CSS
    add_custom_css()

    # Display the logo at the top of the page
    st.image("https://raw.githubusercontent.com/nitishdas199/triprush/refs/heads/main/triprush.png", width=300)  # Replace 'logo.png' with your logo file path if needed

    # Create a selectbox for page navigation in the sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "About Us", "Contact"])

    # Page navigation logic
    if page == "Home":
        home_page()
    elif page == "About Us":
        about_page()
    elif page == "Contact":
        contact_page()

if __name__ == "__main__":
    main()
