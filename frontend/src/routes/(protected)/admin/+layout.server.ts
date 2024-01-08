import { redirect } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ locals }) => {
	if (!locals.user) {
		throw redirect(302, '/');
	}

	if (locals.user.type === 'ME') {
		throw redirect(302, '/mentor/startups/qualified');
	} else if (locals.user.type === 'S') {
		throw redirect(302, '/user/readiness-level');
	}

	return {
		user: locals.user
	};
};
