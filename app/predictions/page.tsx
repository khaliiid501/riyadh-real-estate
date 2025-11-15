'use client'
import { TrendingUp, AlertCircle, Info, Lightbulb } from 'lucide-react'

const regionalForecasts = [
  { region: 'شمال الرياض', forecast: '+4.5%', confidence: 'عالية', color: 'from-emerald-500 to-teal-600' },
  { region: 'شرق الرياض', forecast: '+3.2%', confidence: 'متوسطة', color: 'from-blue-500 to-cyan-600' },
  { region: 'غرب الرياض', forecast: '+3.8%', confidence: 'عالية', color: 'from-violet-500 to-purple-600' },
  { region: 'جنوب الرياض', forecast: '+2.9%', confidence: 'متوسطة', color: 'from-orange-500 to-amber-600' },
]

const factors = [
  { name: 'رؤية 2030', impact: '+20%', level: 'تأثير عالي', color: 'text-emerald-600', icon: Lightbulb },
  { name: 'مشروع مترو الرياض', impact: '+15%', level: 'تأثير عالي', color: 'text-blue-600', icon: TrendingUp },
  { name: 'التضخم وأسعار الفائدة', impact: '-5%', level: 'تأثير متوسط', color: 'text-amber-600', icon: Info },
  { name: 'العرض والطلب', impact: '+8%', level: 'تأثير عالي', color: 'text-violet-600', icon: TrendingUp },
  { name: 'تشريعات الإسكان', impact: '+3%', level: 'تأثير منخفض', color: 'text-gray-600', icon: Info },
]

const risks = [
  { title: 'تقلبات أسعار الفائدة', description: 'ارتفاع مفاجئ في أسعار الفائدة قد يضغط على الطلب العقاري.' },
  { title: 'تأخيرات مشروعات البنية التحتية', description: 'تأجيل مشاريع رئيسية يؤثر على توقعات نمو المناطق المتأثرة.' },
]

export default function PredictionsPage() {
  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-6 bg-gradient-to-l from-blue-600 to-indigo-600 bg-clip-text text-transparent">
        التنبؤات الإقليمية ومؤشرات المخاطر
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
        {regionalForecasts.map((f) => (
          <div key={f.region} className="glass-card rounded-2xl p-6 hover:shadow-2xl transition-all duration-300">
            <div className="flex items-center justify-between mb-4">
              <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${f.color} flex items-center justify-center`}> 
                <TrendingUp className="w-6 h-6 text-white" />
              </div>
              <div className="text-right">
                <h3 className="text-lg font-bold">{f.region}</h3>
                <p className="text-sm text-gray-500">الثقة: <span className="font-semibold text-gray-700">{f.confidence}</span></p>
              </div>
            </div>
            <p className="text-3xl font-bold text-gray-900">{f.forecast}</p>
            <p className="text-sm text-gray-500 mt-2">نمو متوقع سنوياً</p>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12">
        <div className="lg:col-span-2 glass-card rounded-2xl p-8">
          <h2 className="text-2xl font-bold mb-4 text-gray-900">العوامل الاقتصادية والسياسية المؤثرة</h2>
          <div className="space-y-4">
            {factors.map((factor) => {
              const Icon = factor.icon
              return (
                <div key={factor.name} className="flex items-center justify-between p-4 rounded-xl border border-gray-100">
                  <div className="flex items-center gap-4">
                    <div className={`w-12 h-12 rounded-lg bg-gray-50 flex items-center justify-center`}> 
                      <Icon className="w-5 h-5 text-gray-600" />
                    </div>
                    <div className="text-right">
                      <h3 className="font-semibold text-gray-800">{factor.name}</h3>
                      <p className="text-sm text-gray-500">{factor.level}</p>
                    </div>
                  </div>
                  <div className="text-left">
                    <p className={`font-bold ${factor.color}`}>{factor.impact}</p>
                    <p className="text-xs text-gray-400">تأثير متوقع</p>
                  </div>
                </div>
              )
            })}
          </div>
        </div>

        <div className="glass-card rounded-2xl p-8">
          <div className="flex items-start gap-4">
            <div className="p-3 rounded-full bg-red-100">
              <AlertCircle className="w-6 h-6 text-red-600" />
            </div>
            <div>
              <h3 className="text-lg font-bold text-gray-900 mb-2">مخاطر يجب مراقبتها</h3>
              <ul className="space-y-3 text-sm text-gray-600">
                {risks.map((r) => (
                  <li key={r.title}>
                    <p className="font-semibold text-gray-800">{r.title}</p>
                    <p className="text-xs text-gray-500">{r.description}</p>
                  </li>
                ))}
              </ul>
            </div>
          </div>
          
          <div className="mt-6 text-sm text-gray-500">
            <p>نصيحة: دمج هذه التنبؤات مع بيانات العرض والطلب في الوقت الحقيقي سيحسّن دقة التوصيات الاستثمارية.</p>
          </div>
        </div>
      </div>

      <div className="glass-card rounded-2xl p-6 text-center">
        <h3 className="text-lg font-bold text-gray-900 mb-2">ملاحظة منهجية</h3>
        <p className="text-sm text-gray-600 max-w-3xl mx-auto">
          التنبؤات مبنية على تحليل تاريخي لأسعار السوق والعوامل المؤثرة العامة. هذه التوقعات ليست استشارة استثمارية
          ويجب دائماً التحقق منها مع مصادر متعددة وبيانات مُحدثة قبل اتخاذ قرارات مالية.
        </p>
      </div>
    </div>
  )
}