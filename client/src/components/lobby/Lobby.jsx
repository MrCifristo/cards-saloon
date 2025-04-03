import React, { useState } from 'react';
import RoomCard from './RoomCard';
import WesternButton from '../shared/WesternButton';
import CreateRoomModal from './CreateRoomModal';

const SAMPLE_ROOMS = [
  {
    id: 1,
    name: "CALICO DRAW",
    gameType: "Blackjack",
    players: 2,
    maxPlayers: 6,
    status: 'disponible'
  },
  {
    id: 2,
    name: "RED ROCK TABLE",
    gameType: "Poker",
    players: 4,
    maxPlayers: 8,
    status: 'en_curso'
  },
  {
    id: 3,
    name: "HIGH NOON HAND",
    gameType: "Poker",
    players: 5,
    maxPlayers: 8,
    status: 'disponible'
  }
];

export default function Lobby() {
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [rooms] = useState(SAMPLE_ROOMS);

  return (
    <div className="min-h-screen bg-[url('../assets/images/background-cards-saloon.png')] bg-cover bg-center p-8">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-6xl font-western text-[#e6d5b8] mb-4">CARDS SALOON</h1>
          <p className="text-xl text-[#e6d5b8]">
            Juega cartas en línea con tus amigos.
            <br />
            ¡Únete a una sala o crea tu propia sala privada!
          </p>
        </div>

        {/* Action Buttons */}
        <div className="space-y-4 mb-12">
          <WesternButton 
            primary 
            fullWidth 
            onClick={() => setShowCreateModal(true)}
          >
            CREAR SALA PRIVADA
          </WesternButton>
          <WesternButton fullWidth>
            UNIRSE A SALA
          </WesternButton>
        </div>

        {/* Game Rooms */}
        <div>
          <h2 className="text-2xl font-western text-[#e6d5b8] mb-6">UNIRSE A UNA SALA DE JUEGO</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {rooms.map(room => (
              <RoomCard key={room.id} room={room} />
            ))}
          </div>
        </div>
      </div>

      {showCreateModal && (
        <CreateRoomModal 
          onClose={() => setShowCreateModal(false)} 
        />
      )}
    </div>
  );
}