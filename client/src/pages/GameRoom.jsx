// src/pages/GameRoom.jsx
import BlackjackTable from '../components/game/BlackjackTable';

export default function GameRoom() {
    return (
        <div className="min-h-screen bg-western-dark text-western-light">
            <BlackjackTable />
        </div>
    );
}