<script lang="ts">
	import DataPrivacy from '$lib/components/application/DataPrivacy.svelte';
	import EligibilityAgreement from '$lib/components/application/EligibilityAgreement.svelte';
	import GroupInformation from '$lib/components/application/GroupInformation.svelte';
	import ProjectDetails from '$lib/components/application/ProjectDetails.svelte';

	let steps = ['data-privacy', 'project-details', 'group-information', 'eligibility-agreement'],
		currentActive = 0;

	let formData = {
		dataPrivacy: false,
		startupName: '',
		links: '',
		groupName: '',
		memberName1: '',
		memberName2: '',
		memberName3: '',
		memberName4: '',
		memberName5: '',
		universityName: '',
		eligibility: ''
	};

	const handleStep = (stepIncrement: number) => {
		currentActive += stepIncrement;
		console.log(steps[currentActive]);
	};

	const toggleDataPrivacy = () => {
		formData.dataPrivacy = !formData.dataPrivacy
	}
</script>

<div class="flex-1 flex-col h-full rounded-inherit flex items-center justify-center">
	<div class="p-5 flex gap-2 cursor-pointer items-center w-full">
		<img src="launchlab_logo.png" alt="citeams_logo" class="w-8" />
		<a href="/" class="cursor-pointer font-black normal-case text-2xl">LaunchLab</a>
	</div>
	<img src="startup.png" alt="" class="flex-1 w-4/5 scale-x-[-1]" />
</div>
<div class="flex-1 flex flex-col gap-5 items-center justify-between h-full">
	<div class="flex-1 flex flex-col w-full p-10">
		{#if steps[currentActive] === 'data-privacy'}
			<DataPrivacy dataPrivacy={formData.dataPrivacy} toggleDataPrivacy={toggleDataPrivacy}/>
		{:else if steps[currentActive] === 'project-details'}
			<ProjectDetails
				startupName={formData.startupName}
				groupName={formData.groupName}
				links={formData.links}
			/>
		{:else if steps[currentActive] === 'group-information'}
			<GroupInformation
				memberName1={formData.memberName1}
				memberName2={formData.memberName2}
				memberName3={formData.memberName3}
				memberName4={formData.memberName4}
				memberName5={formData.memberName5}
				universityName={formData.universityName}
			/>
		{:else if steps[currentActive] === 'eligibility-agreement'}
			<EligibilityAgreement />
		{/if}
		<div class="flex gap-3 justify-end">
			{#if currentActive != 0}
				<button class="btn" on:click={() => handleStep(-1)}>Prev</button>
			{/if}

			{#if currentActive < steps.length - 1}
				<button class="btn" on:click={() => handleStep(1)} disabled={!formData.dataPrivacy}>Next</button>
			{:else}
				<button class="btn btn-primary">Submit</button>
			{/if}
		</div>
	</div>
</div>
