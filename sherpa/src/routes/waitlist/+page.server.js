/** @type {import('./$types').PageServerLoad} */
export async function load({ cookies }) {
	return {};
}
/** @type {import('./$types').Actions} */
export const actions = {
	subscribe: async ({ request }) => {
		const data = await request.formData();
		console.log(data);
	}
};
