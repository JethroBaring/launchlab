import { error, redirect } from '@sveltejs/kit';
import type { PageServerLoad } from '../$types';

export const load: PageServerLoad = async ({ params, fetch, cookies }) => {
	const response = await fetch(`http://127.0.0.1:8000/applicants/${params.applicant}/`, {
		method: 'get',
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${cookies.get('Access')}`
		}
	});

	const data = await response.json();
	if (response.ok) {
		return {
			info: data,
			params: params.applicant
		};
	}

	throw error(404);
};

export const actions = {
	approve: async ({ cookies, params }) => {
		const response = await fetch(
			`http://127.0.0.1:8000/applicants/${params.applicant}/approve-applicant/`,
			{
				method: 'post',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${cookies.get('Access')}`
				}
			}
		);

		if (response.ok) {
			throw redirect(302, '/admin/dashboard/applicants')
		} else {
			console.log(response.statusText);
			throw redirect(302, '/admin/dashboard/applicants');
		}
	},
	reject: async ({ cookies, params }) => {
		const response = await fetch(
			`http://127.0.0.1:8000/applicants/${params.applicant}/reject-applicant/`,
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
			throw redirect(302, '/admin/dashboard/applicants');
		}
	}
};
