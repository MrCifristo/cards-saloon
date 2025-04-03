// src/components/lobby/RoomCard.jsx
import React from 'react';

export default function RoomCard({ room }) {
  return (
    <div className="bg-[#2a1810] rounded-lg p-4 cursor-pointer hover:bg-[#3a2820] transition-colors border border-[#8b4513]">
      <h3 className="text-xl font-western text-[#e6d5b8]">{room.name}</h3>
      <p className="text-[#e6d5b8] mt-1">{room.gameType}</p>
      <div className="mt-2 text-[#e6d5b8] opacity-75 flex justify-between items-center">
        <span className="text-sm">
          {room.players} / {room.maxPlayers} jugadores
        </span>
        <div className="flex items-center gap-2">
          {room.status === 'en_curso' && (
            <span className="bg-[#8b4513] px-2 py-0.5 rounded text-xs">
              En curso
            </span>
          )}
        </div>
      </div>
    </div>
  );
}