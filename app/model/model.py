import pickle
from pathlib import Path
import re

__version__ = "0.2"

BASE_DIR = Path(__file__).resolve(strict=True).parent

labels = [
    "Advocate",
    "Arts",
    "Automation Testing",
    "Blockchain",
    "Business Analyst",
    "Civil Engineer",
    "Data Science",
    "Database",
    "DevOps Engineer",
    "DotNet Developer",
    "ETL Developer",
    "Electrical Engineering",
    "HR",
    "Hadoop",
    "Health and fitness",
    "Java Developer",
    "Mechanical Engineer",
    "Network Security Engineer",
    "Operations Manager",
    "PMO",
    "Python Developer",
    "SAP Developer",
    "Sales",
    "Testing",
    "Web Designing"
]


with open(f"{BASE_DIR}/resume_pipeline_{__version__}.pkl", "rb") as f:
    resume_prediction_model = pickle.load(f)


def preprocess_text(raw_resume):
    resume_processed = ' '.join(re.findall('[a-zA-Z0-9]+', raw_resume)).lower()   
    return resume_processed 
        
    
def predict_pipeline(text):
    prediction_result = resume_prediction_model.predict([text])
    predicted_label = labels[prediction_result[0]]
    return predicted_label

