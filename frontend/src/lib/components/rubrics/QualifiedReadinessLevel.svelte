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
	let currentTab = "Technology"
	const handleClick = () => {
		check = !check;
	};

	const handleTab = (tab: string) => {
		currentTab = tab
	}
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
			<a href="#" class="tab tab-lifted" class:tab-active={currentTab === "Technology"} on:click={() => handleTab("Technology")}>Technology</a>
			<a href="#" class="tab tab-lifted" class:tab-active={currentTab === "Market"} on:click={() => handleTab("Market")}>Market</a>
			<a href="#" class="tab tab-lifted" class:tab-active={currentTab === "Organizational"} on:click={() => handleTab("Organizational")}>Organizational</a>
			<a href="#" class="tab tab-lifted" class:tab-active={currentTab === "Acceptance"} on:click={() => handleTab("Acceptance")}>Acceptance</a>
			<a href="#" class="tab tab-lifted" class:tab-active={currentTab === "Regulatory"} on:click={() => handleTab("Regulatory")}>Regulatory</a>
			<a href="#" class="tab tab-lifted" class:tab-active={currentTab === "Investment"} on:click={() => handleTab("Investment")}>Investment</a>
		</div>
		<form action={`/${user}/startups/qualified/${id}?/technology`} method="post">
			<TechnologyRubrics questions={questions.filter(question => question.readiness_type === "Technology")} {currentTab}/>
			<MarketRubrics questions={questions.filter(question => question.readiness_type === "Market")} {currentTab}/>
			<AcceptanceRubrics questions={questions.filter(question => question.readiness_type === "Acceptance")} {currentTab}/>
			<OrganizationalRubrics questions={questions.filter(question => question.readiness_type === "Organizational")} {currentTab}/>
			<RegulatoryRubrics questions={questions.filter(question => question.readiness_type === "Regulatory")} {currentTab}/>
			<InvestmentRubrics questions={questions.filter(question => question.readiness_type === "Investment")} {currentTab}/>
			<button class="btn btn-primary" type="submit">save</button>
		</form>
	</div>
</div>
