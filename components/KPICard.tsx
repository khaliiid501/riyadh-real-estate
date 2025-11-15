import { LucideIcon } from 'lucide-react'

interface KPICardProps {
  title: string
  value: string
  change?: string
  icon: LucideIcon
  color: string
}

export default function KPICard({ title, value, change, icon: Icon, color }: KPICardProps) {
  return (
    <div className="glass-card rounded-2xl p-6 hover:shadow-2xl transition-all duration-300">
      <div className="flex items-start justify-between mb-4">
        <div className={`p-3 rounded-xl bg-gradient-to-br ${color}`}> 
          <Icon className="w-6 h-6 text-white" />
        </div>
        {change && (
          <span className="text-green-600 font-bold text-sm flex items-center gap-1">
            <span>↑</span>
            {change}
          </span>
        )}
      </div>
      <h3 className="text-gray-600 text-sm mb-2">{title}</h3>
      <p className="text-3xl font-bold text-gray-900">{value}</p>
    </div>
  )
}