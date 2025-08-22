import streamlit as st
import info
import base64
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(layout="wide")

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
        expander = st.expander(f"# **{job_title}**")
        for image in images:
            try:
                expander.image(image)
            except:
                continue
        for bullet in job_description:
            expander.markdown(bullet)
    st.write("---")


def experience(data):
    for job_title, (job_description, image) in data.items():
        with st.expander(f"# **{job_title}**"):
            col1, col2, col3 = st.columns(3)
            with col2:
                st.image(image, width=150)
            for bullet in job_description:
                st.markdown(bullet)
    st.write("---")

st.header("Published Paper")

with st.expander("Beyond Buzzwords: Making Sustainability a Pillar of the Computing Curriculum"):
    pdf_viewer(
        "Paper.pdf",
        width="90%",            
        height=800,
        viewer_align="center",   
    )

# with st.expander("Beyond Buzzwords"):
#     st.download_button("Download PDF", data=open("Paper.pdf", "rb"), file_name="Beyond Buzzwords: Making Sustainability a Pillar of the Computing Curriculum.pdf")

st.header("Projects")
project(info.projects_data)

st.header("Experience")
experience(info.experience_data)


