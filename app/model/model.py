import pickle
from pathlib import Path

__version__ = "0.0"

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
    
def predict_pipeline(text):
    prediction_result = resume_prediction_model.predict([text])
    predicted_label = labels[prediction_result[0]]
    return predicted_label

# def predict_pipeline(text):
#     preprocessed_input_text = [text]
#     pred = model.predict(preprocessed_input_text)
#     return pred[0]

