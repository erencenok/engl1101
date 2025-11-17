import streamlit as st
import folium
from streamlit_folium import st_folium

# ----------------------- PAGE CONFIG -----------------------
st.set_page_config(
    page_title="Discover Piedmont Park",
    layout="wide",
    page_icon="🌳"
)

# ----------------------- SIDEBAR NAVIGATION -----------------------
st.sidebar.title("Discover Piedmont Park")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "History", "Ecology", "Culture", "Interactive Map", "Videos", "Brochure"]
)

# ----------------------- PAGES -----------------------

# HOME PAGE -------------------------------------------------------
if page == "Home":
    st.title("🌳 Discover Piedmont Park")
    st.subheader("A multimodal experience designed by Georgia Tech students")

    st.write("""
    Piedmont Park is one of Atlanta’s most iconic green spaces—offering skyline views, 
    wildlife, rich cultural history, and decades of community events.  
               
    This website gives a **digital, interactive version** of the “Discover Piedmont Park” project,
    expanding on the brochure and video collection.
    """)

    st.image("piedmont.jpeg", caption="Piedmont Park, Atlanta", use_column_width=True)


# HISTORY PAGE ----------------------------------------------------
elif page == "History":
    st.title("🏛️ History of Piedmont Park")
    
    st.write("""
    Piedmont Park has transformed many times since the 1800s, serving as a farmland,
    exposition site, and now Atlanta’s most visited public park.  
    """)

    st.markdown("### Timeline")
    st.write("""
    - **1887:** Site of the Piedmont Exposition  
    - **1895:** Hosted the Cotton States and International Exposition  
    - **1904:** Became a public park  
    - **1990s–present:** Large expansions, environmental restoration, community events  
    """)

    st.image("history_photo.jpg", caption="Historical image of Piedmont Park")


# ECOLOGY PAGE ----------------------------------------------------
elif page == "Ecology":
    st.title("🌿 Ecology & Environmental Features")

    st.write("""
    Piedmont Park’s ecosystem includes diverse wildlife, restored wetlands,
    native plants, lake habitats, and migratory bird pathways.
    """)

    st.markdown("### Key Ecological Features")
    st.write("""
    - Lake Clara Meer  
    - Native tree species & forests  
    - Community gardens  
    - Wetlands restoration  
    """)

    st.image("ecology_photo.jpg", caption="Wildlife and natural areas")


# CULTURE PAGE ----------------------------------------------------
elif page == "Culture":
    st.title("🎭 Cultural Significance & Attractions")

    st.write("""
    Beyond nature, Piedmont Park is a cultural landmark hosting art festivals,
    concerts, sports, and Atlanta’s most well-known community traditions.
    """)

    st.markdown("### Popular Cultural Spots")
    st.write("""
    - The Meadow  
    - Piedmont Green Market  
    - Active Oval  
    - Dog Parks  
    - Sports courts  
    - Community events and festivals  
    """)

    st.image("culture_photo.jpg", caption="Community events at the park")


# INTERACTIVE MAP -------------------------------------------------
elif page == "Interactive Map":
    st.title("🗺️ Interactive Map of Piedmont Park")

    st.write("Explore key attractions, walking trails, and historical points.")

    # Center of Piedmont Park
    m = folium.Map(location=[33.7851, -84.3738], zoom_start=15)

    # EXAMPLE MARKERS — customize these:
    folium.Marker(
        [33.7856, -84.3720],
        popup="Lake Clara Meer",
        tooltip="Lake Clara Meer"
    ).add_to(m)

    folium.Marker(
        [33.7837, -84.3769],
        popup="Active Oval",
        tooltip="Active Oval"
    ).add_to(m)

    folium.Marker(
        [33.7859, -84.3752],
        popup="The Meadow",
        tooltip="The Meadow"
    ).add_to(m)

    st_folium(m, width=1000, height=600)


# VIDEOS PAGE -----------------------------------------------------
elif page == "Videos":
    st.title("🎥 Nature & Wildlife Video Collection")

    st.write("""
    These videos highlight Piedmont Park's atmosphere, wildlife, 
    and recreational activities (curated by **Lara**).
    """)

    # Upload or embed YouTube links:
    st.subheader("Around the Lake")
    st.video("YOUR_YOUTUBE_LINK_1")

    st.subheader("Trees & Wildlife")
    st.video("YOUR_YOUTUBE_LINK_2")

    st.subheader("Sports & Recreation")
    st.video("YOUR_YOUTUBE_LINK_3")


# BROCHURE PAGE ---------------------------------------------------
elif page == "Brochure":
    st.title("📄 Brochure (Arianna)")

    st.write("""
    Download or view the physical tri-fold brochure that highlights key attractions 
    and cultural features of Piedmont Park.
    """)

    brochure_path = "brochure.pdf"   # Put in same folder

    with open(brochure_path, "rb") as f:
        st.download_button("Download Brochure PDF", f, file_name="PiedmontPark_Brochure.pdf")

    st.image("brochure_preview.png", caption="Preview of brochure design")
