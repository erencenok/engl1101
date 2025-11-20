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
    st.markdown("**The Meadow — a quiet green area with skyline views.**")


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

    st.image(
    "media/IMG_7936.jpeg",
    use_column_width=True,
    caption="Pathway in Piedmont Park"
)
    st.write("""
**Sources:**
- https://www.georgiaencyclopedia.org/articles/geography-environment/piedmont-park/
- https://www.piedmontpark.org/history/
""")


# ---------------------- ECOLOGY ----------------------
elif page == "Ecology":
    st.title("🌿 Ecology & Environmental Features")

    st.write("""
Piedmont Park in Atlanta, Georgia, is more than just expansive lawns with a skyline view of the city; it's a rich ecological space nestled in the heart of a densely urbanized area. It covers over 200 acres in Midtown and is called “Atlanta’s green heart” due to its size and its role in cooling the city by filtering air and providing habitat for wildlife.

Ecologically, one of the park’s most important features is its variety of habitats. These include open meadows, shaded oak and hardwood groves, gardens, woodland patches, and the man-made Lake Clara Meer. Together, they form a mosaic of microhabitats that support a wide range of organisms. Recent tree-planting efforts have added dozens of native trees—74 in a single 2020 project—especially near Oak Hill, the Meadow, and the dog parks. These trees reduce temperatures, improve air quality, store carbon, and provide food and nesting sites for birds, squirrels, chipmunks, and other wildlife.

Lake Clara Meer plays a central role in the park’s ecology. Although artificial, it functions like an urban wetland, supporting ducks, herons, turtles, fish, insects, and other aquatic life that form the base of a complex food web. A wooden boardwalk allows visitors to experience this habitat without disturbing its sensitive shoreline.

Piedmont Park is also one of Atlanta’s most significant urban bird habitats. Local birders have documented around 180 species over the decades. Native species like Carolina Chickadees stay year-round, while migratory warblers and kinglets arrive during spring and fall. Winter visitors include Tufted Titmice, Ruby-crowned Kinglets, Carolina Wrens, and Eastern Phoebes, making the park ecologically active even in colder months.

The meadows and gardens add another dimension of ecological value. Collaborations with organizations such as Trees Atlanta have introduced native grasses and wildflowers, creating pollinator-friendly meadows that support bees, butterflies, and other insects—vital at a time of global pollinator decline.

All of this exists within the broader context of Atlanta’s changing urban ecology. As development expands and forests shrink, Piedmont Park serves as an essential refuge for species that might otherwise disappear from the city. The Piedmont Park Conservancy and the City of Atlanta emphasize these ecological functions as part of a long-term strategy to maintain biodiversity and ecosystem services.

Overall, Piedmont Park is shaped by both natural processes and deliberate restoration efforts. From lake remediation to meadow creation and extensive tree planting, the park has become a thriving ecosystem in the center of a rapidly growing city—demonstrating that urban green spaces can support deep ecological life alongside recreation and community activity.
""")

    st.image(
    "media/IMG_7960.jpeg",
    caption="The Meadow — a large open habitat supporting pollinators, birds, and native plants.",
    use_column_width=True
)

    st.write("""
**Sources:**
- Piedmont Park Conservancy — https://piedmontpark.org/about-us/
- Discover Atlanta — https://discoveratlanta.com/things-to-do/outdoors/piedmont-park/
""")


