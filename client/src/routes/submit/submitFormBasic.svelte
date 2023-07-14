<script>
  // @ts-ignore
  function handleSubmit(e) {
    console.log(e);
  }
</script>

<form action="post">
  <label for="github-link">
    <input
      class="border rounded"
      type="text"
      id="github-link"
      placeholder="https://github.com/username/repositoryname"
    />
  </label>

  <label for="branch">
    <select class="border rounded" name="branch" id="branch">
      <option>main</option>
      <option>deez</option>
      <option>test</option>
    </select>
  </label>

  <button class="bg-gray-700 hover:bg-gray-500 text-white rounded" type="button"> Submit </button>
</form>
