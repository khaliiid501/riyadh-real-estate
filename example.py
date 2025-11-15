"""
Example usage of Riyadh Real Estate Analytics Platform
مثال على استخدام منصة تحليل العقارات في الرياض
"""

from riyadh_real_estate import RiyadhRealEstateData, PricePredictor, MarketAnalyzer
import pandas as pd

def main():
    print("=" * 70)
    print("منصة تحليل العقارات في الرياض")
    print("Riyadh Real Estate Analytics Platform")
    print("=" * 70)
    print()
    
    # Step 1: Create and process data
    print("الخطوة 1: إنشاء ومعالجة البيانات | Step 1: Create and process data")
    print("-" * 70)
    processor = RiyadhRealEstateData()
    df = processor.create_sample_data(n_samples=500)
    print(f"✓ تم إنشاء {len(df)} عقار")
    print(f"✓ Created {len(df)} properties")
    print()
    
    # Show sample data
    print("عينة من البيانات | Sample Data:")
    print(df.head(3).to_string())
    print()
    
    # Step 2: Get statistics
    print("الخطوة 2: الإحصائيات | Step 2: Statistics")
    print("-" * 70)
    stats = processor.get_statistics()
    print(f"متوسط السعر | Average Price: {stats['متوسط_السعر']:,.2f} SAR")
    print(f"متوسط المساحة | Average Area: {stats['متوسط_المساحة']:.2f} sqm")
    print(f"أعلى سعر | Highest Price: {stats['أعلى_سعر']:,.2f} SAR")
    print(f"أدنى سعر | Lowest Price: {stats['أدنى_سعر']:,.2f} SAR")
    print()
    
    # Step 3: Market analysis
    print("الخطوة 3: تحليل السوق | Step 3: Market Analysis")
    print("-" * 70)
    analyzer = MarketAnalyzer(df)
    
    # District analysis
    print("\nتحليل الأحياء | District Analysis:")
    district_analysis = analyzer.analyze_by_district()
    print(district_analysis.head(5).to_string())
    print()
    
    # Property type analysis
    print("تحليل أنواع العقارات | Property Type Analysis:")
    type_analysis = analyzer.analyze_by_property_type()
    print(type_analysis.to_string())
    print()
    
    # Market trends
    print("اتجاهات السوق | Market Trends:")
    trends = analyzer.get_market_trends()
    for key, value in trends.items():
        if isinstance(value, dict):
            print(f"\n{key}:")
            for k, v in value.items():
                print(f"  - {k}: {v}")
        elif isinstance(value, float):
            print(f"{key}: {value:,.2f}")
        else:
            print(f"{key}: {value}")
    print()
    
    # Step 4: Build prediction model
    print("الخطوة 4: بناء نموذج التنبؤ | Step 4: Build Prediction Model")
    print("-" * 70)
    cleaned_data = processor.clean_data()
    X, y = processor.get_feature_matrix()
    
    predictor = PricePredictor(model_type='random_forest')
    print("جاري تدريب النموذج... | Training model...")
    metrics = predictor.train(X, y, test_size=0.2)
    
    print(f"\n✓ تم تدريب النموذج بنجاح | Model trained successfully")
    print(f"  - R² Score: {metrics['test_r2']:.4f}")
    print(f"  - Mean Absolute Error: {metrics['test_mae']:,.2f} SAR")
    print(f"  - Root Mean Squared Error: {metrics['test_rmse']:,.2f} SAR")
    print()
    
    # Feature importance
    print("أهمية الميزات | Feature Importance:")
    importance = predictor.get_feature_importance()
    print(importance.head(10).to_string())
    print()
    
    # Step 5: Make predictions
    print("الخطوة 5: التنبؤ بالأسعار | Step 5: Price Predictions")
    print("-" * 70)
    
    # Predict for first 5 properties
    sample_properties = X.head(5)
    predictions = predictor.predict(sample_properties)
    actual_prices = y.head(5).values
    
    print("مقارنة الأسعار الفعلية والمتوقعة | Actual vs Predicted Prices:")
    comparison_df = pd.DataFrame({
        'السعر الفعلي | Actual': actual_prices,
        'السعر المتوقع | Predicted': predictions,
        'الفرق | Difference': actual_prices - predictions,
        'الدقة % | Accuracy %': (100 - abs((actual_prices - predictions) / actual_prices * 100))
    })
    print(comparison_df.to_string(float_format=lambda x: f'{x:,.2f}'))
    print()
    
    # Step 6: Find best value properties
    print("الخطوة 6: أفضل العقارات قيمة | Step 6: Best Value Properties")
    print("-" * 70)
    best_value = analyzer.find_best_value_properties(n=5)
    print("أفضل 5 عقارات من حيث السعر للمتر المربع:")
    print("Top 5 Best Value Properties (Price per SQM):")
    print(best_value[['الحي', 'نوع_العقار', 'المساحة_متر_مربع', 
                      'السعر_ريال', 'السعر_للمتر_المربع']].to_string())
    print()
    
    # Summary
    print("=" * 70)
    print("✓ تم إكمال التحليل بنجاح!")
    print("✓ Analysis completed successfully!")
    print("=" * 70)
    print()
    print("للاستخدام التفاعلي، استخدم: jupyter notebook notebooks/demo.ipynb")
    print("For interactive usage, use: jupyter notebook notebooks/demo.ipynb")

if __name__ == "__main__":
    main()
