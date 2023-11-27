import type { PageServerLoad } from './$types';
import { redirect } from "@sveltejs/kit";

export const load: PageServerLoad = async ({ locals , cookies}) => {
    if(!locals.user) {
        throw redirect(302, '/')
    }

    if(locals.user.type !== 'S') {
        throw redirect(302, '/admin/home')
    }

    const response = await fetch(`http://127.0.0.1:8000/startups/${locals.user.startupId}/`, {
        method: 'get',
        headers: {
            'Content-type': 'application/json',
            Authorization: `Bearer ${cookies.get('Access')}`
        }
    })

    if(response.ok) {
        return {
            user: locals.user,
            access: cookies.get('Access'),
            hasAnswered: await response.json()
        }
    }

    return {
        user: locals.user,
        access: cookies.get('Access')
    }
};
