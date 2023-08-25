<script>
	import SubmitFormBasic from './submitFormBasic.svelte';

	const handleSubmit = (/** @type {{ githubLink: string; branch: string; }} */ result) => {
		console.log('HELLO FROM +PAGE', result);
	};
	let rand = 0;

	function getRand() {
		fetch('http://localhost:8080/test')
			.then((d) => {
				return d.text();
			})
			.then((d) => {
				console.log(d);
				rand = d;
			});
	}
</script>

<div class="content-container">
	<h1>Submit Your Repository</h1>
</div>

<div class="content-container">
	<SubmitFormBasic onSubmit={handleSubmit} />
</div>

<h1>Your number is {rand}!</h1>
<button on:click={getRand}>Get a random number</button>
