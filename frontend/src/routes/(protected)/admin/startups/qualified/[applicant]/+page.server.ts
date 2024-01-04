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
		const anotherResponse = await fetch(
			`http://127.0.0.1:8000/startups/${params.applicant}/retrieve-initial-readiness-level/`,
			{
				method: 'get',
				headers: {
					Authorization: `Bearer ${cookies.get('Access')}`
				}
			}
		);

		const anotherData = await anotherResponse.json()

		if(anotherResponse.ok) {
			return {
				info: data,
				readiness: anotherData
			}
		}
	}

	throw error(404);
};