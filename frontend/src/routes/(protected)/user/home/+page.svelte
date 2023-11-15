<script>
	import PostCard from '$lib/components/shared/PostCard.svelte';
	const samplePost = ['Jethro', 'Hannah'];
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 items-center gap-10 overflow-scroll py-10 px-5 md:px-8 lg:p-14">
		<div class="max-w-screen-sm flex flex-col items-center w-full gap-6 md:gap-9">
			<h2 class="text-xl font-bold text-left w-full">Home</h2>
			{#each samplePost as post}
				<PostCard />
			{/each}
		</div>
	</div>
</div>
