# fastapi capstone project
# 🚗 Car Price Predictor – Machine Learning & Deployment Project

A full-stack Machine Learning project that predicts the price of a car based on its specifications using a **Random Forest Regressor** model. The project is built using **FastAPI** and deployed on **Render**, with **Docker** for containerization and **Prometheus + Grafana** for monitoring and performance tracking.

---

## 📊 Project Overview

The goal of this project is to build and deploy a **supervised ML model** that estimates car prices based on features such as brand, year, fuel type, transmission, and mileage.  
The application provides a simple web API where users can input car details and get instant price predictions.

---

## 🧠 Tech Stack

- **Python** – Model development & preprocessing  
- **Jupyter Notebook** – Data analysis & feature engineering  
- **Random Forest Regressor** – Supervised ML algorithm for prediction  
- **FastAPI** – Lightweight backend for API serving  
- **Docker** – Containerization for consistent deployment  
- **Redis** – Caching to optimize API performance  
- **Prometheus & Grafana** – Metrics collection and visualization for monitoring  
- **Render** – Cloud platform for deployment

---

## ⚙️ Features

- Preprocessed raw car dataset for model training  
- Implemented **Random Forest Regressor** with hyperparameter tuning  
- Built a REST API using **FastAPI** for serving predictions  
- **Containerized** application using Docker for portability  
- Integrated **Prometheus + Grafana** dashboard for real-time system monitoring  
- Deployed full solution on **Render** with automatic builds from GitHub

---

## 🚀 Deployment

Live Demo: [https://your-app-url.onrender.com](https://your-app-url.onrender.com)

To run locally:
```bash
# Clone the repository
git clone https://github.com/yourusername/car-price-predictor.git
cd car-price-predictor

# Build Docker image
docker build -t car-price-predictor .

# Run container
docker run -p 8000:8000 car-price-predictor
