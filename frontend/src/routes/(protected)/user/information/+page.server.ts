import { error } from "@sveltejs/kit";
import type { PageServerLoad } from "./$types";

export const load: PageServerLoad =async ({cookies, fetch}) => {
    const response = await fetch('http://127.0.0.1:8000/startups/', {
        method: 'get',
        headers: {
            Authorization: `Bearer ${cookies.get('Access')}`
        }
    })

    const data = await response.json()
    if(response.ok) {
        return {
            info: data.results[0]
        }
    }

    throw error(404);
}