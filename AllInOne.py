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
    st.title("CV")
    # Your CV content here...

elif selected_nav == "Portofolio":
    with st.expander("Pilih Kategori", expanded=True):
        selected_category = option_menu(
            "Kategori",
            ["Machine Learning", "Deep Learning", "Data Visualization", "Business Intelligence"],
            icons=["cpu", "brain", "bar-chart", "pie-chart"],
            menu_icon="list",
            default_index=0,
            orientation="horizontal"
        )

        if selected_category == "Machine Learning":
            selected_app = option_menu(
                "Pilih Aplikasi",
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
