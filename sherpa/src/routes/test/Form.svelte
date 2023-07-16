<script>
	import Form from './Form.svelte';
	import Input from './Input.svelte';
	import Select from './Select.svelte';
	import Button from './Button.svelte';
	
	export let data = {};
	export let onSubmit = () => {};

	let name = data.name ?? '';
	let length = data.length ?? 20;
	let type = data.type ?? 'original';
	let errors = {};
	let touchedFields = {};
	
	$: result = {
		name, length, type
	};
	
	$: errors = validate(touchedFields, result);

	const validate = () => {
		const errors = {};
		if (touchedFields.name && name === '') {
			errors.name = 'Name is required';
		}
		if (touchedFields.length && length < 5) {
			errors.length = 'Length should be at least 5';
		}
		if (touchedFields.type && touchedFields.length && type === 'original' && length >= 10 && length <= 20) {
			errors.type = 'For type "original" length should not be between 10 and 20';
		}
		return errors;
	};
	
	const validateAndSubmit = () => {
		touchedFields = { name: true, length: true, type: true };
		if (!Object.keys(errors).length) {
			onSubmit(result);
		}
	};
</script>

<div class="form">
	<fieldset class="fieldset">
		<legend>form</legend>
		<Input
			type="text"
			label="Name"
			bind:value={name}
			on:blur={() => touchedFields.name = true}
			error={errors.name}
		/>
		<Input
			type="number"
			label="Length"
			bind:value={length}
			on:blur={() => touchedFields.length = true}
			error={errors.length}
		/>
		<Select
			label="Type"
			bind:value={type}
			on:blur={() => touchedFields.type = true}
			error={errors.type}
		>
			<option value="original">Original</option>
			<option value="refubrished">Refubrished</option>
		</Select>
		<Button on:click={validateAndSubmit}>Submit</Button>
		<div>
			<pre>
				{JSON.stringify(result, null, 2)}
			</pre>
		</div>
	</fieldset>
</div>


<style>
	.fieldset > * {
		display: block;
	}
	
	.fieldset > :global(:not(legend) + *) {
		margin-top: 16px;
	}
	
	.fieldset {
		border: 1px solid #ddd;
		border-radius: 4px;
		padding: 20px;
	}
</style>