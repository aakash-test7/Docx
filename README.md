# 🧠 Docx PDF Summarizer (TECHWILL x DOCX)

![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Railway](https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
                
**Docx** is an intelligent PDF summarization tool powered by Google's Gemini API and built with Streamlit. It extracts, analyzes, and simplifies PDF content, making it ideal for researchers, students, lawyers, and professionals dealing with complex documents.

🔗 **Live Demo:** [TechWill x Docx](https://aakash-docx.streamlit.app/)  

[![Demo Video](demo.png)](https://youtu.be/SUPVPZ3oqxI)

---

## ✨ Features

* **PDF Summarization**: Extracts and processes text using `pdfplumber`, generating contextual summaries via the Gemini API.
* **Interactive Visualizations**: Presents word frequency charts and visual highlights for better insight.
* **Cloud Integration**: Upload and process documents through the Streamlit interface, with summaries stored and accessed via Google Cloud Storage.
* **FAQ & Insight Engine**: Engage in conversational Q\&A about document content, referencing sources directly from the document.
* **Responsive UI**: Clean, mobile-friendly interface built entirely with Streamlit for ease of use.

---

## 🗂️ Project Structure

```
Docx/
├── .streamlit/                  # Streamlit configuration and secrets
│   ├── config.toml              # Theme and UI settings
│   └── secrets.toml             # GCP credentials for cloud access
│
├── Pages/                        # Multi-page Streamlit app views
│   ├── 1_🏠_Home.py              # Home page with main interface
│   ├── 2_🧠Logic.py              # Main summary tool 
│   ├── 3_📜_Wizard.py            # Step-by-step summarization wizard
│   ├── 3_🧪_Source_Code.py       # Displays full app source code
│   └── 4_🎓_Tutorial.py          # Video tutorial and how-to page
│
├── app.py                       # Main Streamlit app entry point
├── backend.py                   # Handles GCS operations and Gemini API interactions
├── requirements.txt             # Python dependencies
├── demo.png                     # Screenshot of the application
├── logo.gif                     # Application logo
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.7 or higher
* Google Cloud account with a service account key
* Gemini API access

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/aakash-test7/Docx.git
   cd Docx
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure GCP Credentials**:

   Create a `.streamlit/secrets.toml` file with your GCP service account credentials:

  ```toml
  [gcp_service_account]
  type = "service_account"
  project_id = "your-project-id"
  private_key_id = "your-private-key-id"
  private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
  client_email = "your-service-account-email"
  client_id = "your-client-id"
  auth_uri = "https://accounts.google.com/o/oauth2/auth"
  token_uri = "https://oauth2.googleapis.com/token"
  auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
  client_x509_cert_url = "your-cert-url"
  
  [mysql]
  host = "hostname"
  user = "root"
  password = ""
  port = 27
  
  [gemini_api_key]
  GEMINI_API_KEY = ""
  ```

   > Ensure this file is added to `.gitignore` to prevent sensitive information from being committed.

5. **Run the application**:

   ```bash
   streamlit run app.py
   ```

---

## 📚 Use Cases

* Summarizing academic papers
* Analyzing legal contracts
* Simplifying product manuals
* Distilling business reports
* Compressing educational content

---

## 🔧 Configuration

Customize the app's appearance by modifying `.streamlit/config.toml`:

```toml
[theme]
base = "light"
primaryColor = "#ef3415"
backgroundColor = "#000000"
secondaryBackgroundColor = "#6c7b7b"
textColor = "#FFFFFF"
font = "serif"
```

---

## 🔭 Future Enhancements

* [x] **Multi-Language Summarization**: Auto-translate output summaries.
* [x] **Drag & Drop PDF Upload**: Enhance user experience.
* [x] **Chat Mode**: Interact with documents conversationally.
* [ ] **User Authentication**: Optional login for saving history. ( under testing, update soon )
* [ ] **History Log**: View previous summaries. ( total count with timestamp is saved )
* [ ] **Summary Tone Customization**: Choose between technical, casual, or bullet-point summaries.
* [ ] **Topic Graphs**: Visualize major topics within documents.
* [ ] **LLM Switcher**: Toggle between Gemini, GPT-4, Claude, etc.
* [ ] **Deployment Options**: Containerize and deploy, ( currently using Streamlit Cloud )

---

## 🧑‍💻 Author

**Aakash Kharb**

* GitHub: [aakash-test7](https://github.com/aakash-test7)

---

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and enhancements are welcome!

---
