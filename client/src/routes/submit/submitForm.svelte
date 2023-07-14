<form class="bg-white rounded border p-8 w-full">
	<legend>form</legend>

	<div class="mb-6">
		<label class="block text-gray-700 text-sm font-bold mb-2" for="github-link">
			Github Link
		</label>
		<input
			class=" appearance-none border rounded w-full p-2 bg-gray-200 text-gray-700 leading-tight focus:shadow-outline focus:outline-none focus:bg-white"
			id="github-link"
			type="text"
			placeholder="https://github.com/username/repositoryname"
		/>
	</div>

	<div class="flex flex-wrap justify-between">
		<div class="w-full min-[320px]:w-1/3 mb-6 min-[320px]:mb-0">
			<label class="block text-gray-700 text-sm font-bold mb-2" for="branch"> Branch </label>
			<div class="relative">
				<select
					class="w-full appearance-none border rounded p-2 text-gray-700 leading-tight cursor-pointer"
					id="branch"
				>
					<option>main</option>
					<option>deez</option>
					<option>test</option>
				</select>
				<div
					class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
				>
					<svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"
						><path
							d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
						/></svg
					>
				</div>
			</div>
		</div>

		<div class="w-full min-[320px]:w-1/3 mb-6 min-[320px]:mb-0 flex justify-end">
			<button
				class="bg-gray-700 hover:bg-gray-500 text-white font-bold p-2 rounded focus:outline-none focus:shadow-outline inline-block self-end"
				type="button"
			>
				Submit
			</button>
		</div>
	</div>
</form>

<!-- <form class="w-full max-w-lg">
	<div class="flex flex-wrap -mx-3 mb-6">
		<div class="w-full px-3">
			<label
				class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
				for="github-link"
			>
				Github Link
			</label>
			<input
				class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
				id="github-link"
				type="text"
				placeholder="https://github.com/username/repositoryname"
			/>
		</div>
	</div>

	<div class="flex flex-wrap -mx-3 mb-2">
		<div class="w-full md:w-1/3 px-3 mb-6 md:mb-0">
			<label
				class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
				for="grid-city"
			>
				City
			</label>
			<input
				class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
				id="grid-city"
				type="text"
				placeholder="Albuquerque"
			/>
		</div>
		<div class="w-full md:w-1/3 px-3 mb-6 md:mb-0">
			<label
				class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
				for="grid-state"
			>
				State
			</label>
			<div class="relative">
				<select
					class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
					id="grid-state"
				>
					<option>New Mexico</option>
					<option>Missouri</option>
					<option>Texas</option>
				</select>
				<div
					class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
				>
					<svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"
						><path
							d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
						/></svg
					>
				</div>
			</div>
		</div>
		<div class="w-full md:w-1/3 px-3 mb-6 md:mb-0">
			<label
				class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
				for="grid-zip"
			>
				Zip
			</label>
			<input
				class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
				id="grid-zip"
				type="text"
				placeholder="90210"
			/>
		</div>
	</div>
</form> -->
