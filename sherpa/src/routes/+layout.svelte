<script>
	import '../app.css';
	const options = ['blog', 'q&a', 'waitlist'];
</script>

<nav>
	<div class="container mx-auto p-2 flex justify-between items-center max-w-3xl md:mt-16">
		<div id="logo-wrap">
			<a href="." class="text-xl font-bold" id="logo">aetheon</a>
		</div>
		<ul class="space-x-4">
			{#each options as option (option)}
				<li class="inline-block"><a href={option}>{option}</a></li>
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
