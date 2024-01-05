import { error, fail, redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch }) => {
	const uratQuestions = await fetch('http://127.0.0.1:8000/readinesslevel/urat-questions/')

	const data = await uratQuestions.json()
	if(uratQuestions.ok) {
		return {
			technologyQuestions: data.results.filter((d) => d.readiness_type === "Technology"),
			marketQuestions: data.results.filter((d) => d.readiness_type === "Market"),
			acceptanceQuestions: data.results.filter((d) => d.readiness_type === "Acceptance"),
			organizationalQuestions: data.results.filter((d) => d.readiness_type === "Organizational"),
			regulatoryQuestions: data.results.filter((d) => d.readiness_type === "Regulatory"),
			investmentQuestions: data.results.filter((d) => d.readiness_type === "Investment"),

		}
	}
};

export const actions = {
	application: async ({ request, fetch }) => {
		const formData = await request.formData();

		if (
			!Object.values(formData)
				.filter((key) => key !== 'links' && key !== 'university_name')
				.every((value) => value !== undefined && value !== null && value !== '')
		) {
			return fail(400, { credentials: true });
		}
		const newFormData = new FormData();
		const members = ['member_2_email', 'member_3_email', 'member_4_email', 'member_5_email'];

		newFormData.append('data_privacy', formData.get('data_privacy') as string);
		newFormData.append('name', formData.get('name') as string);
		newFormData.append('capsule_proposal', formData.get('capsule_proposal') as File);
		newFormData.append('links', formData.get('links') as string);
		newFormData.append('group_name', formData.get('group_name') as string);
		newFormData.append('member_1_name', formData.get('member_1_name') as string);
		newFormData.append('member_1_number', formData.get('member_1_number') as string);
		newFormData.append('member_1_email', formData.get('member_1_email') as string);
		newFormData.append('university_name', formData.get('university_name') as string);
		newFormData.append('eligibility', formData.get('eligibility') as string);

		for (let i = 0; i < members.length; i++) {
			if (formData.get(`${members[i]}`) !== null) {
				newFormData.append('set_members', formData.get(`${members[i]}`) as string);
			}
		}

		const response = await fetch('http://127.0.0.1:8000/startups/', {
			method: 'post',
			body: newFormData
		});

		if (response.ok) {
			const data = await response.json();
			const startupId = data.id;
			
			const types = ["technology","market","acceptance", "organizational", "regulatory", "investment"]

			await Promise.all(types.map(async (type) => {
				for(let i = 0; i < 3; i++) {
					await fetch('http://127.0.0.1:8000/urat-question-answer/', {
						method: 'post',
						headers: {
							'Content-type': 'application/json'
						},
						body: JSON.stringify({
							startup_id: startupId,
							urat_question_id: formData.get(`${type}${i}id`),
							response: formData.get(`${type}${i}`)
						})
					})
				}
			})).then(values => {
				console.log(values)
				throw redirect(302, '/emailsent');
			}).catch(error => {
				console.log(error)
				return fail(400, { credentials: true });
			})
		}

	}
};
