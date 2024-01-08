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
        const mentor = await fetch(`http://127.0.0.1:8000/startups/${data.results[0].id}/mentors/`, {
            method: 'get',
            headers: {
                Authorization: `Bearer ${cookies.get('Access')}`
            }
        })

        const m = await mentor.json()
        if(mentor.ok) {
            return {
                info: data.results[0],
                mentor: m
            }
        }
    }

    throw error(404);
}