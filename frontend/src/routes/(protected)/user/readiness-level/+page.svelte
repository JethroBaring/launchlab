<script lang="ts">
	import { browser } from '$app/environment';
	import ApplicantReadinessLevel from '$lib/components/applicant/ApplicantReadinessLevel.svelte';
	import Icon from '$lib/components/icons/icon.svelte';
	import QualifiedReadinessLevelUpdate from '$lib/components/rubrics-update/QualifiedReadinessLevelUpdate.svelte';
	import QualifiedReadinessLevel from '$lib/components/rubrics/QualifiedReadinessLevel.svelte';
	import SpiderGraph from '$lib/components/shared/SpiderGraph.svelte';
	import QualifiedReadinessLevelUser from '$lib/components/user-rubric/QualifiedReadinessLevelUser.svelte';
	import { Chart } from 'chart.js/auto';
	import { onMount } from 'svelte';
	export let data;
</script>

<svelte:head>
	<title>Startup - Readiness Level</title>
</svelte:head>

<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-3 overflow-scroll h-full w-full mx-auto">
			<h2 class="text-2xl font-bold text-left">Readiness Level</h2>
			{#if data.scores.length != 0}
				<div class="flex-1 overflow-scroll">
					<div class="h-0">
						<div class="flex flex-col gap-5">
							<QualifiedReadinessLevelUser questions={data.questions} scores={data.scores} readiness={data.readiness}/>
						</div>
					</div>
				</div>
			{:else}
				<div class="flex justify-center items-center w-full h-full font-semibold">Not rated yet.</div>
			{/if}
		</div>
	</div>
</div>
