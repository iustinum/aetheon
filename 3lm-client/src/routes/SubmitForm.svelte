<!-- This is a submit form with a drop down menu on top, then a place to input a website link below, then a submit button on the bottom -->
<!-- <script>

	let selectedOption = '';
	let websiteLink = '';

	const options = [
		{ value: 'Option 1', label: 'Option 1' },
		{ value: 'Option 2', label: 'Option 2' },
		{ value: 'Option 3', label: 'Option 3' }
	];

	function handleSubmit() {
		// Handle form submission here
		console.log('Selected option:', selectedOption);
		console.log('Website link:', websiteLink);
	}
</script> -->

<!-- <div class="">
	<select bind:value={selectedOption} placeholder="Select an option" />
	<input type="text" bind:value={websiteLink} placeholder="Enter website link" />
	<button on:click={handleSubmit}>Submit</button>
</div> -->
<script>
	let options = [
		{ id: 1, text: `branch1` },
		{ id: 2, text: `branch2` },
		{ id: 3, text: `branch3` }
	];

	let selected = options[0];

	let answer = '';

	function handleSubmit() {
		alert(`answered question ${selected.id} (${selected.text}) with "${answer}"`);
	}
</script>

<form class="flex flex-col justify-center gap-{8}" on:submit|preventDefault={handleSubmit}>
	<input class="outline-1 outline" bind:value={answer} placeholder="github link" />

	<select bind:value={selected} on:change={() => (answer = '')}>
		{#each options as option}
			<option value={option}>
				{option.text}
			</option>
		{/each}
	</select>

	<button class="outline outline-offset-2 outline-2" disabled={!answer} type="submit">
		Submit
	</button>
</form>
<!-- 
<div class="flex flex-col justify-center gap-{8}">
	<input type="text" bind:value={websiteLink} placeholder="Enter website link" />
	<select bind:value={selectedOption} placeholder="Select an option" />
	<button on:click={handleSubmit}>Submit</button>
</div> -->
