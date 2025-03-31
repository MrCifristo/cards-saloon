import React from "react"

// src/components/auth/LoginForm.jsx
export default function LoginForm({ onLogin }) {
    const [nickname, setNickname] = React.useState('')
  
    const handleSubmit = (e) => {
      e.preventDefault()
      if (nickname.trim()) {
        onLogin(nickname.trim())
      }
    }
  
    return (
      <div 
        className="min-h-screen flex items-center justify-center bg-western-dark"
        style={{ backgroundImage: "url('https://media.istockphoto.com/id/157502989/es/foto/lejano-oeste-fondo-grunge-de-badlands.jpg?s=612x612&w=0&k=20&c=7nBxefXQ5de6ql0dwPmKVmIqpdaeBx5phYG8TvXhkYc=')", backgroundSize: 'cover' }}
      >
        <div className="bg-western-medium bg-opacity-90 p-8 rounded-lg shadow-xl border-2 border-western-accent w-full max-w-md mx-4">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-western text-western-accent mb-2">Wild Card Saloon</h1>
            <p className="text-western-light">Ingresa tu alias para unirte a la partida</p>
          </div>
          
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <div className="relative">
                <input
                  type="text"
                  value={nickname}
                  onChange={(e) => setNickname(e.target.value)}
                  className="block w-full px-4 py-3 bg-western-light bg-opacity-80 border border-western-accent rounded-md text-western-dark font-bold focus:outline-none focus:ring-2 focus:ring-western-accent"
                  placeholder="Tu alias de pistolero"
                  required
                />
                <div className="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
                  <svg className="h-5 w-5 text-western-red" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                </div>
              </div>
            </div>
            
            <button
              type="submit"
              className="w-full py-3 px-4 bg-western-red hover:bg-opacity-90 text-white font-western rounded-md shadow-lg transition duration-150 text-xl tracking-wider"
            >
              ENTRAR AL SALOON
            </button>
          </form>
          
          <div className="mt-6 text-center text-western-light text-sm">
            <p>Al entrar aceptas batirte en duelo de cartas</p>
          </div>
        </div>
      </div>
    )
  }