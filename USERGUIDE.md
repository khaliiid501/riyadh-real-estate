# دليل المستخدم | User Guide

## جدول المحتويات | Table of Contents

1. [المقدمة | Introduction](#introduction)
2. [البدء السريع | Quick Start](#quick-start)
3. [معالجة البيانات | Data Processing](#data-processing)
4. [التحليل السوقي | Market Analysis](#market-analysis)
5. [التنبؤ بالأسعار | Price Prediction](#price-prediction)
6. [أمثلة متقدمة | Advanced Examples](#advanced-examples)
7. [الأسئلة الشائعة | FAQ](#faq)

## المقدمة | Introduction

منصة تحليل العقارات في الرياض هي أداة شاملة لتحليل والتنبؤ بأسعار العقارات في مدينة الرياض باستخدام تقنيات التعلم الآلي.

The Riyadh Real Estate Analytics Platform is a comprehensive tool for analyzing and predicting property prices in Riyadh using machine learning techniques.

## البدء السريع | Quick Start

### التثبيت | Installation

```bash
pip install -r requirements.txt
pip install -e .
```

### استخدام أساسي | Basic Usage

```python
from riyadh_real_estate import RiyadhRealEstateData, PricePredictor, MarketAnalyzer

# إنشاء بيانات عينة | Create sample data
processor = RiyadhRealEstateData()
df = processor.create_sample_data(n_samples=500)

# تحليل | Analyze
analyzer = MarketAnalyzer(df)
trends = analyzer.get_market_trends()

# تنبؤ | Predict
processor.clean_data()
X, y = processor.get_feature_matrix()
predictor = PricePredictor()
metrics = predictor.train(X, y)
```

## معالجة البيانات | Data Processing

### تحميل البيانات | Loading Data

#### من ملف CSV | From CSV File

```python
processor = RiyadhRealEstateData()
df = processor.load_data('path/to/data.csv')
```

#### إنشاء بيانات عينة | Create Sample Data

```python
df = processor.create_sample_data(n_samples=1000)
```

### تنظيف البيانات | Cleaning Data

```python
cleaned_df = processor.clean_data()
```

هذه الوظيفة:
- تزيل التكرارات
- تعالج القيم المفقودة
- تحذف القيم الشاذة

This function:
- Removes duplicates
- Handles missing values
- Removes outliers

### إعداد البيانات للنمذجة | Preparing Data for Modeling

```python
X, y = processor.get_feature_matrix()
```

## التحليل السوقي | Market Analysis

### تحليل حسب الحي | Analysis by District

```python
analyzer = MarketAnalyzer(df)
district_stats = analyzer.analyze_by_district()
print(district_stats)
```

يعرض:
- عدد العقارات
- متوسط السعر
- الوسيط
- القيم الدنيا والعليا
- الانحراف المعياري

Shows:
- Property count
- Average price
- Median
- Min and max values
- Standard deviation

### تحليل حسب نوع العقار | Analysis by Property Type

```python
type_stats = analyzer.analyze_by_property_type()
```

### اتجاهات السوق | Market Trends

```python
trends = analyzer.get_market_trends()
```

يوفر:
- إجمالي عدد العقارات
- متوسط السعر العام
- أكثر الأحياء نشاطاً
- توزيع أنواع العقارات

Provides:
- Total properties
- Overall average price
- Most active districts
- Property type distribution

### إيجاد أفضل العقارات قيمة | Finding Best Value Properties

```python
best_deals = analyzer.find_best_value_properties(n=10)
```

### مقارنة الأحياء | Comparing Districts

```python
comparison = analyzer.compare_districts(['العليا', 'الملقا', 'النرجس'])
```

## التنبؤ بالأسعار | Price Prediction

### اختيار النموذج | Model Selection

المنصة تدعم ثلاثة أنواع من النماذج:

The platform supports three model types:

```python
# Random Forest (الأفضل للدقة | Best for accuracy)
predictor = PricePredictor(model_type='random_forest')

# Gradient Boosting
predictor = PricePredictor(model_type='gradient_boosting')

# Linear Regression (الأسرع | Fastest)
predictor = PricePredictor(model_type='linear')
```

### تدريب النموذج | Training the Model

```python
metrics = predictor.train(X, y, test_size=0.2)

print(f"R² Score: {metrics['test_r2']:.4f}")
print(f"MAE: {metrics['test_mae']:,.2f} SAR")
print(f"RMSE: {metrics['test_rmse']:,.2f} SAR")
```

### التنبؤ بالأسعار | Making Predictions

#### تنبؤ جماعي | Batch Prediction

```python
predictions = predictor.predict(X_test)
```

#### تنبؤ لعقار واحد | Single Property Prediction

```python
property_features = {
    'المساحة_متر_مربع': 250,
    'عدد_الغرف': 4,
    'عدد_دورات_المياه': 3,
    # ... المزيد من الميزات
}
price = predictor.predict_single(property_features)
```

### أهمية الميزات | Feature Importance

```python
importance = predictor.get_feature_importance()
print(importance.head(10))
```

### حفظ وتحميل النموذج | Saving and Loading Model

```python
# حفظ | Save
predictor.save_model('models/my_model.pkl')

# تحميل | Load
new_predictor = PricePredictor()
new_predictor.load_model('models/my_model.pkl')
```

## أمثلة متقدمة | Advanced Examples

### مثال 1: تحليل شامل | Example 1: Comprehensive Analysis

```python
# تحميل البيانات | Load data
processor = RiyadhRealEstateData()
df = processor.create_sample_data(n_samples=2000)

# تحليل متقدم | Advanced analysis
analyzer = MarketAnalyzer(df)

# حساب السعر للمتر المربع لجميع العقارات
df_with_price_per_sqm = analyzer.calculate_price_per_sqm()

# تحليل توزيع الأسعار في كل حي
for district in df['الحي'].unique():
    district_data = df[df['الحي'] == district]
    avg_price = district_data['السعر_ريال'].mean()
    print(f"{district}: {avg_price:,.2f} SAR")
```

### مثال 2: مقارنة النماذج | Example 2: Model Comparison

```python
processor = RiyadhRealEstateData()
processor.create_sample_data(n_samples=1000)
processor.clean_data()
X, y = processor.get_feature_matrix()

models = ['random_forest', 'gradient_boosting', 'linear']
results = {}

for model_type in models:
    predictor = PricePredictor(model_type=model_type)
    metrics = predictor.train(X, y)
    results[model_type] = metrics['test_r2']
    print(f"{model_type}: R² = {metrics['test_r2']:.4f}")

best_model = max(results, key=results.get)
print(f"\nأفضل نموذج | Best model: {best_model}")
```

### مثال 3: تحليل مع تصورات | Example 3: Analysis with Visualizations

```python
analyzer = MarketAnalyzer(df)

# رسم توزيع الأسعار
analyzer.plot_price_distribution(save_path='plots/price_distribution.png')

# رسم الأسعار حسب الحي
analyzer.plot_price_by_district(save_path='plots/district_prices.png')

# رسم الارتباطات
analyzer.plot_correlation_heatmap(save_path='plots/correlations.png')
```

## الأسئلة الشائعة | FAQ

### س: كيف أعد بياناتي للاستخدام مع المنصة؟
Q: How do I prepare my data for use with the platform?

**ج:** تأكد من أن ملف CSV يحتوي على الأعمدة التالية:
- الحي (District)
- نوع_العقار (Property Type)
- المساحة_متر_مربع (Area in sqm)
- عدد_الغرف (Number of bedrooms)
- عدد_دورات_المياه (Number of bathrooms)
- عمر_العقار_سنوات (Age in years)
- المسافة_من_المركز_كم (Distance from center in km)
- السعر_ريال (Price in SAR)

**A:** Ensure your CSV file contains these columns with the exact names.

### س: ما هي دقة نماذج التنبؤ؟
Q: What is the accuracy of prediction models?

**ج:** تختلف الدقة حسب جودة البيانات وحجمها. عادةً:
- Random Forest: R² > 0.85
- Gradient Boosting: R² > 0.83
- Linear Regression: R² > 0.75

**A:** Accuracy varies with data quality and size. Typically the values shown above.

### س: كيف أحسّن دقة النموذج؟
Q: How can I improve model accuracy?

**ج:**
1. استخدم بيانات أكثر (> 1000 عقار)
2. أضف ميزات إضافية (مثل: القرب من الخدمات)
3. نظّف البيانات جيداً
4. استخدم Random Forest أو Gradient Boosting

**A:**
1. Use more data (> 1000 properties)
2. Add additional features
3. Clean data thoroughly
4. Use Random Forest or Gradient Boosting

### س: هل يمكنني استخدام المنصة لمدن أخرى؟
Q: Can I use the platform for other cities?

**ج:** نعم، يمكن تعديل المنصة بسهولة لأي مدينة. فقط استبدل البيانات وأسماء الأحياء.

**A:** Yes, the platform can be easily adapted for any city. Just replace data and district names.

### س: كيف أضيف ميزات جديدة للتنبؤ؟
Q: How do I add new features for prediction?

**ج:** أضف الأعمدة الجديدة لبياناتك وستتعامل معها `get_feature_matrix()` تلقائياً.

**A:** Add new columns to your data and `get_feature_matrix()` will handle them automatically.

## الدعم والمساهمة | Support and Contributing

للحصول على المساعدة أو المساهمة في المشروع:
- افتح issue على GitHub
- أرسل pull request
- راجع دليل المساهمة

For support or to contribute:
- Open an issue on GitHub
- Submit a pull request
- Review contribution guidelines
