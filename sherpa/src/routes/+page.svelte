<script>
	import { getContext } from 'svelte';

	const pages = getContext('pages');
</script>

{#each Object.entries(pages) as [id, Elem]}
	<a {id} />
	<Elem />
{/each}
