import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad =async ({params}) => {
    return {
        params: params.applicant
    }
}