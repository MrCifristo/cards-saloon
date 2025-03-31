// src/pages/Home.jsx
import { useState } from 'react'
import LoginForm from '../components/auth/LoginForm'
import Lobby from '../components/lobby/Lobby'

export default function Home() {
  const [currentUser, setCurrentUser] = useState(null)
  const [view, setView] = useState('login') // 'login' | 'lobby'

  const handleLogin = (nickname) => {
    setCurrentUser({ nickname })
    setView('lobby')
  }

  const handleCreateRoom = () => {
    alert('Creando sala privada...') // Lógica real irá aquí
  }

  const handleJoinRoom = (roomId) => {
    alert(`Uniéndose a sala ${roomId}...`) // Lógica real irá aquí
  }

  return (
    <>
      {view === 'login' && <LoginForm onLogin={handleLogin} />}
      {view === 'lobby' && (
        <Lobby 
          onCreateRoom={handleCreateRoom}
          onJoinRoom={handleJoinRoom} 
        />
      )}
    </>
  )
}