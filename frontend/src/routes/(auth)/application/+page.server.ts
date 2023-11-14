import { fail, redirect } from '@sveltejs/kit';

export const actions = {
	application: async ({ request, fetch }) => {
		const formData = await request.formData();
		console.log(formData);
		if (
			!Object.values(await formData).every(
				(value) => value !== undefined && value !== null && value !== ''
			)
		)
			return fail(400, { credentials: true });

		const response = await fetch('http://127.0.0.1:8000/applicants/', {
			method: 'post',
			body: formData
		});

		if (response.ok) {
			throw redirect(302, '/emailsent');
		}

		return fail(400, { credentials: true });
	}
};
