<script>
  import Form from './Form.svelte';

  let data = { name: 'Rofl', length: 12, type: 'refubrished' };
  let submittedData = null;
</script>

<Form {data} onSubmit={(data) => (submittedData = data)} />

<div>
  <span>Submitted Data</span>
  <pre>
		{JSON.stringify(submittedData, null, 2)}
	</pre>
</div>
