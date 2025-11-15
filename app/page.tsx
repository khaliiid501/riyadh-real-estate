import KPICard from '@/components/KPICard'
import { Home, Building, TrendingUp, Target } from 'lucide-react'

const neighborhoods = [
  { name: 'النرجس', price: '3,100', change: '+9%', color: 'from-emerald-500 to-teal-600' },
  { name: 'العليا', price: '2,850', change: '+8%', color: 'from-blue-500 to-cyan-600' },
  { name: 'الياسمين', price: '2,500', change: '+7%', color: 'from-violet-500 to-purple-600' },
  { name: 'غرناطة', price: '2,200', change: '+6%', color: 'from-orange-500 to-amber-600' },
]

export default function HomePage() {
  return (
    <div className="container mx-auto px-4 py-12">
      <div className="text-center mb-16">
        <h1 className="text-5xl font-bold mb-4 bg-gradient-to-l from-blue-600 via-indigo-600 to-violet-600 bg-clip-text text-transparent">
          منصة الرياض العقارية
        </h1>
        <p className="text-xl text-gray-600 max-w-2xl mx-auto">
          تحليلات ذكية وتنبؤات دقيقة لسوق العقارات في الرياض
          <br />
          توفر لك أدوات متقدمة لاتخاذ قرارات استثمارية مدروسة
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
        <KPICard
          title="متوسط سعر المتر"
          value="2,250 ريال"
          change="+7.2%"
          icon={Home}
          color="from-blue-500 to-blue-600"
        />
        <KPICard
          title="إجمالي العقارات"
          value="1,245,890"
          icon={Building}
          color="from-indigo-500 to-indigo-600"
        />
        <KPICard
          title="معدل العائد ROI"
          value="8.2%"
          icon={TrendingUp}
          color="from-emerald-500 to-emerald-600"
        />
        <KPICard
          title="مستوى الثقة"
          value="87%"
          icon={Target}
          color="from-violet-500 to-violet-600"
        />
      </div>

      <div className="mb-12">
        <h2 className="text-3xl font-bold mb-8 text-gray-900">أسعار الأحياء المميزة</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {neighborhoods.map((neighborhood) => (
            <div
              key={neighborhood.name}
              className="glass-card rounded-2xl p-6 hover:shadow-2xl transition-all duration-300"
            >
              <div className={`w-12 h-12 rounded-xl bg-gradient-to-br ${neighborhood.color} mb-4`} />
              <h3 className="text-xl font-bold text-gray-900 mb-2">{neighborhood.name}</h3>
              <p className="text-3xl font-bold text-gray-900 mb-2">{neighborhood.price}</p>
              <p className="text-sm text-gray-600 mb-2">ريال/متر</p>
              <div className="flex items-center gap-2">
                <span className="text-green-600 font-bold">{neighborhood.change}</span>
                <span className="text-gray-500 text-sm">نمو سنوي</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="glass-card rounded-2xl p-8 text-center">
        <h3 className="text-xl font-bold mb-4 text-gray-900">مصادر البيانات</h3>
        <div className="flex flex-wrap justify-center gap-6 text-sm text-gray-600">
          <span>الهيئة العامة للإحصاء (GASTAT)</span>
          <span>•</span>
          <span>وزارة الشؤون البلدية (MOMRA)</span>
          <span>•</span>
          <span>منصة سكني (Sakani)</span>
          <span>•</span>
          <span>صندوق التنمية العقارية (REDF)</span>
        </div>
        <p className="text-sm text-gray-500 mt-4">آخر تحديث: نوفمبر 2025</p>
      </div>
    </div>
  )
}