# ---------------------- CULTURE ----------------------
elif page == "Culture":
    st.title("🎭 Cultural Significance")

    st.write("""
Piedmont Park hosts some of Atlanta’s most iconic annual festivals and cultural celebrations.
These events highlight the city’s diverse communities, creative talent, and long-standing traditions.
Many of these events are free and bring thousands of visitors to the park each year.
""")

    # ---------------- Dogwood Festival ----------------
    st.header("🌸 Atlanta Dogwood Festival (April)")
    st.write("""
The Atlanta Dogwood Festival is one of the city’s oldest traditions, held every April to celebrate 
the blooming of dogwood trees. The festival includes a fine arts market, musical performances, 
and food vendors across Piedmont Park.
""")
    st.image("media/dog.JPG", caption="Atlanta Dogwood Festival")

    st.markdown("---")

    # ---------------- Jazz Festival ----------------
    st.header("🎷 Atlanta Jazz Festival (May)")
    st.write("""
One of the largest free jazz festivals in the country, the Atlanta Jazz Festival takes place every 
Memorial Day weekend. It showcases legendary performers, emerging artists, and a month-long 
series of jazz events leading up to the main festival in the park.
""")
    st.image("media/jazz.jpg", caption="Atlanta Jazz Festival")

    st.markdown("---")

    # ---------------- Arts Festival ----------------
    st.header("🎨 Piedmont Park Arts Festival (August)")
    st.write("""
The Piedmont Park Arts Festival is a two-day outdoor celebration of visual arts featuring up to 
250 artists, live demonstrations, local food vendors, and children’s activities. It is one of Midtown’s 
most beloved art-focused events.
""")
    st.markdown("---")

    # ---------------- Shaky Knees ----------------
    st.header("🎸 Shaky Knees Festival (September)")
    st.write("""
Shaky Knees is a major alternative rock music festival that took place in Piedmont Park for the 
first time in 2025. The festival attracts huge crowds and features well-known headliners from 
around the world.
""")
    st.image("media/shakyknees.jpg", caption="Shaky Knees Festival at Piedmont Park")

    st.markdown("---")

    # ---------------- Pride ----------------
    st.header("🌈 Atlanta Pride & Atlanta Black Pride (Sept–Oct)")
    st.write("""
Atlanta Pride is one of the largest free Pride festivals in the United States, held annually in 
Piedmont Park. Atlanta Black Pride, held on Labor Day weekend, is one of the largest Black 
LGBTQIA+ celebrations in the world. Both festivals bring vibrant parades, performances, and 
community gatherings to the park.
""")
    st.image("media/pride.png.webp", caption="Atlanta Pride Festival")

    st.markdown("---")

    # ---------------- Sources ----------------
    st.subheader("Sources")
    st.write("""
- https://dogwood.org/  
- https://atljazzfest.com/  
- https://piedmontparkartsfestival.com/  
- https://www.atlantanewsfirst.com/2025/09/20/shaky-knees-2025-kicks-off-piedmont-park/  
- https://atlantapride.org/  
""")

