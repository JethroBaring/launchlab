<script lang="ts">
	let current = 'pending'
	const handleClick = (cur: string) => {
		current = cur
	};
</script>

<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-3 overflow-scroll h-full w-full mx-auto">
			<h2 class="text-2xl font-bold text-left">Startups</h2>
			<div class="tabs">
				<a
					href="/admin/startups/pending"
					class="tab tab-bordered tab-active"
					class:tab-active={current === 'pending'}
					on:click={() => handleClick('pending')}>Pending</a
				>
				<a
					href="/admin/startups/qualified"
					class="tab tab-bordered"
					class:tab-active={current === 'rated'}
					on:click={() => handleClick('rated')}>Rated</a
				>
				<a
					href="/admin/startups/pending"
					class="tab tab-bordered tab-active"
					class:tab-active={current === 'qualified'}
					on:click={() => handleClick('qualified')}>Qualified</a
				>
			</div>
			<div class="flex-1 overflow-scroll">
				<slot />
			</div>
		</div>
	</div>
</div>
