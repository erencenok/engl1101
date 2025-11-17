import streamlit as st
import folium
from streamlit_folium import st_folium
import qrcode
from io import BytesIO
import os

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
For more than a century, Piedmont Park has been at the center of Atlanta’s growth. The land began as farmland in the mid-1800s, but after hosting the Piedmont Exposition of 1887 and the larger Cotton States and International Exposition of 1895, it became a major public gathering space that helped showcase the “New South” to the nation and the world. During the 1895 exposition, Booker T. Washington delivered his famous “Atlanta Compromise” speech, giving the site lasting historical significance. The City of Atlanta purchased the property in 1904 and began transforming it into a public park with help from the Olmsted Brothers, the landscape architects behind Central Park. After decades of heavy use, the Piedmont Park Conservancy was founded in 1989 to restore and protect the park, leading to major improvements and expansions. Today, Piedmont Park is a 200-acre urban green space that reflects Atlanta’s history, hosting community events, recreation, and education while preserving its cultural heritage.
""")

    st.markdown("### Timeline")
    st.write("""
    - **1887:** Piedmont Exposition  
    - **1895:** Cotton States & International Exposition  
    - **1904:** Became public park  
    - **1990s–present:** Restoration & expansion  
    """)

    st.image("media/IMG_7936.jpeg")


# ---------------------- ECOLOGY ----------------------
elif page == "Ecology":
    st.title("🌿 Ecology & Environmental Features")

    st.write("""
    Piedmont Park supports diverse wildlife, native trees, restored wetlands, and lake ecosystems.
    """)

    st.image("media/IMG_7960.jpeg")


# ---------------------- CULTURE ----------------------
elif page == "Culture":
    st.title("🎭 Cultural Significance")

    st.write("""
    Piedmont Park is home to Atlanta’s largest events, markets, concerts, and neighborhood traditions.
    """)

    st.video("media/IMG_7929.mp4")


# ---------------------- INTERACTIVE MAP ----------------------
elif page == "Interactive Map":
    st.title("🗺️ Interactive Map & Walking Routes")
    st.write("Explore the park using an interactive walking-route trail map.")

    # Map center
    m = folium.Map(location=[33.7851, -84.3738], zoom_start=15, tiles="CartoDB positron")

    # ---------- RAW GITHUB IMAGE URLS (REPLACE THESE) ----------
    lake_img = "piedmont-park-running-trail-03.jpg"
    oval_img = "RAW_URL_2"
    meadow_img = "RAW_URL_3"
    dog_img = "RAW_URL_4"
    garden_img = "RAW_URL_5"

    # ---------- MARKERS WITH POPUP IMAGES ----------
    folium.Marker(
        (33.784089977396995, -84.37297344943022),
        tooltip="Lake Clara Meer",
        popup=folium.Popup(f"<img src='{lake_img}' width='220'>", max_width=250)
    ).add_to(m)

    folium.Marker(
        (33.786417322689346, -84.37607408312104),
        tooltip="Active Oval",
        popup=folium.Popup(f"<img src='{oval_img}' width='220'>", max_width=250)
    ).add_to(m)

    folium.Marker(
        (33.78339296107428, -84.37157950990911),
        tooltip="The Meadow",
        popup=folium.Popup(f"<img src='{meadow_img}' width='220'>", max_width=250)
    ).add_to(m)

    folium.Marker(
        (33.78819038380616, -84.3709058638687),
        tooltip="Dog Park",
        popup=folium.Popup(f"<img src='{dog_img}' width='220'>", max_width=250)
    ).add_to(m)

    folium.Marker(
        (33.789986280083774, -84.37252046600035),
        tooltip="Atlanta Botanical Garden",
        popup=folium.Popup(f"<img src='{garden_img}' width='220'>", max_width=250)
    ).add_to(m)

    # ---------- WALKING ROUTE ----------
    walking_route = [
        (33.78339296107428, -84.37157950990911),  
        (33.784089977396995, -84.37297344943022),
        (33.78819038380616, -84.3709058638687),  
        (33.789986280083774, -84.37252046600035),
        (33.786417322689346, -84.37607408312104)
    ]

    folium.PolyLine(
        walking_route,
        tooltip="Suggested Walking Route",
        color="blue",
        weight=4,
        opacity=0.7
    ).add_to(m)

    st_folium(m, width=1000, height=600)


# ---------------------- VIDEOS ----------------------
elif page == "Videos":
    st.title("🎥 Video Collection")
    st.write("Short videos showcasing the nature, wildlife, and atmosphere of Piedmont Park.")

    video_files = [f for f in os.listdir("media") if f.lower().endswith(".mp4")]

    for video in sorted(video_files):
        st.video(f"media/{video}")


# ---------------------- BROCHURE ----------------------
elif page == "Brochure":
    st.title("📄 Tri-Fold Brochure")

    st.write("Download the printed brochure designed for visiting Piedmont Park.")
    st.info("Arianna will provide the PDF. Upload it to brochure/brochure.pdf")
    st.write("📄 Brochure coming soon!")


# ---------------------- TEAM PAGE ----------------------
elif page == "Team":
    st.title("👥 Meet the Team")
    st.write("Our project was created by Georgia Tech students as part of a multimodal assignment.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Eren")
        st.write("Website development, interactive map, and design.")
        st.write("📸 Photo coming soon.")

    with col2:
        st.subheader("Lara")
        st.write("Video creation, environmental footage, narration.")
        st.write("📸 Photo coming soon.")

    with col3:
        st.subheader("Arianna")
        st.write("Brochure design, cultural research, layout.")
        st.write("📸 Photo coming soon.")


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
