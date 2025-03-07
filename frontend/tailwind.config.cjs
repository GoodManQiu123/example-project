/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        // sans: ['Consolas', 'Arial', 'sans-serif'],
      },
      colors: {
        primary: {
          DEFAULT: '#154ec1',
        },
        blue: {
          DEFAULT: '#60a5fa',
        },
        yellow: {
          DEFAULT: '#fcd34d',
        },
        red: {
          DEFAULT: '#ef4444',
        },
        purple: {
          DEFAULT: '#d946ef',
        },
        green: {
          DEFAULT: '#4ade80',
        },
      }
    },
    screens: {
      xs: '0px',
      sm: '576px',
      md: '768px',
      lg: '992px',
      xl: '1200px',
    },
  },
  plugins: [],
}
