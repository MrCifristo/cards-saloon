/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'western': {
          'dark': '#1a1a1a',
          'light': '#f5f5f5',
          'brown': '#8B4513',
          'brown-dark': '#6B2C0F',
          'red': '#B22222',
          'red-dark': '#8B0000',
          'green': '#228B22',
          'green-dark': '#006400',
          'gold': '#DAA520',
          'border': '#D2B48C',
          'card': '#2C1810',
          'input': '#3C2810',
          'table': '#1E130C',
        },
      },
      fontFamily: {
        'western': ['Playfair Display', 'serif'],
      },
      backgroundImage: {
        'western-pattern': "url('/src/assets/images/wood-pattern.png')",
        'western-card-back': "url('/src/assets/images/card-back.png')",
      },
    },
  },
  plugins: [],
} 