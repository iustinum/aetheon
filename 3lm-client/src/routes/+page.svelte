<script>
	import SubmitForm from './SubmitForm.svelte';
</script>

<nav class="text-black">
	<div class="container mx-auto px-4 py-2 flex justify-between items-center">
		<div class="text-xl font-bold">Logo</div>
		<ul class="space-x-4">
			<li class="inline-block"><a href="." class="hover:text-gray-300">Home</a></li>
			<li class="inline-block"><a href="." class="hover:text-gray-300">About</a></li>
		</ul>
	</div>
</nav>

<!-- main -->
<div class="flex justify-center p-10">
	<!-- wrapper class for submit form: -->
	<div class="max-w-md w-full p-4 sm:p-6"> 
		<SubmitForm />
	</div>
</div>
