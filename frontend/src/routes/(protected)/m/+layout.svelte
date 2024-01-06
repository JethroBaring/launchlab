<script lang="ts">
	import { TopBar, LeftSideBar, BottomBar } from '$lib/components/shared';
	import { userSidebarLinks } from '$lib/constants';
</script>

<main class="flex h-screen">
	<div class="w-full md:flex">
		<TopBar />
		<LeftSideBar sidebarLinks={userSidebarLinks} name={"mentor" ?? ""}  type={"M"}/>
		<div class="flex flex-1 h-full p-10 bg-slate-100">
			<slot />
		</div>
		<BottomBar bottomBarLinks={userSidebarLinks} />
	</div>
</main>
