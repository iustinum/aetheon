<script>
  import SubmitFormBasic from './submitFormBasic.svelte';

  const handleSubmit = (result) => {
    console.log('HELLO FROM +PAGE', result);
  };
</script>

<div class="content-container">
  <h1 class="text-3xl font-bold">Submit Your Repository</h1>
</div>

<div class="content-container">
  <SubmitFormBasic onSubmit={handleSubmit} />
</div>
