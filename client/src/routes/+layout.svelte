<script>
  import '../app.css';
</script>

<nav class="text-black border">
  <div class="container mx-auto p-4 flex justify-between items-center">
    <a href="." class="text-xl font-bold">3LM</a>
    <ul class="space-x-4">
      <li class="inline-block"><a href=".">Settings</a></li>
      <li class="inline-block"><a href=".">Login/User</a></li>
    </ul>
  </div>
</nav>

<div class="flex items-center flex-col p-10">
  <slot />
</div>

<style>
</style>
