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
	export let questions: any;
	export let answers: any
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
		<TechnologyAssessment {access} questions={questions.filter((q) => q.readiness_type === "Technology")} answers={answers.filter((a) => a.readiness_type === "Technology")}/>
		<MarketAssessment {access} questions={questions.filter((q) => q.readiness_type === "Market")} answers={answers.filter((a) => a.readiness_type === "Market")}/>
		<RegulatoryAssessment {access} questions={questions.filter((q) => q.readiness_type === "Regulatory")} answers={answers.filter((a) => a.readiness_type === "Regulatory")}/>
		<AcceptanceAssessment {access} questions={questions.filter((q) => q.readiness_type === "Acceptance")} answers={answers.filter((a) => a.readiness_type === "Acceptance")}/>
		<OrganizationalAssessment {access} questions={questions.filter((q) => q.readiness_type === "Organizational")} answers={answers.filter((a) => a.readiness_type === "Organizational")}/>
		<InvestmentAssessment {access} questions={questions.filter((q) => q.readiness_type === "Investment")} answers={answers.filter((a) => a.readiness_type === "Investment")}/>
	</div>
</div>
