# منصة تحليل العقارات في الرياض | Riyadh Real Estate Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🏠 نظرة عامة | Overview

منصة تحليلية عقارية متقدمة لمدينة الرياض تقوم على التنبؤ بأسعار العقارات وفق معطيات الواقع باستخدام تقنيات التعلم الآلي والتحليل الإحصائي.

An advanced real estate analytics platform for Riyadh that predicts property prices based on real-world data using machine learning and statistical analysis techniques.

## ✨ المميزات | Features

### 📊 معالجة البيانات | Data Processing
- تحميل وتنظيف بيانات العقارات
- معالجة القيم المفقودة والشاذة
- توليد بيانات عينة للاختبار والتطوير

### 🔮 التنبؤ بالأسعار | Price Prediction
- نماذج تعلم آلي متقدمة (Random Forest, Gradient Boosting, Linear Regression)
- تقييم دقة النماذج باستخدام مقاييس متعددة
- التنبؤ بأسعار العقارات بناءً على الخصائص

### 📈 تحليل السوق | Market Analysis
- تحليل السوق حسب الأحياء
- تحليل السوق حسب نوع العقار
- حساب السعر للمتر المربع
- تحديد اتجاهات السوق
- إيجاد العقارات ذات القيمة الأفضل

### 📉 التصورات البيانية | Visualizations
- توزيع الأسعار
- مقارنة الأحياء
- تحليل الارتباطات
- رسوم بيانية تفاعلية

## 🚀 التثبيت | Installation

### المتطلبات | Requirements
- Python 3.8 أو أحدث | Python 3.8 or higher
- pip (مدير حزم بايثون | Python package manager)

### خطوات التثبيت | Installation Steps

1. **استنساخ المستودع | Clone the repository**
```bash
git clone https://github.com/khaliiid501/riyadh-real-estate.git
cd riyadh-real-estate
```

2. **إنشاء بيئة افتراضية (اختياري لكن موصى به) | Create virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # على Linux/Mac | On Linux/Mac
# أو | or
venv\Scripts\activate  # على Windows | On Windows
```

3. **تثبيت المتطلبات | Install dependencies**
```bash
pip install -r requirements.txt
```

4. **تثبيت الحزمة | Install the package**
```bash
pip install -e .
```

## 📖 الاستخدام | Usage

### مثال سريع | Quick Example

```python
from riyadh_real_estate import RiyadhRealEstateData, PricePredictor, MarketAnalyzer

# 1. تحميل ومعالجة البيانات | Load and process data
data_processor = RiyadhRealEstateData()

# إنشاء بيانات عينة للتجربة | Create sample data for testing
df = data_processor.create_sample_data(n_samples=500)

# أو تحميل بياناتك الخاصة | Or load your own data
# df = data_processor.load_data('path/to/your/data.csv')

# 2. تحليل السوق | Market analysis
analyzer = MarketAnalyzer(df)
trends = analyzer.get_market_trends()
district_analysis = analyzer.analyze_by_district()

# 3. بناء نموذج التنبؤ | Build prediction model
cleaned_data = data_processor.clean_data()
X, y = data_processor.get_feature_matrix()

predictor = PricePredictor(model_type='random_forest')
metrics = predictor.train(X, y)

print(f"Model R² Score: {metrics['test_r2']:.4f}")

