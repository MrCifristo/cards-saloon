import React from "react"

// src/components/lobby/Lobby.jsx
export default function Lobby({ onCreateRoom, onJoinRoom }) {
    const [roomCode, setRoomCode] = React.useState('')
    
    // Salas de ejemplo (luego vendrán del backend)
    const publicRooms = [
      { id: '1', name: 'Mesa del Sheriff', players: 3, maxPlayers: 6, game: 'Blackjack' },
      { id: '2', name: 'Rincón de los Forajidos', players: 2, maxPlayers: 4, game: 'Póker' },
      { id: '3', name: 'Salón del Oro', players: 5, maxPlayers: 8, game: 'Blackjack' },
    ]
  
    return (
      <div className="min-h-screen bg-western-dark p-4" style={{ backgroundImage: "url('https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?ixlib=rb-4.0.3&ixid=M...')", backgroundSize: 'cover' }}>
        <div className="max-w-6xl mx-auto">
          <header className="mb-8 text-center">
            <h1 className="text-5xl font-western text-western-accent mb-2">Wild Card Saloon</h1>
            <p className="text-western-light text-xl">Elige tu partida, forastero</p>
          </header>
          
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Salas públicas */}
            <div className="lg:col-span-2">
              <div className="bg-western-medium bg-opacity-90 p-6 rounded-lg border-2 border-western-accent">
                <h2 className="text-2xl font-western text-western-light mb-4">Mesas Públicas</h2>
                
                <div className="space-y-4">
                  {publicRooms.map(room => (
                    <div 
                      key={room.id} 
                      className="p-4 bg-western-light bg-opacity-80 rounded-md border border-western-dark hover:border-western-accent transition cursor-pointer"
                      onClick={() => onJoinRoom(room.id)}
                    >
                      <div className="flex justify-between items-center">
                        <h3 className="font-bold text-western-dark text-lg">{room.name}</h3>
                        <span className="bg-western-red text-white px-2 py-1 rounded text-sm">
                          {room.players}/{room.maxPlayers} jugadores
                        </span>
                      </div>
                      <div className="flex justify-between mt-2 text-western-medium">
                        <span>Juego: {room.game}</span>
                        <button className="text-western-red hover:underline">Unirse</button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
            
            {/* Crear sala privada */}
            <div className="lg:col-span-1">
              <div className="bg-western-medium bg-opacity-90 p-6 rounded-lg border-2 border-western-accent h-full">
                <h2 className="text-2xl font-western text-western-light mb-4">Crear Sala Privada</h2>
                
                <button
                  onClick={onCreateRoom}
                  className="w-full py-3 px-4 bg-western-accent hover:bg-opacity-90 text-western-dark font-western rounded-md shadow-lg transition duration-150 text-xl tracking-wider mb-6"
                >
                  CREAR NUEVA SALA
                </button>
                
                <div className="mt-6">
                  <h3 className="font-western text-western-light mb-2">Unirse a sala privada</h3>
                  <div className="flex">
                    <input
                      type="text"
                      value={roomCode}
                      onChange={(e) => setRoomCode(e.target.value)}
                      className="flex-1 px-4 py-2 bg-western-light border border-western-accent rounded-l-md focus:outline-none focus:ring-1 focus:ring-western-accent"
                      placeholder="Código de sala"
                    />
                    <button
                      onClick={() => onJoinRoom(roomCode)}
                      className="bg-western-red text-white px-4 py-2 rounded-r-md hover:bg-opacity-90 transition"
                    >
                      Unirse
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }