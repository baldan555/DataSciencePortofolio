import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import MallCustomerClusteringDash
import MNIST_st
import rhizomes_st
import stockapp
import churnpredict_st
import creditRiskApp
import heart_failure_st
import lungcancerpredict_st
import diseasediagnosisandrecommender_st
import TelcoCustomerChurnDash
import nyctaxianomalyApp
import studentperfomance_st
import airqualitypredict
import manufactureDefectApp
import HandGestureRecog 
import faceemotionApp
import sentimentApp
import f1detectApp


# Add custom CSS to hide the GitHub icon

hide_github_icon = “”"
.css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK{ display: none; } #MainMenu{ visibility: hidden; } footer { visibility: hidden; } header { visibility: hidden; }
“”"
st.markdown(hide_github_icon, unsafe_allow_html=True)
# Your app code goes here
st.set_page_config(page_title="Kumpulan Aplikasi Streamlit ", layout="wide")

# Reset session state untuk aplikasi
if "active_app" not in st.session_state:
    st.session_state.active_app = None

# Membuat navbar di bagian atas halaman
selected_nav = option_menu(
    menu_title=None,  # Hapus judul menu untuk navbar
    options=["About Me", "CV", "Portofolio", "Contact"],
    icons=["person", "file-earmark-person", "folder2", "envelope"],
    menu_icon="info-circle",
    default_index=0,
    orientation="horizontal",  # Orientasi horizontal untuk navbar
)

if selected_nav == "About Me":
    # Mengatur layout halaman


    # CSS untuk mendesain tampilan kartu
    st.markdown("""
        <style>
        .card {
            background-color: #f8f9fa;
            padding: 20px;
            margin: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        }
        .card img {
            border-radius: 10px;
            width: 100%;
            height: auto;
            margin-bottom: 15px;
        }
        .card p {
            font-size: 16px;
            color: #333;
        }
        </style>
        """, unsafe_allow_html=True)

    # Desain kartu
    st.markdown("""
        <div class="card">
            <img src="https://media.licdn.com/dms/image/v2/D5603AQGDLd_z2CSC3w/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1677050502605?e=1731542400&v=beta&t=pu3r1KdJ8OPenkD_6__I6Bo96MMiKvnuojkK_lHtLCA" alt="Foto">
            <p>
                Since childhood, I have grown up in an office environment that introduced me to computers, the internet, technology, and software. This experience grew my interest in pursuing the field of computer science. Nowadays, data has become a highly valuable asset, even considered more valuable than fuel. This belief has driven me to focus on the fields of data, machine learning, and artificial intelligence because I believe they can transform our civilization and make it easier. I have high hopes that the skills and abilities I possess, as well as those I will continue to develop, can help address various challenges faced by companies. I aspire to be part of the solution for data-related problems and leverage technology to enhance efficiency and innovation. I firmly believe that with expertise in this field, I can significantly contribute to the success of companies and tackle data-related phenomena. I believe that through dedication and continuous self-improvement, I will be able to provide innovative and effective solutions to overcome existing challenges. I am confident that with the skills and knowledge I have acquired, I can make a positive impact on companies and society as a whole. Together, we can create a better future by harnessing the immense potential embedded in data, machine learning, and artificial intelligence.
            </p>
        </div>
        """, unsafe_allow_html=True)
      


    
    
