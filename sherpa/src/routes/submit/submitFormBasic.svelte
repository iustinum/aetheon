<script>
  let githubLink = '';
  let branch = '';

  export let onSubmit = (/** @type {{ githubLink: string; branch: string; }} */ res) => {

  };

  $: result = {
    githubLink,
    branch
  };

  const validateAndSubmit = () => {
    onSubmit(result);
  };
</script>

<form action="post">
  <input
    class="border rounded"
    type="text"
    id="github-link"
    bind:value={githubLink}
    placeholder="https://github.com/username/repositoryname"
  />

  <select class="border rounded" name="branch" id="branch" bind:value={branch}>
    <option>main</option>
    <option>deez</option>
    <option>test</option>
  </select>

  <button
    class="bg-gray-700 hover:bg-gray-500 text-white rounded"
    type="button"
    on:click={validateAndSubmit}
  >
    Submit
  </button>
</form>

<div>
  <pre>
    {JSON.stringify(result, null, 2)}
  </pre>
</div>
