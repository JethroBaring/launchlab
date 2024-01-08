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
		const urat_questions = await fetch('http://127.0.0.1:8000/readinesslevel/urat-questions/', {
			method: 'get',
			headers: {
				Authorization: `Bearer ${cookies.get('Access')}`
			}
		});

		const questions_data = await urat_questions.json();

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

		if (urat_questions.ok && urat_answers.ok) {
			return {
				info: data,
				questions: questions_data.results,
				answers: answers_data.results,
				access: cookies.get('Access')
			};
		}
	}

	throw error(404);
};

export const actions = {
	rate: async ({ cookies, params }) => {
		const response = await fetch(
			`http://127.0.0.1:8000/startups/${params.applicant}/rate-applicant/`,
			{
				method: 'post',
				headers: {
					'Content-type': 'application/json',
					Authorization: `Bearer ${cookies.get('Access')}`
				}
			}
		);

		if (response.ok) {
			throw redirect(302, `/admin/startups/rated/${params.applicant}`);
		}
	}
};
