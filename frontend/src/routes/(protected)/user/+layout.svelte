<script>
	import { TopBar, LeftSideBar, BottomBar } from '$lib/components/shared';
	import { userSidebarLinks } from '$lib/constants';
	export let data
</script>

<main class="flex h-screen">
	<div class="w-full md:flex">
		<TopBar />
		<LeftSideBar sidebarLinks={userSidebarLinks} name={data.user.startupName ?? ""}  type={data.user.type}/>
		<div class="flex flex-1 h-full">
			<slot />
		</div>
		<BottomBar bottomBarLinks={userSidebarLinks} />
	</div>
</main>
