<script>
	import { TopBar, LeftSideBar, BottomBar } from '$lib/components/shared';
	import { adminSidebarLinks } from '$lib/constants';
	export let data
</script>

<div class="w-full md:flex">
	<TopBar />
	<LeftSideBar sidebarLinks={adminSidebarLinks} name={`${data.user.firstName} ${data.user.lastName}`} type={data.user.type}/>
	<div class="flex flex-1 h-full">
		<slot />
	</div>
</div>
