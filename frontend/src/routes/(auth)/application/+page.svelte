<script lang="ts">
	import {
		DataPrivacy,
		ProjectDetails,
		GroupInformation,
		EligibilityAgreement
	} from '$lib/components/application';
	import type { ActionData } from './$types';
	export let form: ActionData;

	let steps = ['data-privacy', 'project-details', 'group-information', 'eligibility-agreement'],
		currentActive = 0;

	let formData = {
		dataPrivacy: false,
		eligibility: false,
	};

	const handleStep = (stepIncrement: number) => {
		currentActive += stepIncrement;
		console.log(steps[currentActive]);
	};

	const toggleDataPrivacy = () => {
		formData.dataPrivacy = !formData.dataPrivacy;
	};

	const toggleEligibility = () => {
		formData.eligibility = !formData.eligibility;
	};




	
	console.log(form?.credentials);
</script>

<svelte:head>
	<title>Application</title>
</svelte:head>


<div class="flex-1 flex-col h-full rounded-inherit flex items-center justify-center">
	<div class="p-5 flex gap-2 cursor-pointer items-center w-full">
		<img src="launchlab_logo.png" alt="citeams_logo" class="w-8" />
		<a href="/" class="cursor-pointer font-black normal-case text-2xl">LaunchLab</a>
	</div>
	<img src="startup.png" alt="" class="flex-1 w-4/5 scale-x-[-1]" />
</div>
<div class="flex-1 flex flex-col gap-5 items-center justify-between h-full">
	<div class="flex-1 flex flex-col w-full p-10">
		{#if currentActive === 0}
			<h1 class="text-2xl font-semibold mb-5 px-6">Data Privacy and Consent</h1>
		{:else if currentActive === 1}
			<h1 class="text-2xl font-semibold mb-5 px-6">Project Details</h1>
		{:else if currentActive === 2}
			<h1 class="text-2xl font-semibold mb-5 px-6">Group Information</h1>
		{:else if currentActive === 3}
			<h1 class="text-2xl font-semibold mb-5 px-6">Eligibility and Agreement</h1>
		{/if}
		<form
			action="?/application"
			method="post"
			class="flex-1 flex flex-col"
			enctype="multipart/form-data"
		>
			<DataPrivacy dataPrivacy={formData.dataPrivacy} {toggleDataPrivacy} {currentActive} />
			<ProjectDetails {currentActive}/>
			<GroupInformation {currentActive}/>
			<EligibilityAgreement
				{toggleEligibility}
				eligibility={formData.eligibility}
				{currentActive}
			/>

			<div class="flex gap-3 justify-end">
				{#if currentActive != 0}
					<button class="btn" on:click|preventDefault={() => handleStep(-1)}>Prev</button>
				{/if}

				{#if currentActive < steps.length - 1}
					<button
						class="btn"
						on:click|preventDefault={() => handleStep(1)}
						type="submit"
						disabled={!formData.dataPrivacy}>Next</button
					>
				{:else}
					<button
						class="btn btn-primary"
						type="submit"
						disabled={!formData.eligibility}
						>Submit</button
					>
				{/if}
			</div>
			{#if form?.credentials}
				<p>invalid credentials</p>
			{/if}
		</form>
	</div>
</div>
