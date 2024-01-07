import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals }) => {
	if (locals.user) {
		if(locals.user.type === "S")
			throw redirect(302, '/user/home');
		else if(locals.user.type === "M")
			throw redirect(302, '/admin/startups/pending');
		else
			throw redirect(302, '/mentor/startups/qualified')
	}
};
