<script>
	const questions = [
		{ q: 'asfdasdf', a: 'ansawerewer heheheheheeh' },
		{ q: 'asfdasdf2', a: 'ansawerewer heheheheheeh2' },
		{ q: 'asfdasdf3', a: 'ansawerewer heheheheheeh3' }
	];
</script>

<div class="page text-content bg-gray-400 rounded">
	<h1 class="text-center">WAITLIST</h1>

	<form action="subscribe" method="post">
		<label>
			input1
			<input name="input1" type="input1" />
		</label>
		<label>
			input2
			<input name="input2" type="input2" />
		</label>
		<button>Log in</button>
	</form>
</div>

<div class="page text-content">
	<h1>q&a !!</h1>
	<br class="block" />

	{#each questions as { q, a }, i (i)}
		<h3 class="">Q: {q}</h3>
		<p>A: {a}</p>
		<br class="block" />
	{/each}
</div>
