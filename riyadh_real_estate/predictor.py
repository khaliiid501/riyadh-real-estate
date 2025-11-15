"""
Price Prediction Module for Riyadh Real Estate
وحدة التنبؤ بالأسعار العقارية في الرياض

This module implements machine learning models to predict real estate prices in Riyadh.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from typing import Dict, Tuple, Optional
import joblib


class PricePredictor:
    """
    A class for predicting real estate prices in Riyadh using machine learning.
    
    فئة للتنبؤ بأسعار العقارات في الرياض باستخدام التعلم الآلي
    """
    
    def __init__(self, model_type: str = 'random_forest'):
        """
        Initialize the price predictor.
        
        Args:
            model_type: Type of model to use ('random_forest', 'gradient_boosting', 'linear')
        """
        self.model_type = model_type
        self.model = self._initialize_model()
        self.is_trained = False
        self.feature_names = None
        
    def _initialize_model(self):
        """Initialize the prediction model based on type."""
        if self.model_type == 'random_forest':
            return RandomForestRegressor(
                n_estimators=100,
                max_depth=20,
                min_samples_split=5,
                min_samples_leaf=2,
                random_state=42
            )
        elif self.model_type == 'gradient_boosting':
            return GradientBoostingRegressor(
                n_estimators=100,
                max_depth=5,
                learning_rate=0.1,
                random_state=42
            )
        elif self.model_type == 'linear':
            return LinearRegression()
        else:
            raise ValueError(f"Unknown model type: {self.model_type}")
    
    def train(self, X: pd.DataFrame, y: pd.Series, test_size: float = 0.2) -> Dict:
        """
        Train the prediction model.
        
        Args:
            X: Feature matrix
            y: Target variable (prices)
            test_size: Proportion of data to use for testing
            
        Returns:
            Dictionary containing training metrics
        """
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        
        # Store feature names
        self.feature_names = X.columns.tolist()
        
        # Train model
        self.model.fit(X_train, y_train)
        self.is_trained = True
        
        # Evaluate model
        train_predictions = self.model.predict(X_train)
        test_predictions = self.model.predict(X_test)
        
        metrics = {
            'train_mae': mean_absolute_error(y_train, train_predictions),
            'train_rmse': np.sqrt(mean_squared_error(y_train, train_predictions)),
            'train_r2': r2_score(y_train, train_predictions),
            'test_mae': mean_absolute_error(y_test, test_predictions),
            'test_rmse': np.sqrt(mean_squared_error(y_test, test_predictions)),
            'test_r2': r2_score(y_test, test_predictions),
        }
        
        return metrics
    
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """
        Predict prices for given properties.
        
        Args:
            X: Feature matrix for properties
            
        Returns:
            Array of predicted prices
        """
        if not self.is_trained:
            raise ValueError("Model not trained. Please train the model first.")
        
        return self.model.predict(X)
    
    def predict_single(self, property_features: Dict) -> float:
        """
        Predict price for a single property.
        
        Args:
            property_features: Dictionary of property features
            
        Returns:
            Predicted price
        """
        if not self.is_trained:
            raise ValueError("Model not trained. Please train the model first.")
        
        # Create DataFrame with single row
        df = pd.DataFrame([property_features])
        
        # Ensure all expected features are present
        for feature in self.feature_names:
            if feature not in df.columns:
                df[feature] = 0
        
        # Reorder columns to match training data
        df = df[self.feature_names]
        
        prediction = self.model.predict(df)
        return float(prediction[0])
    
    def get_feature_importance(self) -> pd.DataFrame:
        """
        Get feature importance scores.
        
        Returns:
            DataFrame with features and their importance scores
        """
        if not self.is_trained:
            raise ValueError("Model not trained. Please train the model first.")
        
        if hasattr(self.model, 'feature_importances_'):
            importance_df = pd.DataFrame({
                'feature': self.feature_names,
                'importance': self.model.feature_importances_
            })
            return importance_df.sort_values('importance', ascending=False)
        else:
            raise ValueError("Model does not support feature importance.")
    
    def save_model(self, file_path: str):
        """
        Save the trained model to a file.
        
        Args:
            file_path: Path to save the model
        """
        if not self.is_trained:
            raise ValueError("Model not trained. Cannot save untrained model.")
        
        model_data = {
            'model': self.model,
            'model_type': self.model_type,
            'feature_names': self.feature_names,
            'is_trained': self.is_trained
        }
        joblib.dump(model_data, file_path)
    
    def load_model(self, file_path: str):
        """
        Load a trained model from a file.
        
        Args:
            file_path: Path to the saved model
        """
        model_data = joblib.load(file_path)
        self.model = model_data['model']
        self.model_type = model_data['model_type']
        self.feature_names = model_data['feature_names']
        self.is_trained = model_data['is_trained']
