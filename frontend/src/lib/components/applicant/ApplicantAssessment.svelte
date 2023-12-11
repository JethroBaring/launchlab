<script lang="ts">
	import {
		AcceptanceAssessment,
		InvestmentAssessment,
		MarketAssessment,
		OrganizationalAssessment,
		RegulatoryAssessment,
		TechnologyAssessment
	} from '../assessment';
	import Icon from '../icons/icon.svelte';
	let check = true;
	export let data: any;
	export let access: any
	const handleClick = () => {
		check = !check;
	};
</script>

<div class="collapse">
	<input type="checkbox" checked={check} on:click={handleClick} />
	<div class="collapse-title text-xl font-semibold">
		<div class="flex gap-3 items-center">
			<p>Assessment</p>
			<Icon
				data1={check ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
				data2={null}
			/>
		</div>
	</div>
	<div class="collapse-content flex flex-col gap-3">
		<TechnologyAssessment response={data} {access}/>
		<MarketAssessment response={data} {access}/>
		<RegulatoryAssessment response={data} {access}/>
		<AcceptanceAssessment response={data} {access}/>
		<OrganizationalAssessment response={data} {access}/>
		<InvestmentAssessment response={data} {access}/>
	</div>
</div>
