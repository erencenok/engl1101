import streamlit as st
import folium
from streamlit_folium import st_folium
import qrcode
from io import BytesIO

st.set_page_config(
    page_title="Discover Piedmont Park",
    layout="wide",
    page_icon="🌳"
)

# ---------------------- SIDEBAR NAV ----------------------
st.sidebar.title("Discover Piedmont Park")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "History", "Ecology", "Culture", "Interactive Map", "Videos", "Brochure", "Team", "QR Generator"]
)

# ---------------------- HOME ----------------------
if page == "Home":
    st.title("🌳 Discover Piedmont Park")
    st.subheader("A multimodal experience designed by Georgia Tech students")

    st.write("""
    Explore Piedmont Park through history, ecology, culture, videos, and interactive maps.
    """)

    st.image("media/IMG_7960.jpeg", use_column_width=True)


# ---------------------- HISTORY ----------------------
elif page == "History":
    st.title("🏛️ History of Piedmont Park")

    st.write("""
    Piedmont Park has transformed many times since the 1800s, serving as farmland, 
    exposition grounds, and Atlanta’s most popular urban park.
    """)

    st.markdown("### Timeline")
    st.write("""
    - **1887:** Piedmont Exposition  
    - **1895:** Cotton States & International Exposition  
    - **1904:** Became public park  
    - **1990s–present:** Restoration & expansion  
    """)

    st.image("images/history_photo.jpg")


# ---------------------- ECOLOGY ----------------------
elif page == "Ecology":
    st.title("🌿 Ecology & Environmental Features")

    st.write("""
    Piedmont Park supports diverse wildlife, native trees, restored wetlands, and lake ecosystems.
    """)

    st.image("images/ecology_photo.jpg")


# ---------------------- CULTURE ----------------------
elif page == "Culture":
    st.title("🎭 Cultural Significance")

    st.write("""
    Piedmont Park is home to Atlanta’s largest events, markets, concerts, and neighborhood traditions.
    """)

    st.image("images/culture_photo.jpg")


# ---------------------- INTERACTIVE MAP ----------------------
elif page == "Interactive Map":
    st.title("🗺️ Interactive Map & Walking Routes")

    st.write("Explore the park using an interactive walking-route trail map.")

    # Map center
    m = folium.Map(location=[33.7851, -84.3738], zoom_start=15, tiles="CartoDB positron")

    # --- Attraction Markers ---
    attractions = {
        "Lake Clara Meer": (33.7856, -84.3720),
        "Active Oval": (33.7837, -84.3769),
        "The Meadow": (33.7859, -84.3752),
        "Dog Park": (33.7869, -84.3710)
    }

    for name, loc in attractions.items():
        folium.Marker(loc, popup=name, tooltip=name,
                      icon=folium.Icon(color="green", icon="info-sign")).add_to(m)

    # --- WALKING ROUTE (Polyline) ---
    walking_route = [
        (33.7859, -84.3752),  # Meadow
        (33.7856, -84.3720),  # Lake Clara Meer
        (33.7863, -84.3705),  # Dog Park area
        (33.7837, -84.3769)   # Active Oval
    ]

    folium.PolyLine(
        walking_route,
        tooltip="Suggested Walking Route",
        color="blue",
        weight=4,
        opacity=0.7
    ).add_to(m)

    # Render map
    st_folium(m, width=1000, height=600)


# ---------------------- VIDEOS ----------------------
elif page == "Videos":
    st.title("🎥 Video Collection")

    st.write("Short videos showcasing the nature, wildlife, and atmosphere of Piedmont Park.")

    st.video("YOUR_YOUTUBE_LINK_1")
    st.video("YOUR_YOUTUBE_LINK_2")
    st.video("YOUR_YOUTUBE_LINK_3")


# ---------------------- BROCHURE ----------------------
elif page == "Brochure":
    st.title("📄 Tri-Fold Brochure")

    st.write("Download the printed brochure designed for visiting Piedmont Park.")

    with open("brochure/brochure.pdf", "rb") as pdf:
        st.download_button("Download Brochure", pdf, file_name="PiedmontPark_Brochure.pdf")

    st.image("images/brochure_preview.png")


# ---------------------- TEAM PAGE ----------------------
elif page == "Team":
    st.title("👥 Meet the Team")

    st.write("Our project was created by Georgia Tech students as part of a multimodal assignment.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Eren")
        st.write("Website development, interactive map, and design.")
        st.image("images/eren.jpg", caption="Eren", width=200)

    with col2:
        st.subheader("Lara")
        st.write("Video creation, environmental footage, narration.")
        st.image("images/lara.jpg", caption="Lara", width=200)

    with col3:
        st.subheader("Arianna")
        st.write("Brochure design, cultural research, layout.")
        st.image("images/arianna.jpg", caption="Arianna", width=200)


# ---------------------- QR CODE GENERATOR ----------------------
elif page == "QR Generator":
    st.title("🔗 QR Code Generator")
    st.write("Create QR codes to post around campus linking to your website or project pages.")

    url = st.text_input("Enter the URL you want to encode:", "https://google.com")

    if st.button("Generate QR Code"):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        # Convert to displayable format
        buf = BytesIO()
        img.save(buf)
        buf.seek(0)

        st.image(buf, caption="Your QR Code", width=300)

        st.download_button(
            label="Download QR Code",
            data=buf,
            file_name="qr_code.png",
            mime="image/png"
        )
