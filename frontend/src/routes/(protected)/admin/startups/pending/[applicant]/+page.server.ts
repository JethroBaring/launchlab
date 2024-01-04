import { error, redirect } from '@sveltejs/kit';
import type { PageServerLoad } from '../$types';

export const load: PageServerLoad = async ({ params, fetch, cookies }) => {
	const response = await fetch(`http://127.0.0.1:8000/startups/${params.applicant}/`, {
		method: 'get',
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${cookies.get('Access')}`
		}
	});

	const data = await response.json();
	if (response.ok) {
		const anotherResponse = await fetch(
			`http://127.0.0.1:8000/startups/${params.applicant}/retrieve-initial-readiness-level/`,
			{
				method: 'get',
				headers: {
					Authorization: `Bearer ${cookies.get('Access')}`
				}
			}
		);

		const anotherData = await anotherResponse.json();

		if (anotherResponse.ok) {
			return {
				info: data,
				response: anotherData,
				params: params.applicant,
				access: cookies.get('Access')
			};
		}
	}

	throw error(404);
};

export const actions = {
	approve: async ({ cookies, params }) => {
		const response = await fetch(
			`http://127.0.0.1:8000/startups/${params.applicant}/approve-applicant/`,
			{
				method: 'post',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${cookies.get('Access')}`
				}
			}
		);

		if (response.ok) {
			throw redirect(302, '/admin/startups/applicants');
		} else {
			console.log(response.statusText);
			throw redirect(302, '/admin/startups/applicants');
		}
	},
	reject: async ({ cookies, params }) => {
		const response = await fetch(
			`http://127.0.0.1:8000/startups/${params.applicant}/reject-applicant/`,
			{
				method: 'post',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${cookies.get('Access')}`
				}
			}
		);

		if (response.ok) {
			return {
				message: 'email has been sent to the applicant'
			};
		} else {
			console.log(response.statusText);
			throw redirect(302, '/admin/startups/applicants');
		}
	}
};
