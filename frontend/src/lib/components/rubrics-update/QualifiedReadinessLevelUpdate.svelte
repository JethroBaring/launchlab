<script lang="ts">
	import Icon from '../icons/icon.svelte';
	import AcceptanceRubricsUpdate from './AcceptanceRubricsUpdate.svelte';
	import InvestmentRubricsUpdate from './InvestmentRubricsUpdate.svelte';
	import MarketRubricsUpdate from './MarketRubricsUpdate.svelte';
	import OrganizationalRubricsUpdate from './OrganizationalRubricsUpdate.svelte';
	import RegulatoryRubricsUpdate from './RegulatoryRubricsUpdate.svelte';
	import TechnologyRubricsUpdate from './TechnologyRubricsUpdate.svelte';
	import SpiderGraph from '../shared/SpiderGraph.svelte';

	export let questions: any, id: number, user: string, scores: any, access: any, readiness: any;
	console.log(readiness);
	let check = false;
	let currentType = 'Technology';
	let currentTab = 'overview';

	const handleClick = (cur: string) => {
		currentTab = cur;
	};

	const handleType = (type: string) => {
		currentType = type;
	};

</script>

<div class="collapse">
	<input type="checkbox" checked={check} />
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
				{access}
				startupId={id}
				readiness_level={readiness.filter((r) => r.readiness_type==="Technology")[0]}
			/>
			<MarketRubricsUpdate
				questions={questions.filter((question) => question.readiness_type === 'Market')}
				currentTab={currentType}
				scores={scores.filter((score) => score.readiness_type === 'Market')}
				{access}
				startupId={id}
				readiness_level={readiness.filter((r) => r.readiness_type==="Market")[0]}

			/>
			<AcceptanceRubricsUpdate
				questions={questions.filter((question) => question.readiness_type === 'Acceptance')}
				currentTab={currentType}
				scores={scores.filter((score) => score.readiness_type === 'Acceptance')}
				{access}
				startupId={id}
				readiness_level={readiness.filter((r) => r.readiness_type==="Acceptance")[0]}

			/>
			<OrganizationalRubricsUpdate
				questions={questions.filter((question) => question.readiness_type === 'Organizational')}
				currentTab={currentType}
				scores={scores.filter((score) => score.readiness_type === 'Organizational')}
				{access}
				startupId={id}
				readiness_level={readiness.filter((r) => r.readiness_type==="Organizational")[0]}

			/>
			<RegulatoryRubricsUpdate
				questions={questions.filter((question) => question.readiness_type === 'Regulatory')}
				currentTab={currentType}
				scores={scores.filter((score) => score.readiness_type === 'Regulatory')}
				{access}
				startupId={id}
				readiness_level={readiness.filter((r) => r.readiness_type==="Regulatory")[0]}

			/>
			<InvestmentRubricsUpdate
				questions={questions.filter((question) => question.readiness_type === 'Investment')}
				currentTab={currentType}
				scores={scores.filter((score) => score.readiness_type === 'Investment')}
				{access}
				startupId={id}
				readiness_level={readiness.filter((r) => r.readiness_type==="Investment")[0]}

			/>
		{:else}
			<div class="w-1/2 mx-auto">
				<SpiderGraph
					trl={readiness.filter((r) => r.readiness_type === 'Technology')[0].readiness_level}
					arl={readiness.filter((r) => r.readiness_type === 'Acceptance')[0].readiness_level}
					irl={readiness.filter((r) => r.readiness_type==="Investment")[0].readiness_level}
					mrl={readiness.filter((r) => r.readiness_type==="Market")[0].readiness_level}
					rrl={readiness.filter((r) => r.readiness_type==="Regulatory")[0].readiness_level}
					orl={readiness.filter((r) => r.readiness_type==="Organizational")[0].readiness_level}
				/>
			</div>
		{/if}
	</div>
</div>
