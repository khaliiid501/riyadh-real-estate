import './globals.css'
import Navigation from '@/components/Navigation'
import { ReactNode } from 'react'

export const metadata = {
  title: 'منصة الرياض العقارية',
  description: 'تحليلات وتنبؤات لسوق العقارات في الرياض',
}

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="ar" dir="rtl">
      <body className="min-h-screen bg-gray-50 text-gray-900">
        <Navigation />
        <main>{children}</main>
      </body>
    </html>
  )
}