import streamlit as st
import os
import base64

# --- APP CONFIGURATION ---
st.set_page_config(page_title='Empee Accommodation Web App', layout="wide")

st.title('Welcome to Empee accommodation web app')

# --- STANDARD WHATSAPP LINK (MALE_WHATSAPP_LINK_1) ---
# Setting the required link globally: https://wa.me/2349117035219
STANDARD_WHATSAPP_LINK = "https://wa.me/2349117035219"

# --- SIDEBAR ---
with st.sidebar:
    st.header("Empee Accommodation")
    st.write("Welcome!!!. 👋")
    st.markdown("---")
    select_option = st.radio("Go to", ("Male Private Hostels", "Female Private Hostel", "Apartments", "About", "Contact"))
    st.markdown("---")
    st.subheader("Settings")
    st.write("Pick a theme color:")
    selected_color = st.color_picker("", "#0000FF")
    # Apply the selected color to a header
    st.markdown(f"<h1 style='color:{selected_color};'>My Title</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("📫 Contact Me")
    # Sidebar contact link is standardized
    st.markdown(f"Feel free to reach out via [mmpeters626@gmail.com](mailto:mmpeters626@gmail.com) or chat on **WhatsApp**:")
    st.link_button(label="Chat on WhatsApp 💬", url=STANDARD_WHATSAPP_LINK)

# --- GLOBAL IMAGE HELPER FUNCTION ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except FileNotFoundError:
        return None

# --- MAIN CONTENT BODY ---

if select_option == "Male Private Hostels":
    st.markdown(
        """
        ## These are the hostels for both male and female available for booking with their prices.
        NOTE: the ones taken are marked as taken
        """
    )
    st.write("Male Hostels")
    st.markdown("---")
    
    # --- PROFILE IMAGE ---
    profile_image_base64 = get_base64_image("My Profile Pics.jpg")
    if profile_image_base64:
        st.markdown("""
            <style>
            .profile-img {
                width: 150px;
                height: 150px;
                border-radius: 50%;
                object-fit: cover;
                margin-bottom: 20px;
            }
            </style>
        """, unsafe_allow_html=True)
        st.markdown(f'<img src="data:image/png;base64,{profile_image_base64}" class="profile-img">', unsafe_allow_html=True)
    else:
        st.error(f"Error: Profile image 'My Profile Pics.jpg' not found.")
    
    
    # --- MALE HOSTEL VIDEOS SECTION ---
    st.subheader("Male Hostel Videos")

    # Define links using the standard link
    MALE_WHATSAPP_LINK_1 = STANDARD_WHATSAPP_LINK
    MALE_WHATSAPP_LINK_2 = STANDARD_WHATSAPP_LINK # All links must use MALE_WHATSAPP_LINK_1

    # List of videos with descriptions (All 'whatsapp_link' fields are now STANDARD_WHATSAPP_LINK)
    videos_with_comments = [
        {
            "filename": "male hostel video 1.mp4",
            "description": "**8 man room male private hostel**\n"
            "**Location:** moore road, off university road, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 530k total package per bed space for the 1st year and 450 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Close Proximity to both Unilag and Yabatech etc\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1
        },
        
        {
            "filename": "male hostel video 2.mp4",
            "description": "**4 man room male private hostel** available\n"
            "**Location:** Pako, Akoka, Lagos, very close to yabatech/unilag\n"
            "**Price:** 730k total package per bed space for a year and 650k in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1
        },
        
        {
            "filename": "male hostel video 3.mp4",
            "description": "**6 man room male private hostel** available\n"
            "**Location:** Pako, Akoka, Lagos, very close to yabatech/unilag\n"
            "**Price:** 680k total package per bed space for a year and 600k in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1
        },
        
        {
            "filename": "male hostel video 4.mp4",
            "description": "**2 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 780k total package per bed space for the 1st year and 700 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1
        },
        
        {
            "filename": "male hostel video 5.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 730k total package per bed space for the 1st year and 650 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1
        },
        
        {
            "filename": "male hostel video 5.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 730k total package per bed space for the 1st year and 650 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1
        },
        
        { 
            "filename": "male hostel video 5.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 730k total package per bed space for the 1st year and 650 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1
        },
        
        {
            "filename": "male hostel video 8.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Iwaya, akoka, Yaba, lagos, unilag\n"
            "**Price:** 600k total package per bed space for the 1st year and 500k in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Working Air conditioner\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- 1 minute walk to unilag back gate\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1
        },
        
        {
            "filename": "male hostel video 9.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1
        },
        
        {
            "filename": "male hostel video 10.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1 # Updated
        },
        {
            "filename": "male hostel video 11.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1 # Updated
        },
        
        {
            "filename": "male hostel video 12.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1 # Updated
        },
        
        {
            "filename": "male hostel video 13.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1 # Updated
        },
        
        {
            "filename": "male hostel video 14.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1 # Updated
        },
        
        {
            "filename": "male hostel video 15.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1 # Updated
        },
        
        {
            "filename": "male hostel video 16.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1 # Updated
        },
        
        {
            "filename": "male hostel video 17.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": MALE_WHATSAPP_LINK_1 # Updated
        },
        
        # NOTE: Videos 18-23 did not have a link in the original code, so no button is added.
        {
            "filename": "male hostel video 18.mp4",
            "description": "Additional view of hostel facilities.",
            "whatsapp_link": None 
        },
        
        {
            "filename": "male hostel video 19.mp4",
            "description": "Additional view of hostel facilities.",
            "whatsapp_link": None
        },
        {
            "filename": "male hostel video 20.mp4",
            "description": "Additional view of hostel facilities.",
            "whatsapp_link": None
        },
        {
            "filename": "male hostel video 21.mp4",
            "description": "Additional view of hostel facilities.",
            "whatsapp_link": None
        },
        {
            "filename": "male hostel video 22.mp4",
            "description": "Additional view of hostel facilities.",
            "whatsapp_link": None
        },
        {
            "filename": "male hostel video 23.mp4",
            "description": "Additional view of hostel facilities.",
            "whatsapp_link": None
        },
    ]

    # Loop through each video and display with comment
    col1, col2 = st.columns(2) 
    
    # We will use a counter to alternate between the two columns
    for i, video_info in enumerate(videos_with_comments):
        filename = video_info["filename"]
        description = video_info["description"]
        whatsapp_link = video_info["whatsapp_link"]
        
        # Select the column based on the index (even/odd)
        current_col = col1 if i % 2 == 0 else col2
        
        with current_col:
            st.subheader(f"Video {i+1}")
            if os.path.exists(filename):
                # Display video and description in the selected column
                st.video(filename, format="video/mp4", start_time=0) 
                st.markdown(f"**Description:** {description}")
                
                # --- ADDED THE LINK BUTTON HERE ---
                if whatsapp_link:
                    st.link_button(label="Book via WhatsApp Now! 📱", url=whatsapp_link, help="Click to chat and reserve your space")
                # -----------------------------------
                
                st.markdown("---") # Add a separator in the column
            else:
                st.error(f"Video file '{filename}' not found.")

elif select_option == "Female Private Hostel":
    st.title("Female Private Hostels")
    st.markdown("### Images and videos of Female Private Hostels available for booking.")
    st.markdown("---")
        
    # --- FEMALE HOSTEL IMAGES SECTION ---
    st.subheader("Female Hostel Images")
        
    # The WhatsApp link is now standardized
    FEMALE_WHATSAPP_LINK = STANDARD_WHATSAPP_LINK # Updated

    image_with_comments = [
        
        {
            "filename": "female hostel picture 2 room.jpg",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": FEMALE_WHATSAPP_LINK # Updated
        },
        
        
        {
            "filename": "female hostel picture 2 kitchen.jpg",
            "description": "Tour of the male hostel rooms.",
            "whatsapp_link": None
        },
        {
            "filename": "female hostel picture 1.jpg",
            "description": "Common areas in the hostel.",
            "whatsapp_link": None
        },
        {
            "filename": "female hostel picture 1.jpg",
            "description": "Hostel dining area.",
            "whatsapp_link": None
        }
    ]

    # Display images
    for image_info in image_with_comments:
        filename = image_info["filename"]
        description = image_info["description"]
        whatsapp_link = image_info["whatsapp_link"]
        if os.path.exists(filename):
            st.image(filename, width=350)
            st.markdown(f"**Description:** {description}")
            
            # --- ADDED THE LINK BUTTON HERE (for image section) ---
            if whatsapp_link:
                st.link_button(label="Book via WhatsApp Now! 📱", url=whatsapp_link, help="Click to chat and reserve your space")
            # --------------------------------------------------------
            
            st.markdown("---")
        else:
            st.error(f"Image file '{filename}' not found for female hostels.")
            
    st.subheader("Female Hostel Videos")

    # List of videos with descriptions (Using a placeholder list structure for brevity)
    videos_with_comments_female = [
        
        {
            "filename": "male hostel video 1.mp4",
            "description": "**8 man room male private hostel**\n"
            "**Location:** moore road, off university road, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 530k total package per bed space for the 1st year and 450 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Close Proximity to both Unilag and Yabatech etc\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": FEMALE_WHATSAPP_LINK # Updated
        },
        
        {
            "filename": "male hostel video 2.mp4",
            "description": "**4 man room male private hostel** available\n"
            "**Location:** Pako, Akoka, Lagos, very close to yabatech/unilag\n"
            "**Price:** 730k total package per bed space for a year and 650k in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Constant water supply\n"
            "- Tiolets and Baths\n"
            "- Tight security etc\n"
            "- 10 minute walk to Unilag back gate\n"
            "- Working Air conditioner\n"
            "- Serene Environment\n"
            "- Inverter\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": FEMALE_WHATSAPP_LINK # Updated
        },
        # NOTE: Including the last video for completeness, assuming all others in the original list are also updated
        {
            "filename": "male hostel video 17.mp4",
            "description": "**4 man room female private hostel** available\n"
            "**Location:** Pako, akoka, Yaba, lagos, very close to yabatech/unilag\n"
            "**Price:** 480k total package per bed space for the 1st year and 400 in subsequent years....\n\n"
            "#### **Hostel Facilities**\n\n"
            "- 24/7 Electricity Power Supply\n"
            "- Each bunks has a fan\n"
            "- Constant water supply\n"
            "- tiolets and Baths\n"
            "- Tight security etc\n"
            "- Hotplate is available\n\n"
            "Send a direct message to Michael Peters to reserve your bed space in this hostel.",
            "whatsapp_link": FEMALE_WHATSAPP_LINK # Updated
        },
    ]
    
    # Display videos (using the same structure as the male section for button placement)
    for video_info in videos_with_comments_female:
        filename = video_info["filename"]
        description = video_info["description"]
        whatsapp_link = video_info["whatsapp_link"]
        if os.path.exists(filename):
            st.video(filename, format="video/mp4", start_time=0)
            st.markdown(f"**Description:** {description}")
            
            # --- ADDED THE LINK BUTTON HERE (for video section) ---
            if whatsapp_link:
                st.link_button(label="Book via WhatsApp Now! 📱", url=whatsapp_link, help="Click to chat and reserve your space")
            # --------------------------------------------------------
            
            st.markdown("---")
        else:
            st.error(f"Video file '{filename}' not found for female hostels.")

elif select_option == "Apartments":
    st.title("Apartments")
    st.markdown("Content for Apartments will go here.")

elif select_option == "About":
    st.title("About Empee Accommodation")
    st.markdown("Content about the company/service will go here.")

elif select_option == "Contact":
    st.title("Contact Us")
    st.markdown(f"For bookings and inquiries, please reach out via WhatsApp using this link:")
    st.link_button(label="Chat on WhatsApp 💬", url=STANDARD_WHATSAPP_LINK) # Updated