<script lang="ts">
	import { goto } from '$app/navigation';
	import {
		AcceptanceRL,
		MarketRL,
		OrganizationalRL,
		RegulatoryRL,
		TechnologyRL
	} from '$lib/components/assessment/index.js';
	import { onMount } from 'svelte';
	export let data;

	let trl: number = 9,
		mrl: number = 9,
		rrl: number = 9,
		arl: number = 9,
		orl: number = 9;

	let steps = ['trl', 'mrl', 'rrl', 'arl', 'orl'],
		currentActive = 0;

	const handleStep = (stepIncrement: number) => {
		currentActive += stepIncrement;
		console.log(steps[currentActive]);
	};

	const handleLevel = (levelName: string, level: number) => {
		if (levelName === 'trl') {
			trl = level;
		} else if (levelName === 'mrl') {
			mrl = level;
		} else if (levelName === 'rrl') {
			rrl = level;
		} else if (levelName === 'arl') {
			arl = level;
		} else if (levelName === 'orl') {
			orl = level;
		}
	};

	const handleSubmit = async () => {
		const response = await fetch('http://127.0.0.1:8000/readiness-levels/', {
			method: 'post',
			headers: {
				'Content-type': 'application/json',
				Authorization: `Bearer ${data.access}`
			},
			body: JSON.stringify({
				startup_id: data.user.startupId,
				trl: trl,
				orl: orl,
				mrl: mrl,
				rrl: rrl,
				arl: arl
			})
		});

		if (response.ok) {
			goto('/');
		}
	};
</script>

<svelte:head>
	<title>Assessment</title>
</svelte:head>
{#if data.hasAnswered.readiness_levels.length > 0}
	<div>
		you have already taken the assessment
	</div>
{:else}
	
<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-3 overflow-scroll h-full w-9/12 mx-auto">
			{#if currentActive === 0}
				<h2 class="text-2xl font-semibold mb-5 px-6">Technology Readiness Level</h2>
			{:else if currentActive === 1}
				<h2 class="text-2xl font-semibold mb-5 px-6">Market Readiness Level</h2>
			{:else if currentActive === 2}
				<h2 class="text-2xl font-semibold mb-5 px-6">Regulatory Readiness Level</h2>
			{:else if currentActive === 3}
				<h2 class="text-2xl font-semibold mb-5 px-6">Acceptance Readiness Level</h2>
			{:else if currentActive === 4}
				<h2 class="text-2xl font-semibold mb-5 px-6">Organizational Readiness Level</h2>
			{/if}
			<ul class="steps w-1/2 mx-auto">
				<li class="step" class:step-primary={currentActive >= 0}>TRL</li>
				<li class="step" class:step-primary={currentActive >= 1}>MRL</li>
				<li class="step" class:step-primary={currentActive >= 2}>RRL</li>
				<li class="step" class:step-primary={currentActive >= 3}>ARL</li>
				<li class="step" class:step-primary={currentActive >= 4}>ORL</li>
			</ul>
			<div class="flex-1 overflow-scroll">
				<div class="flex flex-col gap-10 h-0">
					<TechnologyRL {currentActive} {handleLevel} />
					<MarketRL {currentActive} {handleLevel} />
					<RegulatoryRL {currentActive} {handleLevel} />
					<AcceptanceRL {currentActive} {handleLevel} />
					<OrganizationalRL {currentActive} {handleLevel} />
					<div class="flex gap-3 justify-end">
						{#if currentActive != 0}
							<button class="btn btn-custom" on:click|preventDefault={() => handleStep(-1)}
								>Prev</button
							>
						{/if}

						{#if currentActive < steps.length - 1}
							<button
								class="btn btn-custom"
								on:click|preventDefault={() => handleStep(1)}
								type="submit">Next</button
							>
						{:else}
							<button class="btn btn-custom btn-primary" type="submit" on:click={handleSubmit}
								>Submit</button
							>
						{/if}
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
{/if}
