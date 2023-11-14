export const load = async ( { cookies} ) => {
    const token = cookies.get('refreshToken')
    const access = cookies.get('accessToken')
    return {
        tokens : {
            refresh: token,
            access: access
        }
    }
}