# 4. التنبؤ بالأسعار | Predict prices
predictions = predictor.predict(X.head(10))
```

### دفتر ملاحظات تفاعلي | Interactive Notebook

للحصول على تجربة تفاعلية كاملة، استخدم دفتر Jupyter المرفق:

For a complete interactive experience, use the included Jupyter notebook:

```bash
jupyter notebook notebooks/demo.ipynb
```

## 📁 هيكل المشروع | Project Structure

```
riyadh-real-estate/
├── riyadh_real_estate/          # الحزمة الرئيسية | Main package
│   ├── __init__.py              # تهيئة الحزمة | Package initialization
│   ├── data_processor.py        # معالجة البيانات | Data processing
│   ├── predictor.py             # نماذج التنبؤ | Prediction models
│   └── analyzer.py              # تحليل السوق | Market analysis
├── notebooks/                   # دفاتر Jupyter | Jupyter notebooks
│   └── demo.ipynb              # دفتر توضيحي | Demo notebook
├── data/                        # مجلد البيانات | Data folder
│   ├── raw/                     # بيانات خام | Raw data
│   └── processed/               # بيانات معالجة | Processed data
├── models/                      # نماذج محفوظة | Saved models
├── requirements.txt             # المتطلبات | Dependencies
├── setup.py                     # إعداد التثبيت | Setup configuration
└── README.md                    # هذا الملف | This file
```

## 🔧 الوحدات والفئات | Modules and Classes

### 1. RiyadhRealEstateData
معالجة وإدارة بيانات العقارات | Process and manage real estate data

**الوظائف الرئيسية | Main Methods:**
- `load_data(file_path)` - تحميل البيانات من ملف CSV
- `create_sample_data(n_samples)` - إنشاء بيانات عينة
- `clean_data()` - تنظيف ومعالجة البيانات
- `get_feature_matrix()` - إعداد مصفوفة الميزات للنمذجة
- `get_statistics()` - الحصول على الإحصائيات الوصفية

### 2. PricePredictor
التنبؤ بأسعار العقارات باستخدام التعلم الآلي | Predict property prices using ML

**الوظائف الرئيسية | Main Methods:**
- `train(X, y, test_size)` - تدريب النموذج
- `predict(X)` - التنبؤ بالأسعار
- `predict_single(property_features)` - التنبؤ لعقار واحد
- `get_feature_importance()` - الحصول على أهمية الميزات
- `save_model(file_path)` - حفظ النموذج
- `load_model(file_path)` - تحميل نموذج محفوظ

**أنواع النماذج المدعومة | Supported Model Types:**
- `random_forest` - غابات عشوائية (افتراضي | default)
- `gradient_boosting` - تعزيز التدرج
- `linear` - انحدار خطي

### 3. MarketAnalyzer
تحليل السوق العقاري وإنشاء التقارير | Analyze real estate market and generate reports

**الوظائف الرئيسية | Main Methods:**
- `analyze_by_district()` - تحليل حسب الحي
- `analyze_by_property_type()` - تحليل حسب نوع العقار
- `calculate_price_per_sqm()` - حساب السعر للمتر المربع
- `get_market_trends()` - الحصول على اتجاهات السوق
- `find_best_value_properties(n)` - إيجاد أفضل العقارات قيمة
- `compare_districts(districts)` - مقارنة أحياء محددة
- `plot_price_distribution()` - رسم توزيع الأسعار
- `plot_price_by_district()` - رسم الأسعار حسب الحي

## 📊 البيانات المتوقعة | Expected Data Format

يتوقع النظام بيانات عقارية تحتوي على الأعمدة التالية:

The system expects real estate data with the following columns:

| العمود | Column | الوصف | Description | النوع | Type |
|--------|--------|-------|-------------|------|------|
| الحي | District | الحي السكني | Residential district | نص | Text |
| نوع_العقار | Property Type | نوع العقار (شقة، فيلا، أرض) | Property type | نص | Text |
| المساحة_متر_مربع | Area (SQM) | المساحة بالمتر المربع | Area in square meters | رقم | Number |
| عدد_الغرف | Bedrooms | عدد غرف النوم | Number of bedrooms | رقم | Number |
| عدد_دورات_المياه | Bathrooms | عدد دورات المياه | Number of bathrooms | رقم | Number |
| عمر_العقار_سنوات | Age (Years) | عمر العقار بالسنوات | Property age in years | رقم | Number |
| المسافة_من_المركز_كم | Distance (KM) | المسافة من مركز المدينة | Distance from city center | رقم | Number |
| السعر_ريال | Price (SAR) | السعر بالريال السعودي | Price in Saudi Riyals | رقم | Number |

## 🎯 أمثلة الاستخدام | Usage Examples

### مثال 1: تحليل بيانات عقارية | Example 1: Analyze Real Estate Data

```python
from riyadh_real_estate import RiyadhRealEstateData, MarketAnalyzer

