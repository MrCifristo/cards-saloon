import React from 'react';

const Card = ({ value, suit, isHidden = false }) => {
    const getSuitSymbol = (suit) => {
        switch (suit.toLowerCase()) {
            case 'hearts': return '♥';
            case 'diamonds': return '♦';
            case 'clubs': return '♣';
            case 'spades': return '♠';
            default: return suit;
        }
    };

    const getColor = (suit) => {
        return ['hearts', 'diamonds'].includes(suit.toLowerCase()) ? 'text-red-600' : 'text-black';
    };

    if (isHidden) {
        return (
            <div className="w-20 h-28 bg-western-card-back bg-cover rounded-lg shadow-lg transform hover:scale-105 transition-transform duration-200 border-2 border-western-brown">
                <div className="w-full h-full bg-western-pattern opacity-90 rounded-lg"></div>
            </div>
        );
    }

    return (
        <div className="w-20 h-28 bg-white rounded-lg shadow-lg transform hover:scale-105 transition-transform duration-200 border-2 border-western-brown">
            <div className="h-full flex flex-col justify-between p-2">
                <div className={`text-xl font-bold ${getColor(suit)}`}>
                    {value}
                </div>
                <div className={`text-3xl ${getColor(suit)} self-center`}>
                    {getSuitSymbol(suit)}
                </div>
                <div className={`text-xl font-bold ${getColor(suit)} rotate-180`}>
                    {value}
                </div>
            </div>
        </div>
    );
};

export default Card; 