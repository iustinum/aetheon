<script>
	import { getContext } from 'svelte';

	const pages = getContext('pages');
</script>

{#each Object.entries(pages) as [id, Elem]}
	<!-- svelte-ignore a11y-missing-content -->
	<a {id} />
	<Elem />
{/each}
