import { fail, redirect } from '@sveltejs/kit';
import generateMeta from '$lib/utils/openaiController.js';

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

			const initialAssessment = await fetch(
				`http://127.0.0.1:8000/startups/${data.id}/create-initial-readiness-level/`,
				{
					method: 'post',
					headers: {
						'Content-type': 'application/json'
					},
					body: JSON.stringify({
						irl_response: [
							formData.get('investment1'),
							formData.get('investment2'),
							formData.get('investment3')
						],
						trl_response: [
							formData.get('technology1'),
							formData.get('technology2'),
							formData.get('technology3')
						],
						orl_response: [
							formData.get('organizational1'),
							formData.get('organizational2'),
							formData.get('organizational3')
						],
						mrl_response: [
							formData.get('market1'),
							formData.get('market2'),
							formData.get('market3')
						],
						rrl_response: [
							formData.get('regulatory1'),
							formData.get('regulatory2'),
							formData.get('regulatory3')
						],
						arl_response: [
							formData.get('acceptance1'),
							formData.get('acceptance2'),
							formData.get('acceptance3')
						],
						irl: '1,1,1',
						trl: '1,1,1',
						orl: '1,1,1',
						mrl: '1,1,1',
						rrl: '1,1,1',
						arl: '1,1,1'
					})
				}
			);

			if (initialAssessment.ok) {
				const x = await generateMeta(
					formData.get('technology1') as string,
					formData.get('technology2') as string,
					formData.get('technology3') as string,
					formData.get('market1') as string,
					formData.get('market2') as string,
					formData.get('market3') as string,
					formData.get('regulatory1') as string,
					formData.get('regulatory2') as string,
					formData.get('regulatory3') as string,
					formData.get('acceptance1') as string,
					formData.get('acceptance2') as string,
					formData.get('acceptance3') as string,
					formData.get('organizational1') as string,
					formData.get('organizational2') as string,
					formData.get('organizational3') as string,
					formData.get('investment1') as string,
					formData.get('investment2') as string,
					formData.get('investment3') as string
				);

				if(x) {
					console.log(x)
					throw redirect(302, '/emailsent');
				}
			} else {
				console.log(initialAssessment);
			}
		}

		return fail(400, { credentials: true });
	}
};
