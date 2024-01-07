<script lang="ts">
	import Icon from '../icons/icon.svelte';
	import AcceptanceRubricsUpdate from './AcceptanceRubricsUpdate.svelte';
	import InvestmentRubricsUpdate from './InvestmentRubricsUpdate.svelte';
	import MarketRubricsUpdate from './MarketRubricsUpdate.svelte';
	import OrganizationalRubricsUpdate from './OrganizationalRubricsUpdate.svelte';
	import RegulatoryRubricsUpdate from './RegulatoryRubricsUpdate.svelte';
	import TechnologyRubricsUpdate from './TechnologyRubricsUpdate.svelte';
	import SpiderGraph from '../shared/SpiderGraph.svelte';
	import DataPrivacy from '../application/DataPrivacy.svelte';

	export let questions: any, id: number, user: string, scores: any, access: any
	let check = false;
	let currentTab = 'Technology';
	const handleClick = () => {
		check = !check;
	};

	const handleTab = (tab: string) => {
		currentTab = tab;
	};

	let currentView = 'Graph';

	const handleView = (view: string) => {
		currentView = view;
	};

	console.log(scores.filter((score) => score.readiness_type === "Technology"))
</script>

<div class="collapse">
	<input type="checkbox" checked={check} on:click={handleClick} />
	<div class="collapse-title text-xl font-semibold">
		<div class="flex gap-3 items-center">
			<p>Readiness Level</p>
			<Icon
				data1={check ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
				data2={null}
			/>
		</div>
	</div>
	<div class="collapse-content flex flex-col gap-3">
		<div class="tabs">
			<a
				href="#"
				class="tab tab-lifted"
				class:tab-active={currentView === 'Graph'}
				on:click={() => handleView('Technology')}>Graph</a
			>
			<a
				href="#"
				class="tab tab-lifted"
				class:tab-active={currentView === 'Details'}
				on:click={() => handleView('Details')}>Details</a
			>
		</div>
		{#if currentView === "Details"}
			<div class="tabs">
				<a
					href="#"
					class="tab tab-lifted"
					class:tab-active={currentTab === 'Technology'}
					on:click={() => handleTab('Technology')}>Technology</a
				>
				<a
					href="#"
					class="tab tab-lifted"
					class:tab-active={currentTab === 'Market'}
					on:click={() => handleTab('Market')}>Market</a
				>
				<a
					href="#"
					class="tab tab-lifted"
					class:tab-active={currentTab === 'Organizational'}
					on:click={() => handleTab('Organizational')}>Organizational</a
				>
				<a
					href="#"
					class="tab tab-lifted"
					class:tab-active={currentTab === 'Acceptance'}
					on:click={() => handleTab('Acceptance')}>Acceptance</a
				>
				<a
					href="#"
					class="tab tab-lifted"
					class:tab-active={currentTab === 'Regulatory'}
					on:click={() => handleTab('Regulatory')}>Regulatory</a
				>
				<a
					href="#"
					class="tab tab-lifted"
					class:tab-active={currentTab === 'Investment'}
					on:click={() => handleTab('Investment')}>Investment</a
				>
			</div>
				<TechnologyRubricsUpdate
					questions={questions.filter((question) => question.readiness_type === 'Technology')}
					{currentTab}
					scores={scores.filter((score) => score.readiness_type === "Technology")}
					{access}
					startupId={id}
				/>
				<MarketRubricsUpdate
					questions={questions.filter((question) => question.readiness_type === 'Market')}
					{currentTab}
					scores={scores.filter((score) => score.readiness_type === "Market")}
				/>
				<AcceptanceRubricsUpdate
					questions={questions.filter((question) => question.readiness_type === 'Acceptance')}
					{currentTab}
					scores={scores.filter((score) => score.readiness_type === "Acceptance")}
				/>
				<OrganizationalRubricsUpdate
					questions={questions.filter((question) => question.readiness_type === 'Organizational')}
					{currentTab}
					scores={scores.filter((score) => score.readiness_type === "Organizational")}
				/>
				<RegulatoryRubricsUpdate
					questions={questions.filter((question) => question.readiness_type === 'Regulatory')}
					{currentTab}
					scores={scores.filter((score) => score.readiness_type === "Regulatory")}
				/>
				<InvestmentRubricsUpdate
					questions={questions.filter((question) => question.readiness_type === 'Investment')}
					{currentTab}
					scores={scores.filter((score) => score.readiness_type === "Investment")}
				/>
		{:else}
			<div class="w-1/2 mx-auto">
				<SpiderGraph trl={2} arl={2} irl={5} mrl={6} rrl={4} orl={6}/>
			</div>
		{/if}
	</div>
</div>
