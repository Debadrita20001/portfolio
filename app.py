import streamlit as st
from PIL import Image

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Debadrita Neogi | Portfolio", page_icon="📊", layout="wide")

# ------------- PROFILE IMAGE -------------
# Replace 'profile.jpg' with your actual profile image filename
profile_pic = Image.open("Debadrita.jpeg")

# ------------- SIDEBAR -------------
with st.sidebar:
    st.image(profile_pic, width=200)
    st.title("Debadrita Neogi")
    st.write("📍 Kolkata, India")
    st.markdown("[📧 Email](mailto:debadrita.neogi24-26@bibs.co.in)")
    st.write("📞 8777740811")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/debadrita-neogi)")
    st.markdown("[🐙 GitHub](https://github.com/Debadrita20001)")

# ------------- MAIN CONTENT -------------
st.title("📌 Portfolio of Debadrita Neogi")

# ---- Summary ----
st.header("🔍 Summary")
st.write("""
Data-driven and insight-powered professional combining business strategy with analytics to transform complex data into actionable decisions that drive growth.
""")

# ---- Education ----
st.header("🎓 Education")
st.write("""
**MBA - PGPBA & DS**, Bengal Institute of Business Studies  
📅 2024 – Present  

**B.Tech in Computer Science and Business System**, Sister Nivedita University  
📅 2019 – 2023 | 🧮 75%  

**XII – WBCHSE**, Loreto St Mary's Higher Secondary School  
📅 2019 | 📊 61%  

**X – WBBSE**, Holy Child Girl's Higher Secondary School  
📅 2017 | 📊 69%
""")

# ---- Work Experience ----
st.header("💼 Experience")
st.write("""
**Data Analyst Intern**, Unified Mentor Pvt Ltd  
📅 Jun 2024 – Jul 2024  
- Designed and developed interactive dashboards using Power BI.  
- Transformed raw data into meaningful insights for decision-making.

**Python Programming Intern**, Codsoft  
📅 Aug 2024  
- Developed and implemented Python-based solutions for assigned tasks.
""")

# ---- Skills ----
st.header("🛠️ Skills")

cols = st.columns(3)
with cols[0]:
    st.markdown("**Programming Languages**")
    st.write("- Python")
    st.write("- SQL")
with cols[1]:
    st.markdown("**Tools & Software**")
    st.write("- Excel")
    st.write("- Power BI")
    st.write("- Tableau")
    st.write("- MySQL")
with cols[2]:
    st.markdown("**ML & Libraries**")
    st.write("- Regression, Classification, Clustering, Neural Networks")
    st.write("- Numpy, Pandas, Matplotlib, Scikit-learn")

# ---- Projects ----
st.header("📁 Projects")
st.write("""
**Air Quality Analysis**  
A Machine Learning project in Python analyzing air quality and predicting areas needing improvement.

**Zomato Global Restaurant Data Analysis**  
Extracted insights on ratings, cuisines, and city trends.
""")

# ---- Certifications ----
st.header("📜 Certifications")
st.write("""
- Python Programming Internship – CodSoft  
- Data Analyst Internship – Unified Mentor Pvt Ltd  
- Advance Excel & Power BI – E&ICT Academy, IIT Kanpur  
- Machine Learning with Python – Winter Training by E&ICT Academy, IIT Kanpur
""")

# ---- Achievements ----
st.header("🏆 Achievements")
st.write("""
- Successfully completed internships in Python and Data Analytics.  
- Trained at IIT Kanpur on Machine Learning with Python.
""")

# ---- Hobbies & Interests ----
st.header("🎨 Hobbies & Interests")
st.write("""
- Traveling ✈️  
- Exploring New Cuisines 🍜  
- Photography 📸  
- Writing ✍️
""")

# ---- Footer ----
st.markdown("---")
st.write("© 2025 Debadrita Neogi | Made with ❤️ using Streamlit")

