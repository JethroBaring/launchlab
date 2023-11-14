<script lang="ts">
	import type { NavLink } from '$lib/types';

	export let sidebarLinks: NavLink[];
	let activeLink: string = sidebarLinks[0].label;

	const handleClick = (label: string) => {
		activeLink = label;
	};

	export let name: string;
	export let type: string;

</script>

<nav
	class="hidden md:flex px-6 py-10 flex-col justify-between min-w-[270px] bg-slate-100 md:h-screen"
>
	<div class="flex flex-col gap-11">
		<div class="flex-1 flex gap-2 cursor-pointer">
			<img src="/launchlab_logo.png" alt="logo" class="w-8" />
			<a href="/" class="cursor-pointer font-black normal-case text-2xl">LaunchLab</a>
		</div>
		<div class="flex gap-3 items-center">
			<div class="avatar">
				<div class="h-10 rounded-full">
					<img
						src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtmqJGrLmhKGIyO8EPXp0V3d6YSSQ997vt0A&usqp=CAU"
						alt=""
					/>
				</div>
			</div>
			<div class="flex flex-col">
				<p class="text-md font-bold">{name}</p>
				<p class="text-sm">{type === 'S' ? "Startup" : "Manager"}</p>
			</div>
		</div>
		<ul class="flex flex-col gap-6">
			{#each sidebarLinks as link}
				<li
					class="rounded-lg base-medium hover:bg-gray-200 transition"
					class:bg-gray-200={activeLink === link.label}
				>
					<a
						href={`/${link.route}`}
						class="flex gap-4 items-center p-4"
						on:click={() => handleClick(link.label)}
					>
						<button>
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
						</button>
						{link.label}
					</a>
				</li>
			{/each}
		</ul>
	</div>
	<form action="/logout" method="post" class="flex gap-4 items-center p-4">
		<button>
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
		</button>
		logout
	</form>
</nav>
