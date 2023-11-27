import type { PageServerLoad } from "./$types";

export const load: PageServerLoad =async ({fetch, cookies, locals}) => {
    const response = await fetch(`http://127.0.0.1:8000/startups/${locals.user.startupId}/`, {
        method: 'get',
        headers: {
            Authorization: `Bearer ${cookies.get('Access')}`
        }
    })

    if(response.ok) {
        return {
            readiness: await response.json()
        }
    }
}