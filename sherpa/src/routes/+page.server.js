

/** @type {import('./$types').PageServerLoad} */
export async function load({ cookies }) {
	return {};
}


/** @type {import('./$types').Actions} */
export const actions = {
	subscribe: async (request) => {
		const data = await request.formData();
		console.log(data);

		fetch("http://127.0.0.1:8080/subscribe", {method: "POST"})
	}
};
