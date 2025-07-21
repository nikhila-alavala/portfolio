#This File will contain the information to be displayed in your portfolio

# PROFILE
profile_picture = "Images/profile.jpg"
about_me = (
    """I'm currently working as a Pricing Analyst at Veritiv. I have a Master's in Analytics from Georgia Tech with a focus in Computational Data Analysis.
       I’m an incredibly driven individual with a hunger for experience and knowledge. I got my first internship at the age of 15. I strive to make a lasting positive impact wherever I go and strongly believe I can do so with a background in Analytics.
       I am passionate about sustainability and believe that using analytics to empower companies to make more sustainable decisions is key to saving our planet."""
)

# CONTACT & SOCIALS
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://toppng.com/uploads/preview/email-icon-vector-circle-11549825158ieiklzfl8g.png"
my_linkedin_url = "https://www.linkedin.com/in/nikhila-alavala/"
my_github_url = "https://github.com/your-github-username"  # Update with your actual GitHub
my_email_address = "nikhiATL@gmail.com"

# EDUCATION
education_data = {
    'Degree': 'Master of Science in Analytics',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': 'May 2025',
    'GPA': '3.9'
}

# COURSES
course_data = {
    "code": ["ISYE 6501", "CS 7641", "MGT 6203", "MGT 6359", "MGT 6311"],
    "names": ["Analytics Modeling", "Machine Learning", "Data Analytics", "Revenue Management", "Visual Analytics"],
    "semester_taken": ["Spring 2024", "Spring 2024", "Spring 2024", "Summer 2024", "Fall 2024"],
    "skills": [
        "Statistical modeling and optimization techniques",
        "Supervised/unsupervised learning, SVMs, neural nets",
        "Exploratory data analysis and dashboards",
        "Pricing and forecasting models in business",
        "Data visualization using Tableau and D3.js"
    ],
}

# EXPERIENCE
experience_data = {
    "Pricing Analyst – Veritiv": (
        ["- Built automation replacing macros with a python solution, saving a $11M campaign from 4-day delay in my first week",
        "- Identified $4M of profit opportunity by implementing a minimum order quantity, earning C-Suite recognition",
        "- Collaborated with 12 regional sales managers to identify strategic margin increases, generating $200K in profit",
        "- Automated price setting for 1,421 online products with an Alteryx workflow, saving 326 hours of manual work",
        "- Developed web scraping code to find pricing for 3 competitors using BeautifulSoup, improving input data accuracy by 20%",
         ],
        "images/veritiv.jpg"
    ),
    "E-commerce Operations Intern – Walmart (Sam’s Club)": (
        ["- Identified and championed initiatives focused on new premium memberships, driving $50M in incremental revenue",
         "- Designed and presented a sustainability initiative to replace electronic sliding doors with high-speed doors, reducing cooling leakages and resulting in annual savings of $3.1M and a 22M lb reduction in carbon emissions, which was accepted and implemented by the VP of Real Estate"],
        "images/walmart.jpg"
    ),
    "Revenue Management Commercial Cargo Co-Op – Delta Air Lines": (
        ["- Published Tableau dashboard on customer no-show trends, enabling $10M in overbooking revenue in Q1 of 2022",
        "- Produced the first ever visualization of demand vs. inventory over the flight booking window using matplotlib and pandasql, enabling strategic inventory management initiatives",
        "- Built 7 Tableau Dashboards used daily by pricing and inventory team, enabling cross-functional team collaboration",
        "- Analyzed performance of dynamic cargo pricing initiatives by creating a new win/loss metric on Tableau"
        "- Presented projects and key findings to senior leadership on six occasions throughout the co-op"
        ],
        "images/delta.png"
    ),
}

# PROJECTS
projects_data = {
    "Sanction Efficacy ML Model": (
        [
            """
        - **Overview**
            - Spurred by news of sweeping tariffs introduced by the Trump administration, my group from my machine learning class and I chose to focus our project on sanction efficacy. Our group wanted to understand historically what made sanctions successful or not.

        - **Responsibilities** 
            - **Created and tuned a Random Forest model** to predict sanction success or failure
            - **Led model evaluation and error analysis**, focusing on improving accuracy and understanding misclassifications

        - **Model Performance**

            | Metric        | Tuned Model |
            |---------------|-------------|
            | F1 Score      |    82.57%   |
            | AUC-ROC       |    82.77%   |

        - **Key Findings from SHAP Analysis**
            - Features contributing to **successful sanctions** included:
                - **High GDP of the sanctioning state**
                - **Financial sanctions**
                - **African-led sanctions**
                
            - Features contributing to **failed sanctions** included:
                - Sanctioned states in **Asia or Europe**
                - Broad objectives like **policy change**, **regime destabilization**, or **counter-terrorism**
            """
        ],
        ["Images/sanctions.png"]
    ),
    "Screen Time Carbon Emissions Tracker": (
        [ """
            - **Overview**
                - Social media platforms rely on energy-intensive AI algorithms to deliver personalized experiences.
                Users are largely unaware of the environmental impact of their social media usage. 
                GreenScreen is an app that tracks a user's social media usage and reports on the emissions produced from their screen time.

            - **Features**    
                - Pie Chart breakdown of time spent on apps on a daily basis
                - Weekly emissions trend 
                - Adjustable screen time goal 
                - Usage equivalences with aggregated trends
                - Bar chart breakdown of number of minutes spent on each app & carbon emissions 
                - Tips on reducing screen time emissions
            """
        ],
        ["Images/pages.jpg","Images/screens.png"]
    ),
    # "Graduate Research on Sustainable Coding": (
    #     [
    #         "- Integrated sustainable coding practices into 3 core computer science courses",
    #         "- First author of an ACM-published peer-reviewed paper accepted at ITiCSE 2024",
    #         "- Applied PCA, LSA, LDA, and mutual information to support curriculum redesign"
    #     ],
    #     ["images/tips.jpg"]
    # ), 
    "Carbon Emissions Travel Calculator": (
        [ """
            - **Overview**
                - To encourage travelers to consider the carbon emissions of traveling to their destination, our group created an interactive carbon emissions calculator that helps users choose travel destinations based on air or road emissions. 
            
            - **Methodology**    
                - Used Google Maps and CarbonInterface APIs to compute travel emissions
                - Built an ETL pipeline for flight data (15+ MB)
                - Developed a custom match score for sustainable flight options
                - Visualized results on an interactive map
            """
        ],
        ["Images/Carbon_calc.png"]
    ),
}

# PROGRAMMING SKILLS
programming_data = {
    "Python": 90,
    "SQL": 85,
    "R": 60,
    "Scala": 50,
}

programming_icons = {
    "Python": "🐍",
    "SQL": "🗃️",
    "R": "📊",
    "Scala": "🧬"
}

# SPOKEN LANGUAGES
spoken_data = {
    "English": "Fluent",
}

spoken_icons = {
    "English": "🇺🇸"
}

# LEADERSHIP / OTHER
leadership_data = {
    "Graduate Teaching Assistant – Georgia Tech": (
        ["- Led lab sessions and graded assignments for Database Systems", 
         "- Guided students in SQL, ER modeling, and database design"],
        "images/ta.jpg"
    ),
    "Student Ambassador – College of Business": (
        ["- Represented the college in outreach and recruitment events"],
        "images/ambassador.jpg"
    )
}

# ACTIVITIES
activity_data = {
    "Exchange Semester – Bocconi University, Milan": [
        "- Studied International Business and European Economics",
        "- Gained global exposure and cross-cultural collaboration experience"
    ]
}
