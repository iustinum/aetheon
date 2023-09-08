<script>
	let email = '';

	async function handleSubmitSubscribe() {
		// Create the data object to send in the POST request
		const data = { email };

		// Make the POST request
		try {
			const response = await fetch('http://127.0.0.1:8080/subscribe', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(data)
			});

			if (response.ok) {
				console.log('POST request successful');
				// Reset the input after successful submission
				email = '';
			} else {
				console.error('POST request failed');
			}
		} catch (error) {
			console.error('Error sending POST request:', error);
		}
	}
</script>



<div>
	<div class="md:my-16 my-8 p-4 space-y-4 bg-neutral-400">
		<h1 class="text-center">Interested?</h1>
		<p>Subscribe if you want to become a tester, or if your just interested!</p>

		<form on:submit|preventDefault={handleSubmitSubscribe} class="text-center">
			<label>
				<input
					class="text-neutral-800 focus:border-none px-1"
					name="input1"
					type="email"
					placeholder="email@domain.com"
					bind:value={email}
				/>
			</label>
			<button class="bg-neutral-700 px-2">Join</button>
		</form>
	</div>
</div>
