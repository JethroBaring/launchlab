import type { PageServerLoad } from "./$types";

export const load: PageServerLoad =async ({fetch, cookies}) => {
    const response = await fetch('http://127.0.0.1:8000/startups/', {
        method: 'get',
        headers: {
            Authorization: `Bearer ${cookies.get('Access')}`
        }
    })
    const data = await response.json()

    if(response.ok) {
        const anotherResponse = await fetch('http://127.0.0.1:8000/startups?is_qualified=true', {
            method: 'get',
            headers: {
                Authorization: `Bearer ${cookies.get('Access')}`
            }
        })

        if(anotherResponse.ok) {
            const anotherData = await anotherResponse.json()
            return {
                applicants: data.results,
                qualified: anotherData.results
            }
        }
    }
}