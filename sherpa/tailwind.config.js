/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				// https://tailwindcolor.com/
				mainpallet: {
					900: '#18181B',
					800: '#27272A',
					400: '#A1A1AA',
					200: '#E4E4E7'
				},
				accent: {
					900: '#164E63'
				}
			},
			spacing: {
				'90vh': '88vh',
				'94vh': '94vh',
			  }
		}
	},
	plugins: []
};
