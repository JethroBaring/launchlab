import { writable } from 'svelte/store';

function createMessage() {
	const { subscribe, set, update } = writable(0);

	return {
		subscribe,
		increment: () => update((n) => n + 1),
		reset: () => set(0)
	};
}

export const message = createMessage();
