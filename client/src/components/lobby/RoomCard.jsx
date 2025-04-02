// src/components/lobby/RoomCard.jsx
export default function RoomCard({ room }) {
    return (
      <div className="bg-western-medium border border-western-accent rounded-lg p-4 hover:shadow-lg transition-shadow">
        <h3 className="font-western text-xl text-western-accent">{room.name}</h3>
        <div className="flex justify-between mt-2">
          <span>Jugadores: {room.players}/{room.maxPlayers}</span>
          <span className="bg-western-red text-white px-2 rounded">
            {room.gameType}
          </span>
        </div>
        <button className="mt-3 w-full bg-western-accent hover:bg-western-red text-black py-1 rounded transition-colors">
          Unirse
        </button>
      </div>
    )
  }