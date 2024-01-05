import { error } from '@sveltejs/kit';
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
			`http://127.0.0.1:8000/urat-question-answer/?startup_id=${data.id}`,
			{
				method: 'get',
				headers: {
					Authorization: `Bearer ${cookies.get('Access')}`
				}
			}
		);

		const answers_data = await urat_answers.json();

		if (urat_answers.ok) {
			return {
				info: data,
				answers: answers_data.results,
			};
		}
	}

	throw error(404);
};