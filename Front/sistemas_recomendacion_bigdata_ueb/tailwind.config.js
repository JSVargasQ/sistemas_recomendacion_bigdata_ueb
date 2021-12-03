module.exports = {
  purge: [],
  mode: 'jit',
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    boxShadow: ['responsive', 'hover', 'focus'],
    extend: {
      backgroundColor: ['hover'],
    },
  },
  plugins: [],
  pure_getters: [
    './public/**/*.html',
    './src/**/*.{js,jsx,ts,tsx,vue}',
  ]
}
