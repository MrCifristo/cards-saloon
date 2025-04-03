import React from 'react';
import useBlackjack from '../../hooks/useBlackjack';
import Card from '../shared/Card';
import WesternButton from '../shared/WesternButton';

const BlackjackTable = () => {
    const { gameState, loading, error, startGame, hit, stand, placeBet } = useBlackjack();

    if (loading) return (
        <div className="min-h-screen bg-western-dark flex items-center justify-center">
            <div className="text-western-light text-2xl font-western animate-pulse">
                Cargando...
            </div>
        </div>
    );

    if (error) return (
        <div className="min-h-screen bg-western-dark flex items-center justify-center">
            <div className="text-western-red text-xl font-western">
                Error: {error}
            </div>
        </div>
    );

    return (
        <div className="min-h-screen bg-western-dark">
            {/* Fondo con textura de madera */}
            <div className="absolute inset-0 bg-western-pattern opacity-10"></div>
            
            {/* Contenido principal */}
            <div className="relative max-w-6xl mx-auto p-4">
                <div className="bg-western-table rounded-xl p-6 shadow-2xl border-4 border-western-border">
                    {!gameState ? (
                        <div className="flex flex-col items-center justify-center h-[60vh]">
                            <h1 className="text-western-light text-4xl font-western mb-8">
                                ¡Bienvenido al Salón!
                            </h1>
                            <WesternButton onClick={startGame}>
                                Iniciar Partida
                            </WesternButton>
                        </div>
                    ) : (
                        <div className="space-y-8">
                            {/* Estado del juego */}
                            <div className="text-center">
                                <h2 className="text-western-light text-2xl font-western">
                                    {gameState.game_status === "betting" ? "Fase de Apuestas" : "Partida en Curso"}
                                </h2>
                            </div>

                            {/* Mesa de juego */}
                            <div className="grid grid-cols-3 gap-6">
                                {Object.entries(gameState.players).map(([playerId, player]) => (
                                    <div 
                                        key={playerId}
                                        className={`
                                            bg-western-card rounded-lg p-4
                                            ${gameState.current_player === playerId ? 'ring-4 ring-western-gold' : ''}
                                            transition-all duration-300
                                        `}
                                    >
                                        <div className="flex justify-between items-center mb-4">
                                            <h3 className="text-western-light text-xl font-western">
                                                {playerId}
                                            </h3>
                                            <span className="text-western-gold font-western">
                                                ${player.balance}
                                            </span>
                                        </div>

                                        {/* Mano del jugador */}
                                        <div className="flex space-x-2 mb-4">
                                            {player.hand.map((card, index) => (
                                                <Card
                                                    key={index}
                                                    value={card.value}
                                                    suit={card.suit}
                                                />
                                            ))}
                                        </div>

                                        {/* Acciones del jugador */}
                                        {gameState.current_player === playerId && (
                                            <div className="flex space-x-2 justify-center">
                                                <WesternButton
                                                    variant="success"
                                                    onClick={() => hit(playerId)}
                                                >
                                                    Pedir
                                                </WesternButton>
                                                <WesternButton
                                                    variant="danger"
                                                    onClick={() => stand(playerId)}
                                                >
                                                    Plantarse
                                                </WesternButton>
                                            </div>
                                        )}
                                    </div>
                                ))}
                            </div>

                            {/* Panel de apuestas */}
                            {gameState.game_status === "betting" && (
                                <div className="bg-western-card rounded-lg p-4 mt-4">
                                    <h3 className="text-western-light text-xl font-western mb-4">
                                        Hacer Apuesta
                                    </h3>
                                    <div className="flex space-x-4 items-center">
                                        <input
                                            type="number"
                                            className="bg-western-input text-western-light rounded-lg px-4 py-2 w-32"
                                            placeholder="Cantidad"
                                        />
                                        <WesternButton
                                            variant="primary"
                                            onClick={() => placeBet("player1", 100)}
                                        >
                                            Apostar
                                        </WesternButton>
                                    </div>
                                </div>
                            )}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default BlackjackTable; 