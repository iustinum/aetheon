

<script>
	import '../app.css';
	import { setContext } from 'svelte';


	import Home from './home.svelte';
	import QAndA from './q&a.svelte';
	import Waitlist from './waitlist.svelte';
	import Demo from './demo.svelte';

	const pages = {
		"home": Home,
		"demo": Demo,
		"waitlist": Waitlist,
		"q&a": QAndA,
	}

	setContext("pages", pages)



	const links = [
		// { name: 'blog', link: '/blog' },
		{ name: 'demo', link: '/#demo' },
		{ name: 'waitlist', link: '/#waitlist' },
		{ name: 'q&a', link: '/#q&a' },
	];


</script>

<nav class="sticky top-0 z-50 bg-neutral-800 ">
	<div class="container mx-auto p-2 flex justify-between items-center max-w-3xl md:mt-10vh md:px-0">
		<div id="logo-wrap">
			<a href="." class="text-xl font-bold" id="logo">aetheon</a>
			<span>&nbsp&nbsp</span>
			<a href="/blog">blog</a>
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

<footer class="max-w-3xl w-full mx-auto md:py-8">
	<br class="block" />
	<br class="block" />
	<hr class=" my-6 border-neutral-200 sm:mx-auto dark:border-neutral-700 lg:my-8" />
	<span class="block text-sm text-neutral-400 sm:text-center dark:text-neutral-400"
		>© 2023 Aetheon. All Rights Reserved.</span
	>
</footer>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Cypro+Minoan&family=Space+Grotesk:wght@700&display=swap');

	@font-face {
		font-family: 'Arial Black';
		src: url('/fonts/ariblk.ttf');
	}
</style>
