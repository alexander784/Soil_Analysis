import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go

def analyze_soil_data(csv_file):
    df = pd.read_csv(csv_file)

    
    required_columns = ['N', 'P', 'K', 'pH', 'moisture']
    
    X = df[required_columns]
    
    conditions = [
        (df['N'] > 80) & (df['P'] > 50) & (df['K'] > 150) & (df['pH'].between(6, 7)),
        (df['N'] > 50) & (df['P'] > 30) & (df['K'] > 100),
        (df['N'] <= 50) | (df['P'] <= 30) | (df['K'] <= 100)
    ]
    choices = [2, 1, 0]
    y = np.select(conditions, choices, default=0)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    prediction = rf_model.predict(X)[0]
    
    fig = go.Figure()
    for column in required_columns:
        fig.add_trace(go.Bar(
            x=[column],
            y=[df[column].mean()],
            name=column
        ))
    
    fig.update_layout(
        title='Soil Nutrient Levels',
        xaxis_title='Nutrients',
        yaxis_title='Level'
    )
    
    graph_html = fig.to_html(full_html=False)
    
    return prediction, graph_html, df.mean().to_dict()

def get_ai_suggestions(grade, nutrient_levels):
    suggestions = []
    
    if grade == 0:
        suggestions.append("Soil quality is poor. Consider the following improvements:")
        if nutrient_levels['N'] < 50:
            suggestions.append("- Add nitrogen-rich fertilizer (e.g., urea)")
        if nutrient_levels['P'] < 30:
            suggestions.append("- Apply phosphorus fertilizer (e.g., superphosphate)")
        if nutrient_levels['K'] < 100:
            suggestions.append("- Use potassium-rich fertilizer (e.g., potash)")
        suggestions.append("Recommended crops: Hardy plants like rye or clover")
    
    elif grade == 1:
        suggestions.append("Soil quality is moderate. For improvement:")
        if nutrient_levels['N'] < 80:
            suggestions.append("- Supplement with nitrogen fertilizer")
        suggestions.append("Recommended crops: Wheat, barley, or soybeans")
    
    else:
        suggestions.append("Soil quality is excellent!")
        suggestions.append("Recommended crops: Corn, rice, or vegetables")
    
    return suggestions