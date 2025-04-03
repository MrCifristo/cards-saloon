import React from 'react';

export default function WesternButton({ children, primary = false, onClick, className = '', fullWidth = false }) {
    return (
        <button
            onClick={onClick}
            className={`
                ${fullWidth ? 'w-full' : ''}
                py-3 px-6 rounded-lg font-western text-lg transition-colors
                ${primary 
                    ? 'bg-[#8b4513] hover:bg-[#a0522d] text-[#e6d5b8]' 
                    : 'bg-[#2a1810] hover:bg-[#3a2820] text-[#e6d5b8] border border-[#8b4513]'
                }
                ${className}
            `}
        >
            {children}
        </button>
    );
} 