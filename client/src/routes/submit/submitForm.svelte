<div class="w-full">
	<form class="bg-white rounded border p-8">
		<div class="mb-4">
			<label class="block text-gray-700 text-sm font-bold mb-2" for="github-link">
				Github Link
			</label>
			<input
				class=" appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:shadow-outline"
				id="github-link"
				type="text"
				placeholder="https://github.com/username/repositoryname"
			/>
		</div>

		<div class="flex flex-wrap justify-between">
			<div class="w-full md:w-1/3 px-3 mb-6 md:mb-0">
				<label class="block text-gray-700 text-sm font-bold mb-2" for="branch"> Branch </label>
				<!-- 
                <input
                    class=" appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                    id="password"
                    type="password"
                    placeholder="******************"
                />
                <p class="text-red-500 text-xs italic">Please choose a password.</p> -->
				<select
					class="w-full appearance-none border rounded py-2 px-3 text-gray-700 leading-tight"
					id="branch"
				>
					<option>main</option>
					<option>deez</option>
					<option>test</option>
				</select>
			</div>

			<div class="w-full md:w-1/3 px-3 mb-6 md:mb-0 relative">
				<button
					class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded absolute bottom-0 right-0  focus:outline-none focus:shadow-outline"
					type="button"
				>
					Submit
				</button>
			</div>
            
		</div>
	</form>
</div>