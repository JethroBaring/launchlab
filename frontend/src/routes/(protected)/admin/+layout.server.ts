import { redirect } from "@sveltejs/kit";
import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad =async ( {locals}) => {
    if(!locals.user) {
        throw redirect(302, '/')
    }

    if(locals.user.type !== 'M') {
        throw redirect(302, '/user/home')
    }

    return {
        user: locals.user
    }
}