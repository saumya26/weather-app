## 🌤 Weather App 🌤

A full-stack weather app built with React (frontend) and Django REST Framework (backend). It fetches live weather data and displays a dynamic UI based on temperature.

## 🚀 Features

✅ Live Weather Data Fetching (Django API)
✅ Dynamic Background Color (Hot, Warm, Cold)
✅ Responsive UI with React & Bootstrap
✅ RESTful API built using Django REST Framework
✅ Full-stack project with separate frontend and backend

## 📦 Installation & Setup

## 1⃣ Clone the Repository

git clone https://github.com/YOUR_USERNAME/weather-app.git
cd weather-app

##  2⃣ Backend Setup (Django REST Framework)

### Navigate to the backend folder

cd backend

### Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

### Install dependencies

pip install -r requirements.txt

### Run migrations

python manage.py migrate

### Start the Django server

python manage.py runserver

### Your Django API will be available at http://127.0.0.1:8000/api/weather/

## 3⃣ Frontend Setup (React)

### Navigate to the frontend folder

cd ../frontend

### Install dependencies

npm install

### Start the React app

npm start

### Your frontend will run at http://localhost:3000/

## 🔗 API Endpoints

| Method | Endpoint                   | Description                  |
|--------|----------------------------|------------------------------|
| GET    | `/api/weather/?city=London` | Get weather for a city       |

