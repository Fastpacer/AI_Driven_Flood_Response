import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class FloodPredictor:
    def __init__(self, data_path='flood_training_data.csv'):
        self.model = RandomForestClassifier(n_estimators=100)
        
        # Check if the CSV file exists, generate it if not
        if not os.path.exists(data_path):
            print(f"{data_path} not found. Generating training data...")
            self._generate_training_data()
        
        # Load the training data
        self.training_data = pd.read_csv(data_path)
        self.train_model()
        
    def _generate_training_data(self):
        """Create realistic sample dataset (run once to generate CSV)"""
        import numpy as np
        np.random.seed(42)
        
        num_samples = 1000
        data = {
            'rainfall': np.random.uniform(0, 100, num_samples),
            'water_level': np.random.uniform(0.5, 5.0, num_samples),
            'tide': np.random.choice(['low', 'medium', 'high'], num_samples, p=[0.5, 0.3, 0.2]),
            'risk': ['low'] * num_samples
        }
        
        # Create realistic risk rules
        for i in range(num_samples):
            if data['rainfall'][i] > 50 and data['water_level'][i] > 2.5:
                data['risk'][i] = 'high'
            elif data['rainfall'][i] > 30 or data['water_level'][i] > 1.8:
                data['risk'][i] = 'medium'
        
        # Save to CSV
        pd.DataFrame(data).to_csv('flood_training_data.csv', index=False)
        print("Training data generated and saved to flood_training_data.csv")

    def train_model(self):
        # Convert categorical tide levels to numerical
        tide_mapping = {'low': 0, 'medium': 1, 'high': 2}
        self.training_data['tide_encoded'] = self.training_data['tide'].map(tide_mapping)
        
        # Select features and target
        X = self.training_data[['rainfall', 'water_level', 'tide_encoded']]
        y = self.training_data['risk']
        
        # Train-test split
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        self.model.fit(X_train, y_train)
        
        # Simple evaluation
        print(f"Model Accuracy: {self.model.score(X_test, y_test):.2f}")

    def predict_risk(self, real_time_data):
        tide_mapping = {'low': 0, 'medium': 1, 'high': 2}
        input_df = pd.DataFrame([{
            'rainfall': real_time_data['rainfall'],
            'water_level': real_time_data['water_level'],
            'tide_encoded': tide_mapping[real_time_data['tide_level']]
        }])
        
        return self.model.predict(input_df)[0]