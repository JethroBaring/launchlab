<script lang="ts">
	import {
		DataPrivacy,
		ProjectDetails,
		GroupInformation,
		EligibilityAgreement,
		Technology,
		Market,
		Regulatory,
		Acceptance,
		Organizational,
		Investment
	} from '$lib/components/application';
	import ApplicationForm from '$lib/components/application/ApplicationForm.svelte';
	import Image from '$lib/components/application/Image.svelte';
	import type { ActionData } from './$types';
	export let form: ActionData;

	let steps = [
			'data-privacy',
			'project-details',
			'group-information',
			'eligibility-agreement',
			'technology',
			'market',
			'regulatory',
			'acceptance',
			'organizational',
			'investment',
			'calculator'
		],
		currentActive = 0;

	const handleStep = (stepIncrement: number) => {
		currentActive += stepIncrement;
		console.log(steps[currentActive]);
	};

	const labels = [
		'Data Privacy and Consent',
		'Project Details',
		'Group Information',
		'Eligibility and Agreement',
		'Technology Readiness Level',
		'Market Readiness Level',
		'Regulatory Readiness Level',
		'Acceptance Readiness Level',
		'Organizational Readiness Level',
		'Investment Readiness Level',
		'Technology and Commercialization Readiness Level Calculator'
	];

	export let data
	console.log(data.technologyQuestions)
</script>

<svelte:head>
	<title>Application</title>
</svelte:head>

<div class="flex-1 flex-col h-full rounded-inherit flex items-center relative">
	<div class="p-5 flex gap-2 cursor-pointer items-center w-full absolute">
		<img src="launchlab_logo.png" alt="citeams_logo" class="w-8" />
		<a href="/" class="cursor-pointer font-black normal-case text-2xl">ChumCheck</a>
	</div>
	<div class="flex-1 flex items-center justify-center">
		<Image {currentActive} {steps} />
	</div>
</div>
<div class="flex-1 flex flex-col gap-5 items-center justify-between h-full">
	<div class="flex-1 flex flex-col w-full p-10">
		<h1 class="text-2xl font-semibold mb-5 px-6">{labels[currentActive]}</h1>
		<ApplicationForm {form} {steps} {handleStep} {currentActive} questions={data}/>
	</div>
</div>