elif selected_nav == "CV":
    st.markdown("""
    # <div style='text-align: center; margin-bottom: -15px;'>N.I.S. BALDANULLAH</div>
    ### <div style='text-align: center; margin-bottom: -10px;'>Data Enthusiast</div> 
    <div style='text-align: center; margin-bottom: -10px;'>Jakarta, Indonesia</div>  
    <div style='text-align: center;'>+6281245941155 | baldanullah55@gmail.com | <a href='https://www.linkedin.com/in/n-i-s-baldanullah-a666351b7/'>LinkedIn Profile</a></div>
    """, unsafe_allow_html=True)

    st.write("")

    # Profile Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>ABOUT ME</div>
    <hr style="border:2px solid black; margin-top: -40px;">
    <p style='text-align: justify;'>
    I am an enthusiastic fan of technology in the field of data science, studying informatics engineering at Pancasila University. 
    The vast potential in data science has attracted my interest, especially its accurate ability to solve various problems in our society. 
    By utilizing knowledge from campus and self-learning using various free resources and content, I have gained practical experience and applied my knowledge. 
    With my abilities, talents, and enthusiasm, I believe I am well-suited to drive meaningful progress both within organizations and in society at large.
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    # Experience Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>EXPERIENCE</div>
    <hr style="border:2px solid black; margin-top: -40px;">

    #### **Big Data Analyst at Kalla Group**  
    _Aug 2023 — Dec 2023 | Makassar_  
    - Managed large-scale data, including cleansing, storing, and pre-processing
    - Built Machine Learning models such as LSTM, GRU, and Convolutional Neural Network for predicting Asia Bitumen Price
    - Developed and deployed a machine learning model to predict and visualize Asia Bitumen prices in an interactive web app dashboard

    #### **Website Administrator, Editor and Publisher at PT. INIPASTI Communika**  
    _Jan 2020 — Dec 2022 | Makassar_  
    - Monitoring Website Traffic
    - Managing the Server and Hosting Platform
    - Website Content Management
    - User and Access Management
    - Backup and Recovery

    #### **Data Entry Assistant at Institute Social and Political Economic Issue (ISPEI)**  
    _Jan 2014 — Dec 2016 | Makassar_  
    - Developed and maintained data entry guidelines and processes to ensure accuracy and consistency
    - Cleaning and Managing data from input paper into excel
    """, unsafe_allow_html=True)

    st.write("")

    # Education Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>EDUCATION</div>
    <hr style="border:2px solid black; margin-top: -40px;">

    #### **Pancasila University**  
    _Bachelor of Informatics Engineering_  
    _Mar 2020 — Aug 2024 | South Jakarta_
    """, unsafe_allow_html=True)

    st.write("")

    # Projects Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>PROJECTS</div>
    <hr style="border:2px solid black; margin-top: -40px;">

    #### **Capstone Project**  
    _Jun 2023 | Bangkit Academy_  
    Built Machine Learning models to detect vehicle tire quality in vehicle service online booking applications using image processing with CNN (Convolutional Neural Network)

    #### **Interactive Predictive FOB Bitumen Price Dashboard**  
    _Sep 2023 — Nov 2023 | Kalla Group_  
    Built and deployed a machine learning model to predict and visualize Asia bitumen prices in an interactive web app dashboard
    """, unsafe_allow_html=True)

    st.write("")

    # Publication Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>PUBLICATION</div>
    <hr style="border:2px solid black; margin-top: -40px;">

    - **Parallel Processing Pada Pemodelan Machine Learning Menggunakan Random Forest**  
      _May 2023 | Journal of Informatics and Advanced Computing_

    - **Comparison of SAW, WP, and TOPSIS Methods in Determining the Best Journalists**  
      _Oct 2022 — Dec 2022 | Jurnal Riset Informatika_  
      Creating a Decision Support System in deciding the best journalist at the company PT. INIPASTI Communika

    - **Pengujian Aplikasi Belajar Berbasis Website Menggunakan Teknik Equivalence Partitioning**  
      _Nov 2022 | Journal of Informatics and Advanced Computing_
    """, unsafe_allow_html=True)

    st.write("")

    # Courses Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>COURSES</div>
    <hr style="border:2px solid black; margin-top: -40px;">

    - **Data Analyst Python Track** (Jun 2024 - Jul 2024, DQLab)
    

    - **Azure AI Engineer** (Feb 2024 - Mei 2024, KOMINFO Digitalent)
      - Understand Generative AI
      - Understand how to Build an AI from Azure into production

    - **Google Data Analytics** (Jun 2023 — Jun 2023, Coursera)
      - Understand sql and R programming languages
      - Understand how to manage data and perform tabulation commands using sql commands, and analyze data using R

    - **Deep Learning with TensorFlow** (May 2023 — May 2023, Coursera)
      - Understand how to train and build artificial neural network models using image data, voice data using the TensorFlow library

    - **Machine Learning Specialization** (Apr 2023 — Apr 2023, Stanford University)
      - Understand how to model machine learning using linear regression, logistic regression, clustering, and anomaly detection methods

    - **Mathematics for Machine Learning Specialization** (Feb 2023 — Mar 2023, Stanford University)
      - Understand how to model machine learning using linear regression, logistic regression, clustering, and anomaly detection methods

    - **Python Fundamental for Data Science** (Mein 2022 - Jun 2022, DQLab)
      - Understand the basic python for data science such as exporting data, converting raw data to csv, cleaning data and pre-processing data

    - **Data Visualization** (Mar 2022 — Apr 2022, ASEAN Data Science Explorers)
      - Understand how to manage data such as data import, data cleaning, and data visualization
    """, unsafe_allow_html=True)

    st.write("")

    # Certification Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>CERTIFICATION</div>
    <hr style="border:2px solid black; margin-top: -40px;">

    - **TensorFlow Developer Certification** (Issued: Dec 2023 — Dec 2026, Google TensorFlow)
    """, unsafe_allow_html=True)

    st.write("")

    # Skills Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>SKILLS</div>
    <hr style="border:2px solid black; margin-top: -40px;">

    #### Data Analysis:
    - Python
    - SQL
    - Tableau
    - Excel

    #### Machine Learning:
    - Supervised Learning
    - Unsupervised Learning
    - Reinforcement Learning

    #### Deep Learning:
    - Convolutional Neural Network
    - Recurrent Neural Network
    - Object Detection
    - Image Processing

    #### Data Visualization:
    - Matplotlib
    - Plotly
    - Bokeh

    #### Business Intelligence:
    - Tableau
    - Power BI

    #### Data Engineering:
    - SQL
    - Oracle Database
    - DDL
    - DML
    - ETL
    """, unsafe_allow_html=True)

    st.write("")


      # Display the section titles
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>SOFT SKILLS</div>
    <hr style="border:2px solid black; margin-top: -40px;">
    """, unsafe_allow_html=True)

    # Define styles for custom elements
    st.markdown(
        """
        <style>
        .section-title {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin-top: 30px;
        }
        .skill-container {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
        }
        .skill-item {
            width: 30%;
        }
        .language-container {
            display: flex;
            justify-content: space-between;
            padding: 10px 100px;
        }
        .language-item {
            display: flex;
            align-items: center;
        }
        .dot {
            height: 10px;
            width: 10px;
            background-color: black;
            border-radius: 50%;
            display: inline-block;
            margin: 0 2px;
        }
        .empty-dot {
            background-color: lightgray;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


    # Soft skills sliders
    with st.container():
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("Interpersonal Skill")
            st.slider('', 0, 10, 8, key="interpersonal", disabled=True)
        
        with col2:
            st.write("Communication")
            st.slider('', 0, 10, 8, key="communication", disabled=True)
        
        with col3:
            st.write("Collaboration")
            st.slider('', 0, 10, 9, key="collaboration", disabled=True)

    with st.container():
        col1, col2, _ = st.columns([1, 1, 1])

        with col1:
            st.write("Time Management")
            st.slider('', 0, 10, 8, key="time_management", disabled=True)


    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>LANGUAGES</div>
    <hr style="border:2px solid black; margin-top: -40px;">
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="language-container">
            <div class="language-item">
                <span>Indonesia</span>&nbsp;<i>Native</i>&nbsp;&nbsp;
                <span class="dot"></span><span class="dot"></span><span class="dot"></span>
                <span class="dot"></span><span class="dot"></span>
            </div>
            <div class="language-item">
                <span>English</span>&nbsp;<i>Proficient</i>&nbsp;&nbsp;
                <span class="dot"></span><span class="dot"></span><span class="dot"></span>
                <span class="dot"></span><span class="empty-dot"></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )





elif selected_nav == "Portofolio":
    with st.expander("Choose Category", expanded=True):
        selected_category = option_menu(
            "Category",
            ["Machine Learning", "Deep Learning", "Data Visualization", "Business Intelligence"],
            icons=["cpu", "brain", "bar-chart", "pie-chart"],
            menu_icon="list",
            default_index=0,
            orientation="horizontal"
        )

        if selected_category == "Machine Learning":
            selected_app = option_menu(
                "Choose App",
                [
                    "Mall Customer Clustering",
                    "Churn Prediction",
                    "Credit Risk Assessment",
                    "Telco Customer Churn",
                    "NYC Taxi Anomaly Detection",
                    "Heart Failure Prediction",
                    "Lung Cancer Prediction",
                    "Disease Diagnosis and Recommender",
                    "Student Performance",
                    "Air Quality Impact Score Predict",
                    "Manufacture Defect Prediction"
                ],
                icons=[
                    "shop",
                    "person-check",
                    "file-earmark-medical",
                    "people-fill",
                    "taxi",
                    "heart-pulse",
                    "lungs",
                    "stethoscope",
                    "start",
                    "pollution",
                    "factory"
                ],
                menu_icon="briefcase",
                default_index=0,
                orientation="horizontal"

            )


              # Jalankan aplikasi berdasarkan pilihan
            if selected_app == "Mall Customer Clustering":
                MallCustomerClusteringDash.main()
            elif selected_app == "Churn Prediction":
                churnpredict_st.main()
            elif selected_app == "Credit Risk Assessment":
                creditRiskApp.main()
            elif selected_app == "Telco Customer Churn":
                TelcoCustomerChurnDash.main()
            elif selected_app == "NYC Taxi Anomaly Detection":
                nyctaxianomalyApp.main()
            elif selected_app == "Heart Failure Prediction":
                heart_failure_st.main()
            elif selected_app == "Lung Cancer Prediction":
                lungcancerpredict_st.main()
            elif selected_app == "Disease Diagnosis and Recommender":
                diseasediagnosisandrecommender_st.main()
            elif selected_app == "Student Performance":
                studentperfomance_st.main()
            elif selected_app == "Air Quality Impact Score Predict":
                airqualitypredict.main()
            elif selected_app == "Manufacture Defect Prediction":
                manufactureDefectApp.main()

        elif selected_category == "Deep Learning":
            selected_app = option_menu(
                "Pilih Aplikasi",
                [
                    "Draw MNIST Number",
                    "Hand Gesture Recognition",
                    "Face Mood Detect",
                    "YOLOV8 Object Detection",
                    "Stock Forecasting",
                    "Sentiment Analysis",
                ],
                icons=[
                    "hand",
                    "eye",
                    "face",
                    "chart-line",
                    "chat-dots",
                    "gesture"
                ],
                menu_icon="briefcase",
                default_index=0,
                orientation="horizontal"
            )

           
            if selected_app == "Draw MNIST Number":
                MNIST_st.main()
            elif selected_app == "Hand Gesture Recognition":
                HandGestureRecog.main()
            elif selected_app == "Face Mood Detect":
                faceemotionApp.main()
            elif selected_app == "Stock Forecasting":
                stockapp.main()
            elif selected_app == "Sentiment Analysis":
                sentimentApp.main()
            elif selected_app == "YOLOV8 Object Detection":
                f1detectApp.main()




        elif selected_category == "Data Visualization":
            selected_visualization = option_menu(
                "Pilih Library Visualisasi",
                ["Matplotlib", "Plotly"],
                icons=["bar-chart", "graph-up"],
                menu_icon="bar-chart-line",
                default_index=0,
                orientation="horizontal"
            )

            if selected_visualization == "Matplotlib":    
               # List gambar
                images = ["1.png", "2.png", "3.png",]

                # Menampilkan gambar dalam 3 kolom dan 3 baris
                cols = st.columns(3)  # Membuat 3 kolom

                for idx, image in enumerate(images):
                    col = cols[idx % 3]  # Memilih kolom berdasarkan indeks
                    with col:
                        st.image(image, use_column_width=True)  # Menampilkan gambar di kolom
            
    
elif selected_nav == "Contact":
    # CSS untuk mendesain tampilan kontak
    st.markdown("""
        <style>
        .contact-card {
            background-color: #f8f9fa;
            padding: 20px;
            margin: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        }
        .contact-card img {
            width: 40px;
            height: 40px;
            margin: 5px;
        }
        .contact-card a {
            text-decoration: none;
            color: #007bff;
        }
        </style>
        """, unsafe_allow_html=True)

    # Menampilkan kartu kontak dengan logo dan link
    st.markdown("""
        <div class="contact-card">
            <h2>Contact Me</h2>
            <a href="https://wa.me/6291245941155" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp Logo">
            </a>
            <a href="https://www.linkedin.com/in/n-i-s-baldanullah-a666351b7/" target="_blank">
                <img src="data:image/png;base64,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" alt="LinkedIn Logo">
            </a>
            <a href="https://github.com/baldan555" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub Logo">
            </a>
            <a href="https://www.kaggle.com/nissbaldanullah" target="_blank">
                <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAYFBMVEX///8gvv8Au/8Auf/D6v8KvP+Y2v9v0f+b3P/6/v/l9//v+v/p+P/y+/+t5P+X3f+15v/I7f/P7//Z8v8rwf9Qyf+m4f+K2f84xP9jzv961P+76f/d9P8lwP9Ix/+P2v/HpRUKAAAFGElEQVR4nO2d61LjMAxGGxdTeqdt2i2Flvd/y51dLrMLiT/HUiyJ0fnNMD64FVEky5OJ4ziO4ziO84PZ3XeymUsvjIvtNHYSjj9F8dr0EA7SS2Ni2mt4J700JtzQPm5oHze0jxvaxw3t44b2cUP7uKF93NA+bmgfN7SPG9rHDe3jhvZxQ/u4oX3c0D5uaB83tI8b2scN7eOG9nFD+7ihfdzQPm5oHze0jxvaxw3t44b2cUP7uKF93HAoy9Nl1s9lx7z8DJgNH5vQfXL6nWn908W8hqfQ9+veib/YDRCshlsk2ATbhnAHm3hdjuCQhtEwQ7BdjOGQhs8wR3A1ikMaNsMMwfN6HIc0XIZqBbkMN1jwJiPIZJgjKDUrhcUQCwoOg+EwzBB8kpt2w2D4qFqQwTBDcDaqAoBsqF2QbPiMBS8jKwCIhvoFiYYZgvXTpS+QDC0IkgzvsOBrBQUAwfAuQsFtDQVAuWHGDmoQLDfcYcFTHQVAqeEOf0Q3lRQAhYYZgo+1FABlhlgwPldTABQZ7nHCq0awyHCPP6IC9Yk+CgyxYNzXVAAMN8SCjSbB4YYHvIO6ptcONcwQfKmsABhoeEB+zVWZ4EBDvIOtNsFhhi/IL14FikuAIYZwB2NbvzwIGWAIv4PxLFE9Q+Qb4o/oWeEODjBc9E5v/xTUOac+1/AFCmodxJ9puAB+ksUlQJ7hyq5gniH8DoYnOQNEjuGiBf8IhWsvaTIMV6YFMwyXtgWxId5B6eISABliQfnaSxpguDYvCAyXZ/OCacMVFFRRe0mTMsQ7qKP2kqbfcDdHglMLggnDzQ3toJLiEqDXEBK1FJcAxYZBT+0lTalhVFR7SVNqaORLOKF8SlWVXxKUR5qrxleHHRBi6U167XmUG2rPCz8gGNp4aCMZqirX90IybBp9paZv0AzlTlHkQ9xDA9GGaNiEB2kDBNVQ/5lvsqH6aEM31Fo3/IBhD6PissyExVD5GzcOQ93RJs8Q9pMqjjY5hvEG+zCueqNNhmE8rmFnvuJogw3D32dPNBBCw+mYbqBhOL794Ay9H9b6dhEZfj5az8/oJ9V1Jb4BDP/JHRYooLY6o03a8L8K9jP4ayiNNslVf6l/vpqMNinDb09jTyjaaCzWJAy/J7frNm2orov9D/2GXe8KDwajTX+FtPNlKBoQEY+1BSBDz1tcULRR15wx1HAOa9/aos3gU0FL1LCv7dmm4GQXjDa6GtoLTuehkVDKok3JCcuZqWhTYgjTjKmmIn/ROeAFjDaKivxlZ7nhyA+R6XrdFJ7HR2mGomhTOlMBphlqeqNLDWGaoSbaFE/+gGmGliPr5dNb8Bw6HdGGMIEHpRlKWoooU5SOJqINxRCnGRpaikizvmCaoaGliDavDU6eVXB6nThzD6UZCqIN0RBXM8RbiqiTIVcw2kgX+cnTPWGaIR1t6BNaUZoh/WzDMGUXpRmxHVMAwmA4h9UM21N2Jxlphmi0qTPPW7KliGcmO0ozmij3bMM0Vx+lGYJlNyZDmGbIFfm5bn/AaYZUtKl3g4dUSxHfLSyoaUqqyM9nCNOMRqZdmvGuIJhmyEQbzvuecJoh0VLEemcXTDMkog3vvWsozWhC/WcbXkOYZjRt9RuDmG8HxNWM6tGG2TAjzaj9lrh3QaUJD6xm1E6HeyexhdJpwEegeGZdP2Y77bxWM0yLy9TzWUjd1BkazuXnsH/ohNKddjjd93OSf8/vOI7jOI7jjMdvycdIrEsJUe8AAAAASUVORK5CYII=" alt="Kaggle Logo">
            </a>
            <a href="https://www.instagram.com/baldan555/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram Logo">
            </a>
        </div>
        """, unsafe_allow_html=True)

        # CSS untuk mendesain tampilan kontak
    st.markdown("""
        <style>
        .contact-card {
            background-color: #f8f9fa;
            padding: 20px;
            margin: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
        }
        .contact-card img {
            width: 40px;
            height: 40px;
            margin: 5px;
        }
        .contact-card a {
            text-decoration: none;
            color: #007bff;
        }
        </style>
        """, unsafe_allow_html=True)

    # Menampilkan kartu kontak dengan logo dan link
    st.markdown("""
        <div class="contact-card">
            <h2>Follow my Visualization Content</h2>
            <a href="https://www.instagram.com/letthedatatalk/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="WhatsApp Logo">
            
        </div>
        """, unsafe_allow_html=True)
