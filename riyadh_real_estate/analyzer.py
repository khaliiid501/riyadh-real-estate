"""
Market Analysis Module for Riyadh Real Estate
وحدة تحليل السوق العقاري في الرياض

This module provides tools for analyzing the Riyadh real estate market.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Optional, Tuple


class MarketAnalyzer:
    """
    A class for analyzing the Riyadh real estate market.
    
    فئة لتحليل السوق العقاري في الرياض
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the market analyzer.
        
        Args:
            data: DataFrame containing real estate data
        """
        self.data = data
        
    def analyze_by_district(self) -> pd.DataFrame:
        """
        Analyze real estate market by district.
        
        Returns:
            DataFrame with statistics by district
        """
        if 'الحي' not in self.data.columns or 'السعر_ريال' not in self.data.columns:
            raise ValueError("Required columns not found in data.")
        
        district_analysis = self.data.groupby('الحي').agg({
            'السعر_ريال': ['count', 'mean', 'median', 'min', 'max', 'std'],
            'المساحة_متر_مربع': 'mean'
        }).round(2)
        
        district_analysis.columns = [
            'عدد_العقارات', 'متوسط_السعر', 'الوسيط_السعر',
            'أدنى_سعر', 'أعلى_سعر', 'الانحراف_المعياري', 'متوسط_المساحة'
        ]
        
        return district_analysis.sort_values('متوسط_السعر', ascending=False)
    
    def analyze_by_property_type(self) -> pd.DataFrame:
        """
        Analyze real estate market by property type.
        
        Returns:
            DataFrame with statistics by property type
        """
        if 'نوع_العقار' not in self.data.columns or 'السعر_ريال' not in self.data.columns:
            raise ValueError("Required columns not found in data.")
        
        type_analysis = self.data.groupby('نوع_العقار').agg({
            'السعر_ريال': ['count', 'mean', 'median', 'min', 'max'],
            'المساحة_متر_مربع': 'mean',
            'عدد_الغرف': 'mean'
        }).round(2)
        
        type_analysis.columns = [
            'عدد_العقارات', 'متوسط_السعر', 'الوسيط_السعر',
            'أدنى_سعر', 'أعلى_سعر', 'متوسط_المساحة', 'متوسط_عدد_الغرف'
        ]
        
        return type_analysis.sort_values('متوسط_السعر', ascending=False)
    
    def calculate_price_per_sqm(self) -> pd.DataFrame:
        """
        Calculate price per square meter for all properties.
        
        Returns:
            DataFrame with price per square meter analysis
        """
        if 'السعر_ريال' not in self.data.columns or 'المساحة_متر_مربع' not in self.data.columns:
            raise ValueError("Required columns not found in data.")
        
        df = self.data.copy()
        df['السعر_للمتر_المربع'] = df['السعر_ريال'] / df['المساحة_متر_مربع']
        
        return df
    
    def get_market_trends(self) -> Dict:
        """
        Get overall market trends and insights.
        
        Returns:
            Dictionary containing market trend insights
        """
        trends = {
            'إجمالي_العقارات': len(self.data),
            'متوسط_السعر_العام': self.data['السعر_ريال'].mean(),
            'متوسط_المساحة_العامة': self.data['المساحة_متر_مربع'].mean(),
            'أكثر_الأحياء_نشاطا': self.data['الحي'].value_counts().head(3).to_dict(),
            'توزيع_أنواع_العقارات': self.data['نوع_العقار'].value_counts().to_dict(),
        }
        
        if 'السعر_ريال' in self.data.columns and 'المساحة_متر_مربع' in self.data.columns:
            trends['متوسط_السعر_للمتر_المربع'] = (
                self.data['السعر_ريال'] / self.data['المساحة_متر_مربع']
            ).mean()
        
        return trends
    
    def find_best_value_properties(self, n: int = 10) -> pd.DataFrame:
        """
        Find properties with the best value (lowest price per square meter).
        
        Args:
            n: Number of properties to return
            
        Returns:
            DataFrame with best value properties
        """
        df = self.calculate_price_per_sqm()
        return df.nsmallest(n, 'السعر_للمتر_المربع')
    
    def compare_districts(self, districts: List[str]) -> pd.DataFrame:
        """
        Compare specific districts.
        
        Args:
            districts: List of district names to compare
            
        Returns:
            DataFrame with comparison statistics
        """
        df_filtered = self.data[self.data['الحي'].isin(districts)]
        
        comparison = df_filtered.groupby('الحي').agg({
            'السعر_ريال': ['mean', 'median', 'count'],
            'المساحة_متر_مربع': 'mean',
            'عدد_الغرف': 'mean'
        }).round(2)
        
        comparison.columns = [
            'متوسط_السعر', 'الوسيط_السعر', 'عدد_العقارات',
            'متوسط_المساحة', 'متوسط_عدد_الغرف'
        ]
        
        return comparison
    
    def plot_price_distribution(self, save_path: Optional[str] = None):
        """
        Plot the distribution of property prices.
        
        Args:
            save_path: Optional path to save the plot
        """
        plt.figure(figsize=(10, 6))
        plt.hist(self.data['السعر_ريال'], bins=30, edgecolor='black', alpha=0.7)
        plt.xlabel('السعر (ريال سعودي)', fontsize=12)
        plt.ylabel('عدد العقارات', fontsize=12)
        plt.title('توزيع أسعار العقارات في الرياض', fontsize=14)
        plt.grid(axis='y', alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        plt.close()
    
    def plot_price_by_district(self, save_path: Optional[str] = None):
        """
        Plot average prices by district.
        
        Args:
            save_path: Optional path to save the plot
        """
        district_avg = self.data.groupby('الحي')['السعر_ريال'].mean().sort_values(ascending=False)
        
        plt.figure(figsize=(12, 6))
        district_avg.plot(kind='bar', color='steelblue', edgecolor='black')
        plt.xlabel('الحي', fontsize=12)
        plt.ylabel('متوسط السعر (ريال سعودي)', fontsize=12)
        plt.title('متوسط أسعار العقارات حسب الحي', fontsize=14)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        plt.close()
    
    def plot_correlation_heatmap(self, save_path: Optional[str] = None):
        """
        Plot correlation heatmap of numerical features.
        
        Args:
            save_path: Optional path to save the plot
        """
        # Select numerical columns
        numerical_cols = self.data.select_dtypes(include=[np.number]).columns
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(
            self.data[numerical_cols].corr(),
            annot=True,
            fmt='.2f',
            cmap='coolwarm',
            center=0,
            square=True,
            linewidths=1
        )
        plt.title('مصفوفة الارتباط بين المتغيرات', fontsize=14)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        plt.close()
