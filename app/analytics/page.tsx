'use client'
import { LineChart, Line, BarChart, Bar, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

const priceData = [
  { year: '2020', villa: 1800, apartment: 1200, land: 900 },
  { year: '2021', villa: 1950, apartment: 1300, land: 1000 },
  { year: '2022', villa: 2100, apartment: 1450, land: 1150 },
  { year: '2023', villa: 2300, apartment: 1600, land: 1300 },
  { year: '2024', villa: 2500, apartment: 1800, land: 1500 },
  { year: '2025', villa: 2700, apartment: 2000, land: 1700 },
]

const neighborhoodData = [
  { name: 'النرجس', price: 3100 },
  { name: 'العليا', price: 2850 },
  { name: 'الياسمين', price: 2500 },
  { name: 'غرناطة', price: 2200 },
  { name: 'الربوة', price: 1950 },
]

const propertyTypes = [
  { name: 'فيلا', value: 45 },
  { name: 'شقة', value: 35 },
  { name: 'أرض', value: 20 },
]

const COLORS = ['#3b82f6', '#8b5cf6', '#10b981']

export default function AnalyticsPage() {
  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-8 bg-gradient-to-l from-blue-600 to-indigo-600 bg-clip-text text-transparent">
        لوحة التحليل المتقدمة
      </h1>

      <div className="glass-card rounded-2xl p-8 mb-8">
        <h2 className="text-2xl font-bold mb-6 text-gray-900">تطور الأسعار 2020-2025</h2>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart data={priceData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="villa" stroke="#3b82f6" strokeWidth={3} name="فيلا" />
            <Line type="monotone" dataKey="apartment" stroke="#8b5cf6" strokeWidth={3} name="شقة" />
            <Line type="monotone" dataKey="land" stroke="#10b981" strokeWidth={3} name="أرض" />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="glass-card rounded-2xl p-8">
          <h2 className="text-2xl font-bold mb-6 text-gray-900">مقارنة الأحياء - سعر المتر</h2>
          <ResponsiveContainer width="100%" height={400}>
            <BarChart data={neighborhoodData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="price" fill="#3b82f6" radius={[8, 8, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="glass-card rounded-2xl p-8">
          <h2 className="text-2xl font-bold mb-6 text-gray-900">توزيع أنواع العقارات</h2>
          <ResponsiveContainer width="100%" height={400}>
            <PieChart>
              <Pie
                data={propertyTypes}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                outerRadius={120}
                fill="#8884d8"
                dataKey="value"
              >
                {propertyTypes.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  )
}