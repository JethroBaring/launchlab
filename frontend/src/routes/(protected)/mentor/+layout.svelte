<script lang="ts">
	import { TopBar, LeftSideBar, BottomBar } from '$lib/components/shared';
	import { mentorSidebarLinks } from '$lib/constants';
	export let data;
</script>

<main class="flex h-screen">
	<div class="w-full md:flex">
		<TopBar />
		<LeftSideBar sidebarLinks={mentorSidebarLinks} name={`${data.user.firstName} ${data.user.lastName}`}
		type={"ME"}/>
		<div class="flex flex-1 h-full p-10 bg-slate-100">
			<slot />
		</div>
	</div>
</main>
