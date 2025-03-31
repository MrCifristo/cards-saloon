// src/context/AuthContext.jsx
import { createContext, useState } from 'react'

export const AuthContext = createContext()

export function AuthProvider({ children }) {
  const [currentUser, setCurrentUser] = useState(null)
  
  const login = (nickname) => {
    setCurrentUser({
      nickname,
      id: Math.random().toString(36).substring(2, 9),
      balance: 100 // Saldo inicial Q100
    })
  }

  return (
    <AuthContext.Provider value={{ currentUser, login }}>
      {children}
    </AuthContext.Provider>
  )
}