import streamlit as st
from pypdf import PdfReader

# -----------------------------
# PAGE TITLE
# -----------------------------

st.title("🎯 AI Interview Coach")

# -----------------------------
# FILE UPLOAD
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload Your Resume",
    type=["pdf"]
)

# -----------------------------
# ROLE SELECTION
# -----------------------------

role = st.selectbox(
    "Select Target Role",
    [
        "📊 Data Analyst",
        "📈 Business Analyst",
        "📊 Data Scientist",
        "🤖 AI Engineer",
        "🧠 Machine Learning Engineer",
        "💻 Software Engineer"
    ]
)

# -----------------------------
# START INTERVIEW BUTTON
# -----------------------------

if st.button("Start Interview"):
    st.success(f"Preparing interview for {role}")

# -----------------------------
# PROCESS RESUME
# -----------------------------

if uploaded_file:

    # Read PDF
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    # -----------------------------
    # SECTION EXTRACTION FUNCTION
    # -----------------------------

    def extract_section(text, start_keyword, end_keyword):

        start = text.find(start_keyword)

        if start == -1:
            return "Not Found"

        end = text.find(end_keyword, start)

        if end == -1:
            return text[start:]

        return text[start:end]

    # -----------------------------
    # EXTRACT SECTIONS
    # -----------------------------

    skills_section = extract_section(
        text,
        "SKILLS",
        "PROJECTS"
    )

    projects_section = extract_section(
        text,
        "PROJECTS",
        "CERTIFICATIONS"
    )

    # -----------------------------
    # SKILL DETECTION
    # -----------------------------

    known_skills = [
        "Python",
        "SQL",
        "Java",
        "FastAPI",
        "React",
        "Docker",
        "MLflow",
        "Power BI",
        "Machine Learning",
        "NLP",
        "Scikit-learn",
        "Git",
        "GitHub Actions",
        "Pandas",
        "NumPy",
        "Sentence Transformers"
    ]

    found_skills = []

    for skill in known_skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    # -----------------------------
    # PROJECT DETECTION
    # -----------------------------

    known_projects = [
        "AI Travel Companion",
        "Customer Churn Prediction",
        "Unlocking Societal Trends in Aadhaar Enrolment"
    ]

    found_projects = []

    for project in known_projects:
        if project.lower() in text.lower():
            found_projects.append(project)

    # -----------------------------
    # NAME EXTRACTION
    # -----------------------------

    first_line = text.split("\n")[0]
    candidate_name = first_line[:40]

    # -----------------------------
    # SIDEBAR
    # -----------------------------

    with st.sidebar:

        st.header("👤 Candidate Profile")

        st.write(f"**Name:** {candidate_name}")

        st.write(f"**Target Role:** {role}")

        st.write("### 🛠 Skills Found")

        for skill in found_skills:
            st.write(f"✅ {skill}")

        st.write("### 🚀 Projects Found")

        for project in found_projects:
            st.write(f"📌 {project}")

    # -----------------------------
    # MAIN PAGE
    # -----------------------------

    st.subheader("🛠 Skills Section")
    st.write(skills_section)

    st.subheader("🚀 Projects Section")
    st.write(projects_section)

    # -----------------------------
    # FULL RESUME
    # -----------------------------

    with st.expander("📄 View Full Resume Text"):
        st.write(text)