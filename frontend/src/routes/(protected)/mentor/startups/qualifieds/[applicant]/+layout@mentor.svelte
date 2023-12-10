<script lang="ts">
	import Icon from '$lib/components/icons/icon.svelte';
	export let data;
	let applicant = true
	const handleClick = () => {
		applicant = !applicant
	}
</script>


<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-5 overflow-scroll h-full">
			<div class="flex gap-5 items-center">
				<a href="/mentor/startups/qualifieds">
					<Icon data1={'M19.5 12h-15m0 0l6.75 6.75M4.5 12l6.75-6.75'} data2={null} />
				</a>
				<h2 class="text-lg text-left">Back</h2>
			</div>
			<div class="flex-1 overflow-scroll">
				<div class="tabs">
					<a class="tab tab-lifted" href={`/mentor/startups/qualifieds/${data.params}/information`} class:tab-active={applicant} on:click={handleClick}>Information</a> 
					<a class="tab tab-lifted" href={`/mentor/startups/qualifieds/${data.params}/evaluation`} class:tab-active={!applicant} on:click={handleClick}>Evaluation</a> 
				  </div>
				<div class="h-0">
					<slot />
				</div>
			</div>
		</div>
	</div>
</div>
