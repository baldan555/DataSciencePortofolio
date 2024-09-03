import streamlit as st
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
import faceemotionApp
import sentimentApp
import f1detectApp
import HandGestureRecog

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Kumpulan Aplikasi Streamlit", layout="wide")

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
    st.title("About Me")
    st.write("Deskripsi tentang Anda di sini.")
    
elif selected_nav == "CV":
     # Profile Section with tighter spacing
    st.markdown("""
    # <div style='text-align: center; margin-bottom: -15px;'>N.I.S. BALDANULLAH</div>
    ### <div style='text-align: center; margin-bottom: -10px;'>Data Enthusiast</div> 
    <div style='text-align: center; margin-bottom: -10px;'>Jakarta, Indonesia</div>  
    <div style='text-align: center;'>+6281245941155 | baldanullah55@gmail.com</div>
    """, unsafe_allow_html=True)

    # Add some spacing before the next section
    st.write(" ")

    # Profile Text
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>PROFILE</div>
    <hr style="border:2px solid black; margin-top: -40px;">
    <p style='text-align: justify;'>
    I am an enthusiastic fan of technology in the field of data science, studying informatics engineering at Pancasila University. 
    The vast potential in data science has attracted my interest, especially its accurate ability to solve various problems in our society. 
    So far, by utilizing the knowledge from the campus and by self-learning using various free resources and content I have been able to gain practical experience and apply the knowledge I have, with my abilities, talents, and enthusiasm. 
    I believe that I am suitable to participate together we can drive meaningful progress both within the organization and in society at large.
    </p>
    """, unsafe_allow_html=True)

    # Add some spacing
    st.write(" ")

    # Experience Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>EXPERIENCE</div>
    <hr style="border:2px solid black; margin-top: -40px;;">

    #### **Big Data Analyst**  
    _Aug 2023 — Dec 2023 | Makassar_  
    - Managing large scale data such as cleansing, storing, and pre-processing data  
    - Building Machine Learning models such as LSTM (Long Short Term Memory), GRU, Convolutional Neural Network for Predicting Asia Bitumen Price  
    - Build and deploy machine learning model to predict and visualize an Asia Bitumen price into an interactive web app dashboard

    <br>

    #### **Website Administrator, Editor and Publisher at PT. INIPASTI Communika**  
    _Jan 2020 — Dec 2022 | Makassar_  
    - Editing journalists' news narratives  
    - Rewriting news articles from journalists for publication on the company’s online media platform and overseeing the company’s media website  
    - Monitoring website traffic  
    - Keeping track of and managing the number of visitors to the website  
    - Analyzing data insights  
    - Examining and interpreting data to gain valuable insights

    <br>

    #### **Data Entry Assistant at Institute Social and Political Economic Issue (ISPEI)**  
    _Jan 2014 — Dec 2016 | Makassar_  
    - Developed and maintained data entry guidelines and processes to ensure accuracy and consistency  
    - Input data from paper sheets into excel and cleaning and managing data
    """, unsafe_allow_html=True)

    # Add some spacing
    st.write(" ")

    # Education Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>EDUCATION</div>
    <hr style="border:2px solid black; margin-top: -40px;">

    #### **Pancasila University**  
    _Bachelor_  
    _Mar 2020 — Aug 2024 | South Jakarta_
    """, unsafe_allow_html=True)

    # Add some spacing
    st.write(" ")

    # Project Section
    st.markdown("""
    ## <div style='text-align: center; background-color: #f0f0f0; padding: 5px;'>PROJECTS</div>
    <hr style="border:2px solid black; margin-top: -40px;">

    #### **Capstone Project**  
    _Jun 2023 — Jun 2023 | Bangkit Academy_  
    Building Machine Learning models to detect vehicle tire quality in vehicle service online booking applications with image processing using CNN (Convolutional Neural Network)

    <br>

    #### **Interactive Predictive FOB Bitumen Price Dashboard**  
    _Sep 2024 — Nov 2023 | Kalla Group_  
    Build and deploy machine learning model to predict and visualize an Asia bitumen price into an interactive web app dashboard
    """, unsafe_allow_html=True)

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

        elif selected_category == "Data Visualization":
            st.write("Belum ada aplikasi di kategori ini.")
        
        elif selected_category == "Business Intelligence":
            st.write("Belum ada aplikasi di kategori ini.")
    
  

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
    elif selected_app == "Draw MNIST Number":
        MNIST_st.main()
    elif selected_app == "Face Mood Detect":
        faceemotionApp.main()
    elif selected_app == "Stock Forecasting":
        stockapp.main()
    elif selected_app == "Sentiment Analysis":
        sentimentApp.main()
    elif selected_app == "YOLOV8 Object Detection":
        f1detectApp.main()
    elif selected_app == "Hand Gesture Recognition":
        HandGestureRecog.main()

elif selected_nav == "Contact":
    st.title("Contact")
    st.write("Informasi kontak Anda di sini.")
