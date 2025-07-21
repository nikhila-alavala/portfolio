import streamlit as st
import info

#About Me
def about_me():
    co1, col2, col3 = st.columns(3)
    with col2:
        st.header("About Me")
        st.image(info.profile_picture, width=200)
    st.write(info.about_me)
    st.write('---')

about_me()

def links():
    st.sidebar.header("Links")
    st.sidebar.write("Connect with me on LinkedIn!")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
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
            expander.image(image, use_container_width=True)
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

st.header("Projects")
project(info.projects_data)

st.header("Experience")
experience(info.experience_data)
