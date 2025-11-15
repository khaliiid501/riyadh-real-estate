# دليل البداية السريعة | Quick Start Guide

## التثبيت السريع | Quick Installation

```bash
# 1. استنساخ المستودع | Clone repository
git clone https://github.com/khaliiid501/riyadh-real-estate.git
cd riyadh-real-estate

# 2. تثبيت المتطلبات | Install requirements
pip install -r requirements.txt

# 3. تثبيت الحزمة | Install package
pip install -e .

# 4. اختبار التثبيت | Test installation
python test_platform.py
```

## استخدام سريع | Quick Usage

### Python Script

```python
from riyadh_real_estate import RiyadhRealEstateData, PricePredictor, MarketAnalyzer

# إنشاء بيانات عينة | Create sample data
processor = RiyadhRealEstateData()
df = processor.create_sample_data(n_samples=500)

# تحليل السوق | Analyze market
analyzer = MarketAnalyzer(df)
trends = analyzer.get_market_trends()
print(trends)

# بناء نموذج تنبؤ | Build prediction model
processor.clean_data()
X, y = processor.get_feature_matrix()

predictor = PricePredictor(model_type='random_forest')
metrics = predictor.train(X, y)
print(f"Model R² Score: {metrics['test_r2']:.4f}")
```

### Jupyter Notebook

```bash
# تشغيل Jupyter | Run Jupyter
jupyter notebook notebooks/demo.ipynb
```

## الوظائف الأساسية | Core Functions

### 1. معالجة البيانات | Data Processing
- `create_sample_data()` - إنشاء بيانات عينة
- `load_data()` - تحميل بيانات من CSV
- `clean_data()` - تنظيف البيانات
- `get_statistics()` - احصائيات وصفية

### 2. التنبؤ | Prediction
- `train()` - تدريب النموذج
- `predict()` - التنبؤ بالأسعار
- `get_feature_importance()` - أهمية الميزات

### 3. التحليل | Analysis
- `analyze_by_district()` - تحليل حسب الحي
- `analyze_by_property_type()` - تحليل حسب النوع
- `get_market_trends()` - اتجاهات السوق

## الأسئلة الشائعة | FAQ

**س: كيف أستخدم بياناتي الخاصة؟**
ج: استخدم `load_data('path/to/file.csv')` مع التأكد من تطابق أسماء الأعمدة.

**Q: How do I use my own data?**
A: Use `load_data('path/to/file.csv')` ensuring column names match the expected format.

**س: ما هي دقة النموذج؟**
ج: تختلف حسب البيانات، لكن عادة R² > 0.80 مع بيانات جيدة.

**Q: What is the model accuracy?**
A: Varies with data quality, typically R² > 0.80 with good data.

## الدعم | Support

للمساعدة، افتح issue في GitHub.

For help, open an issue on GitHub.
