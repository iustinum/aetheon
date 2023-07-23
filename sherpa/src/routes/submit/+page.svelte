<script>
  import SubmitFormBasic from './submitFormBasic.svelte';

  const handleSubmit = (/** @type {{ githubLink: string; branch: string; }} */ result) => {
    console.log('HELLO FROM +PAGE', result);
  };
</script>

<div class="content-container">
  <h1>Submit Your Repository</h1>
</div>

<div class="content-container">
  <SubmitFormBasic onSubmit={handleSubmit} />
</div>
