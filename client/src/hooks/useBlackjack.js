import { useState, useCallback } from 'react';

const useBlackjack = () => {
    const [gameState, setGameState] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const startGame = useCallback(async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await fetch('/api/blackjack/start', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            const data = await response.json();
            setGameState(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }, []);

    const hit = useCallback(async (playerId) => {
        setLoading(true);
        setError(null);
        try {
            const response = await fetch('/api/blackjack/hit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ playerId }),
            });
            const data = await response.json();
            setGameState(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }, []);

    const stand = useCallback(async (playerId) => {
        setLoading(true);
        setError(null);
        try {
            const response = await fetch('/api/blackjack/stand', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ playerId }),
            });
            const data = await response.json();
            setGameState(data);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }, []);

    const placeBet = useCallback(async (playerId, amount) => {
        setLoading(true);
        setError(null);
        try {
            const response = await fetch('/api/blackjack/bet', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ playerId, amount }),
            });
            const data = await response.json();
            setGameState(data.game_state);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }, []);

    return {
        gameState,
        loading,
        error,
        startGame,
        hit,
        stand,
        placeBet,
    };
};

export default useBlackjack; 