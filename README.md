# 🏠 Indian House Price Predictor

A Streamlit web app that predicts house prices in India using a pre-trained Random Forest model.
Users provide key features like city, BHK, carpet area, furnishing, and property age.
The app delivers instant price estimates with a sleek, interactive interface.

---
#### 🌐 Live Demo

  [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://indian-house-price-predictor.streamlit.app/)


## 🌟Features
- Predicts house prices using a pre-trained **Random Forest Regression model**.  
- Sleek, interactive UI built with **Streamlit**.  
- Inputs include: City, Property Type, Building Type, BHK, Bathrooms, Balconies, Carpet Area, Floor, Furnishing, Facing, Age of Property.  
- Instant predictions with prices formatted in Indian notation.  

---

## How to Use
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/weather-app.git
   ```  
2. Navigate to the project directory:  
   ```bash
   cd indian-house-price-predictor
   ```  
3. Create and activate a virtual environment:  
   ```bash
   python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Mac/Linux
    source .venv/bin/activate
   ```  
4. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
5. Run the app: 
   ```bash
   streamlit run app.py
   ``` 
6. The app will open in your browser.

## 🛠️Technologies Used
- Python 3.10: Core programming language.
- Streamlit: For interactive frontend.
- Pandas: For data handling.
- Scikit-learn: For training and predicting with Random Forest.
- Pickle / Joblib: For model serialization.
---
## Contributing

- Contributions are welcome! Feel free to open issues or submit pull requests to improve the app, add more cities, or enhance the UI.
