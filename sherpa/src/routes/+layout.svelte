<script>
  import "../app.css"
  // import "../font.css"
  const options = ['blog', 'q&a', 'waitlist'];
</script>

<nav class="text-black border">
  <div class="container mx-auto p-4 flex justify-between items-center max-w-4xl">
    <a href="." class="text-xl font-bold">3LM</a>
    <ul class="space-x-4">
      {#each options as option (option)}
        <li class="inline-block"><a href={option}>{option}</a></li>
      {/each}
    </ul>
  </div>
</nav>

<div class="main flex items-center flex-col p-10">
  <slot />
</div>


