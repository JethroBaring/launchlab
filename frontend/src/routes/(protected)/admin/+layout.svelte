<script lang="ts">
	import { browser } from '$app/environment';
	import { TopBar, LeftSideBar, BottomBar } from '$lib/components/shared';
	import { adminSidebarLinks } from '$lib/constants';
	import { onDestroy } from 'svelte';
	export let data;
</script>

<main class="flex h-screen">
	<div class="w-full md:flex">
		<TopBar />
		<LeftSideBar
			sidebarLinks={adminSidebarLinks}
			name={`${data.user.email}`}
			type={data.user.type}
		/>
		<div class="flex flex-1 h-full p-10 bg-slate-100">
			<slot />
		</div>
		<BottomBar bottomBarLinks={adminSidebarLinks} />
	</div>
</main>
<!-- <div class="bg-slate-50 flex-1 rounded-lg flex items-center flex-col">
						<div class="p-5 w-full">
							<div class="font-semibold text-lg">Startups</div>
							<canvas id="chart3" class="flex-1 h-32" height="105" />
						</div>
					</div> -->