# ---------------------- INTERACTIVE MAP ----------------------
elif page == "Interactive Map":
    st.title("🗺️ Routes")
    st.write("Explore Piedmont Park using an interactive map with photos, videos, and walking routes — including Lara’s, Ariana’s, and Eren’s favorite paths.")

    m = folium.Map(location=[33.7851, -84.3738], zoom_start=16, tiles="CartoDB positron")

    # ----------------------------------------------------
    # MARKERS WITH POPUPS (add your images into /media)
    # ----------------------------------------------------

    # Lake Clara Meer
    lake_popup = folium.Popup("""
        <h4>Lake Clara Meer</h4>
        <img src='media/lake.jpg' width='220'>
        <p>A peaceful lake with ducks, turtles, and skyline reflections.</p>
    """, max_width=260)

    folium.Marker(
        (33.784089977396995, -84.37297344943022),
        tooltip="Lake Clara Meer",
        popup=lake_popup,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

    # Active Oval
    oval_popup = folium.Popup("""
        <h4>Active Oval</h4>
        <img src='media/oval.jpg' width='220'>
        <p>Running track, recreation fields, and fitness paths.</p>
    """, max_width=260)

    folium.Marker(
        (33.786417322689346, -84.37607408312104),
        tooltip="Active Oval",
        popup=oval_popup,
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(m)

    # The Meadow
    meadow_popup = folium.Popup("""
        <h4>The Meadow</h4>
        <img src='media/meadow.jpg' width='220'>
        <p>A calm open field perfect for reading, picnics, and skyline views.</p>
    """, max_width=260)

    folium.Marker(
        (33.78339296107428, -84.37157950990911),
        tooltip="The Meadow",
        popup=meadow_popup,
        icon=folium.Icon(color="orange", icon="info-sign")
    ).add_to(m)

    # Dog Park
    dog_popup = folium.Popup("""
        <h4>Dog Park</h4>
        <img src='media/dog.jpg' width='220'>
        <p>One of Midtown's largest off-leash areas for dogs.</p>
    """, max_width=260)

    folium.Marker(
        (33.78819038380616, -84.3709058638687),
        tooltip="Dog Park",
        popup=dog_popup,
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

    # Atlanta Botanical Garden
    garden_popup = folium.Popup("""
        <h4>Atlanta Botanical Garden</h4>
        <img src='media/garden.jpg' width='220'>
        <p>Beautiful curated gardens connected directly to Piedmont Park.</p>
    """, max_width=260)

    folium.Marker(
        (33.789986280083774, -84.37252046600035),
        tooltip="Atlanta Botanical Garden",
        popup=garden_popup,
        icon=folium.Icon(color="purple", icon="info-sign")
    ).add_to(m)

    # Midtown Reflection View (Eren's ending point)
    reflection_popup = folium.Popup("""
        <h4>Midtown Reflection View</h4>
        <p>Eren's favorite place to watch the skyline reflect on the lake.</p>
    """, max_width=250)

    folium.Marker(
        (33.78399315908114, -84.3733409337844),
        tooltip="Midtown Reflection View",
        popup=reflection_popup,
        icon=folium.Icon(color="darkblue", icon="star")
    ).add_to(m)

    # ----------------------------------------------------
    # SUGGESTED WALKING ROUTE (BLUE)
    # ----------------------------------------------------

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

    # ----------------------------------------------------
    # LARA'S FAVORITE ROUTE (RED)
    # ----------------------------------------------------

    laras_route = [
        (33.784089977396995, -84.37297344943022),
        (33.785500, -84.373400),
        (33.786417322689346, -84.37607408312104)
    ]

    folium.PolyLine(
        laras_route,
        tooltip="Lara's Favorite Route",
        color="red",
        weight=4,
        opacity=0.9
    ).add_to(m)

    # ----------------------------------------------------
    # ARIANA'S FAVORITE ROUTE (PURPLE)
    # Botanical Garden → Scenic Hill → Oak Hill → Meadow
    # ----------------------------------------------------

    arianas_route = [
        (33.789986280083774, -84.37252046600035),  # Botanical Garden
        (33.788700, -84.373500),                   # lowered to avoid lake
        (33.787300, -84.374500),                   # Oak Hill path
        (33.785800, -84.374000),                   # approach meadow safely
        (33.78339296107428, -84.37157950990911)    # Meadow
    ]

    folium.PolyLine(
        arianas_route,
        tooltip="Ariana's Favorite Route",
        color="purple",
        weight=4,
        opacity=0.9
    ).add_to(m)

    # ----------------------------------------------------
    # EREN'S FAVORITE ROUTE (ORANGE)
    # Dockside → lakeside dirt path → Midtown Reflection View
    # ----------------------------------------------------

        erens_route = [
        (33.7841148168333, -84.37711797555849),   # Dockside
        (33.783900, -84.376300),                  # lower path
        (33.783750, -84.375300),                  # hugging lake edge
        (33.783700, -84.374300),                  # approaching reflection area
        (33.78399315908114, -84.3733409337844)    # Reflection marker
    ]

    folium.PolyLine(
        erens_route,
        tooltip="Eren's Favorite Route",
        color="orange",
        weight=4,
        opacity=0.9
    ).add_to(m)

    # ----------------------------------------------------
    # RENDER MAP
    # ----------------------------------------------------

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

    pdf_path = "media/brochure.pdf"

    try:
        with open(pdf_path, "rb") as pdf:
            st.download_button(
                label="📥 Download Brochure",
                data=pdf,
                file_name="Piedmont_Park_Brochure.pdf",
                mime="application/pdf"
            )

        st.success("Brochure is ready for download!")

    except FileNotFoundError:
        st.error("❌ Brochure file not found. Make sure it's saved as media/brochure.pdf.")


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
