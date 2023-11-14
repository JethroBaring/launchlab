import type { Handle } from '@sveltejs/kit';
import jwt from 'jsonwebtoken';

export const handle: Handle = async ({ event, resolve }) => {
	//const cookies = event.cookies.getAll();
	// console.log('_____________________________________________________');
	// console.log(cookies);
	// console.log('_____________________________________________________');
	let access = event.cookies.get('Access');
	// try {
	// 	const decode = jwt.verify(access!, 'django-insecure-vak*mz%99+#882*g*87x8$%!r=trnnqd)zh2)i$w51ra4cd&eg');
	// } catch(err) {
	// 	console.log(err)
	// }
	if (!access) {
		try {
			const refresh = event.cookies.get('Refresh');
			if (!refresh) {
				return await resolve(event);
			}

			const response = await fetch('http://127.0.0.1:8000/tokens/refresh/', {
				method: 'POST',
				headers: {
					Authorization: `Bearer ${refresh}`,
					'Content-Type': 'application/json' // Add this line
				},
				body: JSON.stringify({
					refresh: refresh
				})
			});

			if (response.ok) {
				const data = await response.json();
				event.cookies.set('Access', data?.access, {
					path: '/',
					httpOnly: true,
					sameSite: 'strict',
					maxAge: 5 * 60
				});
				access = event.cookies.get('Access');
			} else {
				console.error('Request failed:', response.status, response.statusText);
			}
		} catch (error) {
			console.log('inside refresh');
			console.log(error);
		}
	}
	if (access) {
		try {
			console.log(access);
			const decoded = jwt.verify(
				access,
				'django-insecure-vak*mz%99+#882*g*87x8$%!r=trnnqd)zh2)i$w51ra4cd&eg'
			) as { user_id?: string };

			const response = await fetch(`http://127.0.0.1:8000/user/${decoded?.user_id}/`, {
				method: 'GET',
				headers: {
					Authorization: `Bearer ${access}`,
					'Content-Type': 'application/json' // Add this line
				}
			});
			if (response.ok) {
				const data = await response.json();
				event.locals.user = {
					id: Number.parseInt(decoded.user_id!),
					type: data?.user_type,
					email: data?.email,
					startupId: data?.startup_id,
					startupName: data?.startup_name,
					firstName: data?.first_name,
					lastName: data?.last_name
				};
				console.log(data)
				console.log('access token not expired');
			} else {
				console.error('Request failed:', response.status, response.statusText);
			}
		} catch (err) {
			console.log('access token expired');
			console.log(err);
		}
	}

	return await resolve(event);
};
