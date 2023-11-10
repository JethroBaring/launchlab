/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        'flutter-blue': '#1C83E5',
        'flutter-dark': '#0B213E'
      },
      fontFamily: {
        'Inter': ['Inter', 'sans-serif']
      },
      boxShadow: ['dark'],
      flex: {
        '2' : '0 0 auto'
      }
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light", "dark", "winter"],
  },
}

