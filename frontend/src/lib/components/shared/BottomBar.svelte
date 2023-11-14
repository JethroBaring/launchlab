<script lang="ts">
	import type { NavLink } from '$lib/types';

	export let bottomBarLinks: NavLink[];
	let activeLink: string = bottomBarLinks[0].label;
	const handleClick = (label: string) => {
		activeLink = label;
	};
</script>

<section
	class="flex z-50 justify-between w-full sticky bottom-0 rounded-t-[20px] bg-dark-2 px-5 py-4 md:hidden"
>
	{#each bottomBarLinks as link}
		<a
			href={`/${link.route}`}
			class="flex items-center flex-col gap-1 p-2 transition hover:bg-gray-200 rounded-lg"
            class:bg-gray-200={activeLink==link.label}
			on:click={() => handleClick(link.label)}
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				stroke-width="1.5"
				stroke="currentColor"
				class="w-6 h-6"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75"
				/>
			</svg>
		</a>
	{/each}
</section>
