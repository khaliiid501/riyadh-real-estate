'use client'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { Building2, BarChart3, TrendingUp, Database } from 'lucide-react'

export default function Navigation() {
  const pathname = usePathname()
  
  const links = [
    { href: '/', label: 'الرئيسية', icon: Building2 },
    { href: '/analytics', label: 'التحليلات', icon: BarChart3 },
    { href: '/predictions', label: 'التنبؤات', icon: TrendingUp },
    { href: '/sources', label: 'مصادر البيانات', icon: Database },
  ]

  return (
    <nav className="sticky top-0 z-50 bg-white/80 backdrop-blur-lg border-b border-gray-200/50 shadow-sm">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center gap-2">
            <Building2 className="w-8 h-8 text-blue-600" />
            <span className="text-xl font-bold bg-gradient-to-l from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              الرياض العقارية
            </span>
          </div>
          
          <div className="flex gap-1">
            {links.map(({ href, label, icon: Icon }) => (
              <Link
                key={href}
                href={href}
                className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
                  pathname === href
                    ? 'bg-blue-600 text-white shadow-lg'
                    : 'text-gray-700 hover:bg-gray-100'
                }`}
              >
                <Icon className="w-4 h-4" />
                <span className="font-semibold">{label}</span>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </nav>
  )
}