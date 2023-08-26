<script>
	import '../app.css';
	// const options = {
	// 	"blog": 'asdf',
	// 	'q&a': 'asdf',
	// 	"waitlist": 'asdf'
	// };
	const links = [
		{ name: 'blog', link: '/blog' },
		{ name: 'q&a', link: '/#q&a' },
		{ name: 'waitlist', link: '/#waitlist' }
	];
</script>

<nav class="sticky top-0 z-50">
	<div
		class="container mx-auto p-2 flex justify-between items-center max-w-3xl md:mt-2"
	>
		<div id="logo-wrap">
			<a href="." class="text-xl font-bold" id="logo">aetheon</a>
		</div>
		<ul class="space-x-4">
			{#each links as { name, link } (name)}
				<li class="inline-block"><a href={link}>{name}</a></li>
			{/each}
		</ul>
	</div>
</nav>

<div class="main flex items-center flex-col">
	<slot />
</div>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Cypro+Minoan&family=Space+Grotesk:wght@700&display=swap');

	@font-face {
		font-family: 'Arial Black';
		src: url('/fonts/ariblk.ttf');
	}

	@font-face {
		font-family: 'Gresa';
		src: url('/fonts/GresaRegular.ttf');
	}
</style>
