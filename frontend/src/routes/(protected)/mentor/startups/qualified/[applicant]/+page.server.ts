import { error, fail, redirect } from '@sveltejs/kit';
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
		const rubrics = await fetch('http://127.0.0.1:8000/readinesslevel/readiness-level/', {
			method: 'get',
			headers: {
				Authorization: `Bearer ${cookies.get('Access')}`
			}
		});

		const rubrics2 = await fetch('http://127.0.0.1:8000/readinesslevel/readiness-level/?page=2', {
			method: 'get',
			headers: {
				Authorization: `Bearer ${cookies.get('Access')}`
			}
		});

		const rubrics_data = await rubrics.json();
		const rubrics2_data = await rubrics2.json();

		if (rubrics.ok) {
			return {
				info: data,
				questions: rubrics_data.results.concat(rubrics2_data.results),
				access: cookies.get('Access')
			};
		}
	}

	throw error(404);
};

export const actions = {
	technology: async ({ request, fetch, params, cookies }) => {
		const formData = await request.formData();
		const types = [
			'technology',
			'market',
			'acceptance',
			'organizational',
			'regulatory',
			'investment'
		];
		//console.log(formData)

		// for(let type = 0; type < 6; type++) {
		// 	console.log(types[type])
		// 	for(let level = 1; level <= 9; level++) {
		// 		for(let criteria = 1; criteria <= 6; criteria++) {
		// 			// console.log(`${types[type]}Criteria${level}${criteria}`)
		// 			// console.log(`${types[type]}${level}${criteria}`)
		// 			// console.log(`${types[type]}${level}${criteria}`)
		// 			console.log({
		// 				startup_id: params.applicant,
		// 				criterion_id: formData.get(`${types[type]}Criteria${level}${criteria}`),
		// 				score: formData.get(`${types[type]}${level}${criteria}`),
		// 				remark: formData.get(`${types[type]}Remark${level}${criteria}`)
		// 			})
		// 		}
		// 	}
		// }
		await Promise.all(
			types.map(async (type) => {
				for (let level = 1; level <= 9; level++) {
					for (let criteria = 1; criteria <= 6; criteria++) {
						const response = await fetch('http://127.0.0.1:8000/readiness-level-criterion-answer/', {
							method: 'post',
							headers: {
								'Content-type': 'application/json',
								Authorization: `Bearer ${cookies.get('Access')}`
							},
							body: JSON.stringify({
								startup_id: 123123,
								criterion_id: formData.get(`${type}Criteria${level}${criteria}`),
								score: formData.get(`${type}${level}${criteria}`),
								remark: formData.get(`${type}Remark${level}${criteria}`)
							})
						});

						if(response.ok) {
							console.log("ok")
						} else {
							console.log({
								startup_id: params.applicant,
								criterion_id: formData.get(`${type}Criteria${level}${criteria}`),
								score: formData.get(`${type}${level}${criteria}`),
								remark: formData.get(`${type}Remark${level}${criteria}`),
								criteria: type
							})
						}
					}
				}
			})
		)
			.then((values) => {
				console.log('hello values');
			})
			.catch((error) => {
				console.log(error)
				console.log("hello error");
				return fail(400, { credentials: true });
			});
	}
};
