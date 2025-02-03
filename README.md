Public API - Flask with CORS Support

🚀 A simple public API built with Flask, handling CORS, and in JSON format.
python: https://hng.tech/hire/python-developers

📌 Features:
✅ RESTful API with JSON response
✅ Handles Cross-Origin Resource Sharing (CORS)
✅

📂 Project Structure:
/public-api
│── app.py # Main Flask application
│── requirements.txt # Dependencies
│── README.md # Project documentation

🛠 Technologies Used:
Backend: Flask (Python), Flask-CORS
Deployment: Gunicorn, Render

🚀 API Endpoints:
GET /api/public

📤 Response Example:
json
{
"email": "marcelinusilonuba21@gmail.com",
"current_time": "2025-01-30T12:34:56Z",
"github_repo": "https://github.com/Meskana/HNG12-task0.git"
}

Please follow this steps to start the project locally

1. Activate the Virtual Environment:
   source env/bin/activate
2. Install Required Packages:
   Make sure the requirements.txt file is in the project directory and run:
   pip install -r requirements.txt
3. run python app.py
4. http://127.0.0.1:5000/api/public
