import streamlit as st
import info

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    div.streamlit-expanderHeader p {
        font-size:30px;
        font-weight:bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#About Me 
def about_me():
    st.markdown("<h1 style='text-align: center;'>About Me</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1]) 
    with col2:
        st.image(info.profile_picture)
    st.write(info.about_me)
    st.write('---')

about_me()

def links():
    st.sidebar.header("Links")
    st.sidebar.write("Connect with me on LinkedIn!")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.write("Check out my projects!")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width = "75" height="75"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)    
    st.sidebar.write("Email Me!")
    email_link = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width = "75" height="75"></a>'
    st.sidebar.markdown(email_link, unsafe_allow_html=True)
links()

def education(education_data, course_data):
    st.header("Education")
    st.subheader(f'**{education_data["Institution"]}**')
    for name in education_data.keys():
        st.write(f'**{name}:** {education_data[name]}')

education(info.education_data, info.course_data)

def project(data):
    for job_title, (job_description, images) in data.items():
        with st.expander(f"# **{job_title}**"):
            for image in images:
                try:
                    st.image(image)
                except:
                    continue
            for bullet in job_description:
                    st.markdown(bullet)
    st.write("---")


def experience(data):
    for job_title, (job_description, image) in data.items():
        with st.expander(f"# **{job_title}**"):
            col1, col2, col3 = st.columns([2, 1, 2])
            with col2:
                st.image(image, width= 200)
            for bullet in job_description:
                st.markdown(bullet)
    st.write("---")

st.header("Published Paper")

with st.expander("Beyond Buzzwords: Making Sustainability a Pillar of the Computing Curriculum"):
    st.markdown("""**Abstract:**\\
                The rapid digitalization of the global economy, driven by big data and artificial intelligence, has significantly increased energy consumption, reshaped labor markets, and impacted politics and communities to an extraordinary extent. Addressing these challenges involves educating future computer scientists about the carbon emissions associated with their code and the broader societal consequences of the technologies they design. Traditionally, computing education has focused on optimizing runtime and memory efficiency, frequently overlooking the links to energy efficiency and carbon footprint considerations. Additionally, the integration of ethics into the curriculum has not been comprehensive. This paper proposes a framework for integrating sustainability into the computing curriculum, prioritizing it as a critical consideration for students. It outlines the competencies required for sustainability education and identifies topics directly related to the UN SDGs as a natural entry point for sustainability concepts. Additionally, it reports on a pilot framework implementation at a major US public university, where over 3,200 students from over 30 disciplines were exposed to sustainable coding practices and the ethics of AI and machine learning. The curriculum incorporated transformative teaching and learning methodologies with lectures, supplemental materials, and interactive projects highlighting these themes. Challenges to implementation, which may be encountered by other institutions, are also discussed. Survey results demonstrate that sustainability can be seamlessly integrated into early coding education, encouraging ongoing effort to accentuate energy-efficient coding in computer science courses.""")
    st.markdown(
        "[Read the full paper on ACM Digital Library](https://dl.acm.org/doi/10.1145/3724363.3729034)",
        unsafe_allow_html=True
    )

# with st.expander("Beyond Buzzwords"):
#     st.download_button("Download PDF", data=open("Paper.pdf", "rb"), file_name="Beyond Buzzwords: Making Sustainability a Pillar of the Computing Curriculum.pdf")

st.header("Projects")
project(info.projects_data)

st.header("Experience")
experience(info.experience_data)


