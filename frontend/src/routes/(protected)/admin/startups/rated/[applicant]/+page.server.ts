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

		const urat_answers = await fetch(
			`http://127.0.0.1:8000/urat-question-answers/?startup_id=${data.id}`,
			{
				method: 'get',
				headers: {
					Authorization: `Bearer ${cookies.get('Access')}`
				}
			}
		);

		const answers_data = await urat_answers.json();
		
		const mentor = await fetch('http://127.0.0.1:8000/user/?user_type=ME', {
			method: 'get',
				headers: {
					Authorization: `Bearer ${cookies.get('Access')}`
				}
		})

		const mentor_data = await mentor.json()

		const calculator = await fetch(`http://127.0.0.1:8000/startups/${params.applicant}/calculator-final-scores/`, {
			method: 'get',
				headers: {
					Authorization: `Bearer ${cookies.get('Access')}`
				}
		})

		const calculator_data = await calculator.json()

		if (urat_answers.ok && mentor.ok && calculator.ok) {
			return {
				info: data,
				answers: answers_data.results,
				mentors: mentor_data.results,
				calculator: calculator_data
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
			throw redirect(302, `/admin/startups/qualified/${params.applicant}`);
		} else {
			console.log(response.statusText);
			throw redirect(302, `/admin/startups/pending/${params.applicant}`);
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
	},
};
