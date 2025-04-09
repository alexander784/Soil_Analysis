# Soil Analysis Web Application

This is a Django-based web application for analyzing soil data, predicting soil quality, and providing AI-driven crop suggestions. It features a user-friendly interface with a file upload system, interactive visualizations, and a chatbot powered by a reinforcement learning (RL) agent. 

## Features

- **Soil Quality Prediction:** Uses a Random Forest Classifier to predict soil grade (0-2) based on nutrient levels (N, P, K, pH, moisture) from uploaded CSV files.
- **Interactive Visualizations:** Displays nutrient levels as bar charts using Plotly.
- **AI Suggestions:** Provides initial rule-based suggestions and adaptive crop recommendations via a Q-learning RL agent.
- **Chatbot:** A popup chatbot on the right side, offering real-time assistance for soil and crop queries.
- **File Upload:** Allows users to upload CSV files for analysis, with results displayed on a dedicated page.

## Prerequisites

- **Python:** 3.10.12
- **Django:** 5.0.4
- **pandas:**
- **numpy:**
- **scikit-learn**
- **matplotlib:**
- **plotly:**

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd soil_analysis

2. **Set Up a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Apply Migrations:**
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate

5. **Run dev server:**
    ```bash
    python3 manage.py runserver


## Usage
1. **Upload soil Data:**
* Visit the homepage (/) to access the upload page.
* Upload a CSV file with columns: N, P, K, pH, moisture.
* Example CSV format:
  ```bash
  N,P,K,pH,moisture
  75,45,120,6.5,50

2. **View Results**
* After uploading, you’ll be redirected to the results page showing:
  * Soil grade
  * A bar chart of nutrient levels.
  * AI suggestions (rule-based and RL-agent-driven).

3. **Interact with the Chatbot**

 * A popup chatbot appears on the right side.
 * Ask questions like "nitrogen" or "crop" to get responses based on the latest analysis.

4. **Analyze Another Sample**
   * Click "Analyze Another Sample" to return to the upload page.

## Technical Details

**Soil Prediction**
* Uses `RandomForestClassifier` from `scikit-learn` with synthetic labels based on nutrient thresholds.
* Trained on-the-fly with each upload (no pre-trained model).

**RL Agent**
* Implements Q-learning in utils.py (SoilAgent class).
* States: Soil grade and nitrogen range.
* Actions: Crop recommendations (e.g., wheat, corn).


## Future improvements
* Add CSV input validation and error messages.
* Implement real user feedback for the RL agent.
* Enhance chatbot with NLP (e.g., integrate a model like BERT).


## Contributing
<p>Feel free to fork this repository, submit issues, or create pull requests. Contributions are welcome!</p>











