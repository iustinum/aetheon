<script>
	let codeInput = '';
</script>

<div class="page text-content h-90vh">
	<h1>Demo:</h1>
	<p>instructions (insert code and then click button)</p>

	<textarea
		bind:value={codeInput}
		tabindex="-1"
		class="code-editor"
		placeholder="Write your code here..."
	/>

	<button>Document</button>

	<div class="output">asdf</div>
	<!-- <div class="code-container">
	</div> -->
</div>

<style>
	.output, .code-editor  {
		padding: 10px;
		background-color: #2d2d2d;
		color: #ffffff;
		font-family: 'Courier New', monospace;
		font-size: 14px;
		line-height: 1.5;
		border: none;
		width: 100%;
		height: 40%;
	}
</style>
