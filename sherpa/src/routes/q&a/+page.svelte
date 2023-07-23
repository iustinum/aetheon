<script>
  const questions = [
    { q: 'asfdasdf', a: 'ansawerewer heheheheheeh' },
    { q: 'asfdasdf2', a: 'ansawerewer heheheheheeh2' },
    { q: 'asfdasdf3', a: 'ansawerewer heheheheheeh3' }
  ];
</script>

<div class="content-container">
  <h1>q&a !!</h1>
  <br />

  {#each questions as { q, a }, i (i)}
    <h3 class="">Q: {q}</h3>
    <p>A: {a}</p>
    <br />
  {/each}
</div>
