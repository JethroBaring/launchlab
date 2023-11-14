import { redirect } from "@sveltejs/kit";

export const actions = {
    default: ({cookies}) => {
        cookies.set('Access', '', {
            path:'/',
            expires: new Date(0)
        })

        cookies.set('Refresh', '', {
            path:'/',
            expires: new Date(0)
        })

        throw redirect(302, '/')
    }
}