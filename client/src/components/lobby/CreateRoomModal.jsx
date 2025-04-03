import React, { useState } from 'react';
import WesternButton from '../shared/WesternButton';

export default function CreateRoomModal({ onClose }) {
  const [roomData, setRoomData] = useState({
    name: '',
    gameType: 'poker',
    maxPlayers: 4,
    isPrivate: false
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    // Aquí iría la lógica para crear la sala
    console.log('Crear sala:', roomData);
    onClose();
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
      <div className="bg-[#2a1810] rounded-lg p-6 w-full max-w-md border border-[#8b4513]">
        <h2 className="text-2xl font-western text-[#e6d5b8] mb-6">CREAR NUEVA SALA</h2>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-[#e6d5b8] mb-2">Nombre de la Sala</label>
            <input
              type="text"
              value={roomData.name}
              onChange={(e) => setRoomData({ ...roomData, name: e.target.value })}
              className="w-full bg-[#3a2820] text-[#e6d5b8] border border-[#8b4513] rounded px-3 py-2 focus:outline-none focus:border-[#a0522d]"
              placeholder="Ingresa un nombre para tu sala"
            />
          </div>

          <div>
            <label className="block text-[#e6d5b8] mb-2">Tipo de Juego</label>
            <select
              value={roomData.gameType}
              onChange={(e) => setRoomData({ ...roomData, gameType: e.target.value })}
              className="w-full bg-[#3a2820] text-[#e6d5b8] border border-[#8b4513] rounded px-3 py-2 focus:outline-none focus:border-[#a0522d]"
            >
              <option value="poker">Póker</option>
              <option value="blackjack">Blackjack</option>
            </select>
          </div>

          <div>
            <label className="block text-[#e6d5b8] mb-2">Número Máximo de Jugadores</label>
            <select
              value={roomData.maxPlayers}
              onChange={(e) => setRoomData({ ...roomData, maxPlayers: Number(e.target.value) })}
              className="w-full bg-[#3a2820] text-[#e6d5b8] border border-[#8b4513] rounded px-3 py-2 focus:outline-none focus:border-[#a0522d]"
            >
              {[2, 3, 4, 5, 6, 7, 8].map(num => (
                <option key={num} value={num}>{num} jugadores</option>
              ))}
            </select>
          </div>

          <div className="flex items-center">
            <input
              type="checkbox"
              id="isPrivate"
              checked={roomData.isPrivate}
              onChange={(e) => setRoomData({ ...roomData, isPrivate: e.target.checked })}
              className="mr-2"
            />
            <label htmlFor="isPrivate" className="text-[#e6d5b8]">Sala Privada</label>
          </div>

          <div className="flex gap-4 mt-6">
            <WesternButton type="submit" primary fullWidth>
              CREAR SALA
            </WesternButton>
            <WesternButton type="button" fullWidth onClick={onClose}>
              CANCELAR
            </WesternButton>
          </div>
        </form>
      </div>
    </div>
  );
}