# تحميل البيانات | Load data
processor = RiyadhRealEstateData()
df = processor.create_sample_data(n_samples=1000)

# تحليل السوق | Analyze market
analyzer = MarketAnalyzer(df)

# الحصول على تحليل الأحياء | Get district analysis
district_stats = analyzer.analyze_by_district()
print(district_stats)

# إيجاد أفضل 10 عقارات قيمة | Find top 10 best value properties
best_deals = analyzer.find_best_value_properties(n=10)
print(best_deals)
```

### مثال 2: بناء نموذج تنبؤ | Example 2: Build Prediction Model

```python
from riyadh_real_estate import RiyadhRealEstateData, PricePredictor

# إعداد البيانات | Prepare data
processor = RiyadhRealEstateData()
processor.create_sample_data(n_samples=1000)
processor.clean_data()
X, y = processor.get_feature_matrix()

# تدريب النموذج | Train model
predictor = PricePredictor(model_type='random_forest')
metrics = predictor.train(X, y, test_size=0.2)

# عرض الأداء | Display performance
print(f"R² Score: {metrics['test_r2']:.4f}")
print(f"MAE: {metrics['test_mae']:,.2f} SAR")

# حفظ النموذج | Save model
predictor.save_model('models/riyadh_price_model.pkl')
```

### مثال 3: التنبؤ بسعر عقار | Example 3: Predict Property Price

```python
from riyadh_real_estate import PricePredictor

# تحميل نموذج محفوظ | Load saved model
predictor = PricePredictor()
predictor.load_model('models/riyadh_price_model.pkl')

# التنبؤ بسعر عقار جديد | Predict price for new property
# ملاحظة: يجب أن تطابق الميزات النموذج المدرب
# Note: Features must match the trained model
property_features = {
    'المساحة_متر_مربع': 250,
    'عدد_الغرف': 4,
    'عدد_دورات_المياه': 3,
    'عمر_العقار_سنوات': 5,
    'المسافة_من_المركز_كم': 10,
    # ... ميزات أخرى | other features
}

predicted_price = predictor.predict_single(property_features)
print(f"السعر المتوقع: {predicted_price:,.2f} ريال")
print(f"Predicted Price: {predicted_price:,.2f} SAR")
```

## 🤝 المساهمة | Contributing

نرحب بالمساهمات! إذا كنت ترغب في المساهمة:

Contributions are welcome! If you'd like to contribute:

1. انسخ المستودع (Fork)
2. أنشئ فرعاً للميزة الجديدة (`git checkout -b feature/AmazingFeature`)
3. قم بتنفيذ تغييراتك (`git commit -m 'Add some AmazingFeature'`)
4. ادفع إلى الفرع (`git push origin feature/AmazingFeature`)
5. افتح طلب سحب (Pull Request)

## 📝 الترخيص | License

هذا المشروع مرخص بموجب ترخيص MIT - انظر ملف [LICENSE](LICENSE) للتفاصيل.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 المؤلف | Author

**khaliiid501**

## 🙏 شكر وتقدير | Acknowledgments

- شكراً لجميع المساهمين في مكتبات التعلم الآلي مفتوحة المصدر
- Thanks to all contributors to open-source machine learning libraries
- البيانات المستخدمة في الأمثلة هي بيانات عينة وليست حقيقية
- Sample data used in examples is synthetic and not real

## 📧 التواصل | Contact

للأسئلة والاستفسارات، يرجى فتح issue في المستودع.

For questions and inquiries, please open an issue in the repository.

---

**ملاحظة:** هذه منصة تحليلية وليست بديلاً عن الاستشارة المهنية في مجال العقارات.

**Note:** This is an analytical platform and not a substitute for professional real estate consultation.