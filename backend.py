import streamlit as st
from google.cloud import storage
from google.oauth2 import service_account
from datetime import timedelta

@st.cache_resource
def init_gcs_client():
    try:
        secrets = st.secrets["gcp_service_account"]
        credentials = service_account.Credentials.from_service_account_info(secrets)
        return storage.Client(credentials=credentials)
    except Exception as e:
        st.error(f"Failed to initialize GCS client: {str(e)}")
        return None

# Initialize client
client = init_gcs_client()
bucket_name = "docx-27"

@st.cache_data(ttl=1800)  # cache for 30 minutes (1800 seconds)
def generate_signed_url(blob_name, expiration_minutes=30):
    """Generate a signed URL for temporary access to a GCS object"""
    client = init_gcs_client()
    if not client:
        st.error("GCS client not initialized")
        return None

    try:
        bucket = client.bucket("docx-27")
        blob = bucket.blob(blob_name)

        if not blob.exists():
            st.error(f"File {blob_name} not found in GCS")
            return None

        url = blob.generate_signed_url(
            version="v4",
            expiration=timedelta(minutes=expiration_minutes),
            method="GET"
        )
        return url
    except Exception as e:
        st.error(f"Error generating signed URL: {str(e)}")
        return None
