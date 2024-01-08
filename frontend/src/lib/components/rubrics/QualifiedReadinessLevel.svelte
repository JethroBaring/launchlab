<script lang="ts">
	import Icon from '../icons/icon.svelte';
	import AcceptanceRubrics from './AcceptanceRubrics.svelte';
	import InvestmentRubrics from './InvestmentRubrics.svelte';
	import MarketRubrics from './MarketRubrics.svelte';
	import OrganizationalRubrics from './OrganizationalRubrics.svelte';
	import RegulatoryRubrics from './RegulatoryRubrics.svelte';
	import TechnologyRubrics from './TechnologyRubrics.svelte';
	export let questions: any, id: number, user: string
	let check = false;

	let currentType = 'Technology';
	const handleType = (type: string) => {
		currentType = type;
	};
	const handleClick = () => {
		check = !check;
	};

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
		<form action={`/${user}/startups/qualified/${id}?/technology`} method="post">
			<TechnologyRubrics questions={questions.filter(question => question.readiness_type === "Technology")} currentTab={currentType}/>
			<MarketRubrics questions={questions.filter(question => question.readiness_type === "Market")} currentTab={currentType}/>
			<AcceptanceRubrics questions={questions.filter(question => question.readiness_type === "Acceptance")} currentTab={currentType}/>
			<OrganizationalRubrics questions={questions.filter(question => question.readiness_type === "Organizational")} currentTab={currentType}/>
			<RegulatoryRubrics questions={questions.filter(question => question.readiness_type === "Regulatory")} currentTab={currentType}/>
			<InvestmentRubrics questions={questions.filter(question => question.readiness_type === "Investment")} currentTab={currentType}/>
			<div class="flex w-full justify-end">
				<button class="btn btn-primary btn-custom mt-5" type="submit">save</button>
			</div>
		</form>
	</div>
</div>
