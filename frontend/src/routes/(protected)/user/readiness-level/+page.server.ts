import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch, cookies }) => {
	const response = await fetch(`http://127.0.0.1:8000/startups/`, {
		method: 'get',
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${cookies.get('Access')}`
		}
	});

	const data = await response.json();
	if (response.ok) {
		const rubrics = await fetch('http://127.0.0.1:8000/readinesslevel/readiness-levels/', {
			method: 'get',
			headers: {
				Authorization: `Bearer ${cookies.get('Access')}`
			}
		});

		const rubrics2 = await fetch('http://127.0.0.1:8000/readinesslevel/readiness-levels/?page=2', {
			method: 'get',
			headers: {
				Authorization: `Bearer ${cookies.get('Access')}`
			}
		});

		const haveScores = await fetch(`http://127.0.0.1:8000/readiness-level-criterion-answers/?page_size=324&startup_id=${parseInt(data.results[0].id)}`, {
			method: 'get',
			headers: {
				Authorization: `Bearer ${cookies.get('Access')}`
			}
		})

		const rubrics_data = await rubrics.json();
		const rubrics2_data = await rubrics2.json();
		const scores_data = await haveScores.json()

		return {
			questions: rubrics_data.results.concat(rubrics2_data.results),
			scores: scores_data.results
		};
	}

	throw error(404);
};
