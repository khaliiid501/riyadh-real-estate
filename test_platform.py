"""
Simple test script to verify the Riyadh Real Estate Analytics Platform
اختبار بسيط للتحقق من منصة تحليل العقارات في الرياض
"""

import sys
sys.path.insert(0, '.')

from riyadh_real_estate import RiyadhRealEstateData, PricePredictor, MarketAnalyzer

def test_data_processing():
    """Test data processing functionality"""
    print("Testing Data Processing Module...")
    processor = RiyadhRealEstateData()
    df = processor.create_sample_data(n_samples=100)
    
    assert len(df) == 100, "Failed to create sample data"
    assert 'السعر_ريال' in df.columns, "Price column missing"
    
    stats = processor.get_statistics()
    assert stats['عدد_العقارات'] == 100, "Statistics calculation failed"
    
    print("✓ Data Processing Module: OK")

def test_market_analysis():
    """Test market analysis functionality"""
    print("Testing Market Analysis Module...")
    processor = RiyadhRealEstateData()
    df = processor.create_sample_data(n_samples=100)
    
    analyzer = MarketAnalyzer(df)
    trends = analyzer.get_market_trends()
    
    assert 'إجمالي_العقارات' in trends, "Trends calculation failed"
    assert trends['إجمالي_العقارات'] == 100, "Property count mismatch"
    
    district_analysis = analyzer.analyze_by_district()
    assert len(district_analysis) > 0, "District analysis failed"
    
    print("✓ Market Analysis Module: OK")

def test_price_prediction():
    """Test price prediction functionality"""
    print("Testing Price Prediction Module...")
    processor = RiyadhRealEstateData()
    processor.create_sample_data(n_samples=200)
    processor.clean_data()
    X, y = processor.get_feature_matrix()
    
    predictor = PricePredictor(model_type='random_forest')
    metrics = predictor.train(X, y, test_size=0.2)
    
    assert 'test_r2' in metrics, "Training metrics missing"
    assert metrics['test_r2'] > 0, "Model R² score should be positive"
    
    predictions = predictor.predict(X.head(5))
    assert len(predictions) == 5, "Prediction count mismatch"
    
    print(f"✓ Price Prediction Module: OK (R² = {metrics['test_r2']:.4f})")

def main():
    """Run all tests"""
    print("=" * 60)
    print("Riyadh Real Estate Analytics Platform - Test Suite")
    print("منصة تحليل العقارات في الرياض - مجموعة الاختبارات")
    print("=" * 60)
    print()
    
    try:
        test_data_processing()
        test_market_analysis()
        test_price_prediction()
        
        print()
        print("=" * 60)
        print("✓ All tests passed successfully!")
        print("✓ جميع الاختبارات نجحت!")
        print("=" * 60)
        return 0
        
    except Exception as e:
        print()
        print("=" * 60)
        print(f"✗ Test failed: {str(e)}")
        print(f"✗ فشل الاختبار: {str(e)}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
