<script lang="ts">
	import Icon from '../icons/icon.svelte';
	import AcceptanceRubricsUpdate from './AcceptanceRubricsUser.svelte';
	import InvestmentRubricsUpdate from './InvestmentRubricsUser.svelte';
	import MarketRubricsUpdate from './MarketRubricsUser.svelte';
	import OrganizationalRubricsUpdate from './OrganizationalRubricsUser.svelte';
	import RegulatoryRubricsUpdate from './RegulatoryRubricsUser.svelte';
	import TechnologyRubricsUpdate from './TechnologyRubricsUser.svelte';
	import SpiderGraph from '../shared/SpiderGraph.svelte';

	export let questions: any, scores: any;
	let currentType = 'Technology';
	let currentTab = 'overview';

	const handleClick = (cur: string) => {
		currentTab = cur;
	};

	const handleType = (type: string) => {
		currentType = type;
	};
</script>

<div class="tabs">
	<a
		class="tab tab-bordered"
		class:tab-active={currentTab === 'overview'}
		on:click={() => handleClick('overview')}>Overview</a
	>
	<a
		class="tab tab-bordered"
		class:tab-active={currentTab === 'detailed'}
		on:click={() => handleClick('detailed')}>Detailed Evaluation</a
	>
</div>
{#if currentTab === 'detailed'}
	<div class="flex w-full h-10 bg-slate-50">
		<button
			class="flex-1 flex justify-center items-center"
			on:click={() => handleType('Technology')}
			class:bg-slate-300={currentType === 'Technology'}>Technology</button
		>
		<button
			class="flex-1 flex justify-center items-center"
			on:click={() => handleType('Market')}
			class:bg-slate-300={currentType === 'Market'}>Market</button
		>
		<button
			class="flex-1 flex justify-center items-center"
			on:click={() => handleType('Organizational')}
			class:bg-slate-300={currentType === 'Organizational'}>Organizational</button
		>
		<button
			class="flex-1 flex justify-center items-center"
			on:click={() => handleType('Acceptance')}
			class:bg-slate-300={currentType === 'Acceptance'}>Acceptance</button
		>
		<button
			class="flex-1 flex justify-center items-center"
			on:click={() => handleType('Regulatory')}
			class:bg-slate-300={currentType === 'Regulatory'}>Regulatory</button
		>
		<button
			class="flex-1 flex justify-center items-center"
			on:click={() => handleType('Investment')}
			class:bg-slate-300={currentType === 'Investment'}>Investment</button
		>
	</div>
	<TechnologyRubricsUpdate
		questions={questions.filter((question) => question.readiness_type === 'Technology')}
		currentTab={currentType}
		scores={scores.filter((score) => score.readiness_type === 'Technology')}
	/>
	<MarketRubricsUpdate
		questions={questions.filter((question) => question.readiness_type === 'Market')}
		currentTab={currentType}
		scores={scores.filter((score) => score.readiness_type === 'Market')}
	/>
	<AcceptanceRubricsUpdate
		questions={questions.filter((question) => question.readiness_type === 'Acceptance')}
		currentTab={currentType}
		scores={scores.filter((score) => score.readiness_type === 'Acceptance')}
	/>
	<OrganizationalRubricsUpdate
		questions={questions.filter((question) => question.readiness_type === 'Organizational')}
		currentTab={currentType}
		scores={scores.filter((score) => score.readiness_type === 'Organizational')}
	/>
	<RegulatoryRubricsUpdate
		questions={questions.filter((question) => question.readiness_type === 'Regulatory')}
		currentTab={currentType}
		scores={scores.filter((score) => score.readiness_type === 'Regulatory')}
	/>
	<InvestmentRubricsUpdate
		questions={questions.filter((question) => question.readiness_type === 'Investment')}
		currentTab={currentType}
		scores={scores.filter((score) => score.readiness_type === 'Investment')}
	/>
{:else}
	<div class="w-1/2 mx-auto">
		<SpiderGraph trl={2} arl={2} irl={5} mrl={6} rrl={4} orl={6} />
	</div>
{/if}
