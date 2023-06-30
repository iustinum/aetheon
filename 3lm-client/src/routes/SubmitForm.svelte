<script>
	import Select from 'svelte-select';

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
</script>

<div class="form-container">
	<Select class="dropdown" bind:value={selectedOption} {options} placeholder="Select an option" />
	<input type="text" bind:value={websiteLink} placeholder="Enter website link" />
	<button class="submit-button" on:click={handleSubmit}>Submit</button>
</div>

<style>
	.form-container {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 300px;
	}

	.dropdown {
		width: 50%;
		margin-right: 10px;
	}

	.submit-button {
		width: 50%;
	}

	.form-container {
		display: flex;
		align-items: center;
		justify-content: space-between;
		width: 300px;
	}

	.dropdown {
		width: 50%;
		margin-right: 10px;
		flex-grow: 1;
	}

	.submit-button {
		width: 50%;
		flex-grow: 1;
		margin-left: 10px;
	}
</style>
