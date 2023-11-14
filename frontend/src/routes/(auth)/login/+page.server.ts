import { dev } from '$app/environment';
import { fail, redirect } from '@sveltejs/kit';

export const actions = {
	login: async ({ cookies, request , fetch}) => {
		const data = Object.fromEntries(await request.formData());

        const { email, password } = data

		const response = await fetch(`http://127.0.0.1:8000/tokens/acquire/`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ email, password })
		});

		const json = await response.json();

		if (response.status === 200) {
			cookies.set('Refresh', json.refresh, {
				path: '/',
				httpOnly: true,
				sameSite: 'strict',
				maxAge: 60 * 60 * 24,
				secure: !dev
			});

            cookies.set('Access', json.access, {
				path: '/',
				httpOnly: true,
				sameSite: 'strict',
				maxAge: 5 * 60,
				secure: !dev
			})
			console.log("success")
			throw redirect(302, '/');
		}
        
		return fail(400, { credentials: true, email: email});
	}
};
