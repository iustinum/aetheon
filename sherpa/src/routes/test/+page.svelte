<script>
	let rand = 0;

	function getRand() {
		fetch('http://localhost:5000/test')
			.then((d) => {
				return d.text();
			})
			.then((d) => {
				console.log(d);
				rand = d;
			});
	}
</script>

<h1>Your number is {rand}!</h1>
<button on:click={getRand}>Get a random number</button>
