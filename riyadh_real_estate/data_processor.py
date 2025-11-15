"""
Data Processing Module for Riyadh Real Estate
معالج البيانات العقارية للرياض

This module handles data loading, cleaning, and preprocessing for Riyadh real estate data.
"""

import pandas as pd
import numpy as np
from typing import Optional, Dict, List


class RiyadhRealEstateData:
    """
    A class for processing and managing Riyadh real estate data.
    
    فئة لمعالجة وإدارة بيانات العقارات في الرياض
    """
    
    def __init__(self):
        """Initialize the data processor."""
        self.data: Optional[pd.DataFrame] = None
        self.processed_data: Optional[pd.DataFrame] = None
        
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load real estate data from a CSV file.
        
        Args:
            file_path: Path to the CSV file containing real estate data
            
        Returns:
            DataFrame containing the loaded data
        """
        self.data = pd.read_csv(file_path)
        return self.data
    
    def create_sample_data(self, n_samples: int = 100) -> pd.DataFrame:
        """
        Create sample real estate data for testing and demonstration.
        
        Creates realistic sample data for Riyadh properties including:
        - Location (district/neighborhood)
        - Property type (apartment, villa, land)
        - Area in square meters
        - Number of bedrooms
        - Number of bathrooms
        - Age of property
        - Distance from city center
        - Price in SAR
        
        Args:
            n_samples: Number of sample records to generate
            
        Returns:
            DataFrame with sample real estate data
        """
        np.random.seed(42)
        
        # Riyadh districts (أحياء الرياض)
        districts = [
            'العليا', 'الملقا', 'النرجس', 'الياسمين', 'الربوة',
            'المروج', 'الملز', 'السليمانية', 'الورود', 'الغدير'
        ]
        
        property_types = ['شقة', 'فيلا', 'أرض']  # Apartment, Villa, Land
        
        data = {
            'الحي': np.random.choice(districts, n_samples),
            'نوع_العقار': np.random.choice(property_types, n_samples),
            'المساحة_متر_مربع': np.random.randint(100, 1000, n_samples),
            'عدد_الغرف': np.random.randint(1, 8, n_samples),
            'عدد_دورات_المياه': np.random.randint(1, 6, n_samples),
            'عمر_العقار_سنوات': np.random.randint(0, 30, n_samples),
            'المسافة_من_المركز_كم': np.random.uniform(1, 50, n_samples),
        }
        
        df = pd.DataFrame(data)
        
        # Generate realistic prices based on features
        base_price = 500000  # Base price in SAR
        
        # Price factors
        area_factor = df['المساحة_متر_مربع'] * 1500
        type_factor = df['نوع_العقار'].map({
            'شقة': 1.0,
            'فيلا': 1.5,
            'أرض': 0.8
        })
        room_factor = df['عدد_الغرف'] * 50000
        age_penalty = df['عمر_العقار_سنوات'] * -10000
        location_factor = (50 - df['المسافة_من_المركز_كم']) * 5000
        
        # Calculate price with some random variation
        df['السعر_ريال'] = (
            base_price +
            area_factor * type_factor +
            room_factor +
            age_penalty +
            location_factor +
            np.random.normal(0, 100000, n_samples)
        )
        
        # Ensure prices are positive
        df['السعر_ريال'] = df['السعر_ريال'].clip(lower=100000)
        
        self.data = df
        return df
    
    def clean_data(self) -> pd.DataFrame:
        """
        Clean and preprocess the real estate data.
        
        Returns:
            Cleaned DataFrame
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
        
        df = self.data.copy()
        
        # Remove duplicates
        df = df.drop_duplicates()
        
        # Handle missing values
        df = df.dropna()
        
        # Remove outliers (properties with unrealistic prices or sizes)
        if 'السعر_ريال' in df.columns:
            price_q1 = df['السعر_ريال'].quantile(0.01)
            price_q99 = df['السعر_ريال'].quantile(0.99)
            df = df[(df['السعر_ريال'] >= price_q1) & (df['السعر_ريال'] <= price_q99)]
        
        if 'المساحة_متر_مربع' in df.columns:
            area_q1 = df['المساحة_متر_مربع'].quantile(0.01)
            area_q99 = df['المساحة_متر_مربع'].quantile(0.99)
            df = df[(df['المساحة_متر_مربع'] >= area_q1) & (df['المساحة_متر_مربع'] <= area_q99)]
        
        self.processed_data = df
        return df
    
    def get_feature_matrix(self) -> tuple:
        """
        Prepare feature matrix and target variable for modeling.
        
        Returns:
            Tuple of (X, y) where X is feature matrix and y is target variable
        """
        if self.processed_data is None:
            self.clean_data()
        
        df = self.processed_data.copy()
        
        # Encode categorical variables
        df_encoded = pd.get_dummies(df, columns=['الحي', 'نوع_العقار'], drop_first=True)
        
        # Separate features and target
        y = df_encoded['السعر_ريال']
        X = df_encoded.drop('السعر_ريال', axis=1)
        
        return X, y
    
    def get_statistics(self) -> Dict:
        """
        Get descriptive statistics of the real estate data.
        
        Returns:
            Dictionary containing various statistics
        """
        if self.data is None:
            raise ValueError("No data loaded. Please load data first.")
        
        stats = {
            'عدد_العقارات': len(self.data),
            'متوسط_السعر': self.data['السعر_ريال'].mean() if 'السعر_ريال' in self.data.columns else None,
            'متوسط_المساحة': self.data['المساحة_متر_مربع'].mean() if 'المساحة_متر_مربع' in self.data.columns else None,
            'أعلى_سعر': self.data['السعر_ريال'].max() if 'السعر_ريال' in self.data.columns else None,
            'أدنى_سعر': self.data['السعر_ريال'].min() if 'السعر_ريال' in self.data.columns else None,
        }
        
        return stats
