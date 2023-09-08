<script>
	let codeInput = '';
	let codeOutput = "";

	async function changeOutput() {

		const data = { codeInput };

		// Make the POST request
		try {
			const response = await fetch('http://127.0.0.1:8080/prompt', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(data)
			});

			if (response.ok) {
				console.log('POST request successful', response);
				// Reset the input after successful submission
				response.json().then((data) => {
					codeOutput =  JSON.stringify(data)}
				)
			} else {
				console.error('POST request failed');
				codeOutput = "something went wrong";

			}
		} catch (error) {
			console.error('Error sending POST request:', error);
		}
	}
</script>

<div class="page text-content h-90vh">
	<h1>Demo:</h1>
	<p>instructions (insert code and then click button)</p>

	<textarea
		bind:value={codeInput}
		tabindex="-1"
		class="code-editor"
		placeholder="Write your code here..."
	/>

	<button on:click={changeOutput}>Document</button>

	<div class="output" >{codeOutput}</div>
</div>

<style>
	.output, .code-editor  {
		padding: 10px;
		background-color: #2d2d2d;
		color: #ffffff;
		font-family: 'Courier New', monospace;
		font-size: 14px;
		line-height: 1.5;
		border: none;
		width: 100%;
		height: 20%;
	}
</style>
