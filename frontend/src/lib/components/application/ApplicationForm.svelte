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
		Investment,

		TechnologyCalculator

	} from '$lib/components/application';
	export let form: any, steps: any, handleStep: Function, currentActive: number;

	let formData = {
		dataPrivacy: false,
		eligibility: false
	};

	const toggleDataPrivacy = () => {
		formData.dataPrivacy = !formData.dataPrivacy;
	};

	const toggleEligibility = () => {
		formData.eligibility = !formData.eligibility;
	};

	export let questions: any
</script>

<form
	action="?/application"
	method="post"
	class="flex-1 flex flex-col"
	enctype="multipart/form-data"
>
	<DataPrivacy dataPrivacy={formData.dataPrivacy} {toggleDataPrivacy} {currentActive} />
	<ProjectDetails {currentActive} />
	<GroupInformation {currentActive} />
	<EligibilityAgreement {toggleEligibility} eligibility={formData.eligibility} {currentActive} />
	<Technology {currentActive} question={questions.technologyQuestions}/>
	<Market {currentActive} question={questions.marketQuestions}/>
	<Regulatory {currentActive} question={questions.regulatoryQuestions}/>
	<Acceptance {currentActive} question={questions.acceptanceQuestions}/>
	<Organizational {currentActive} question={questions.organizationalQuestions}/>
	<Investment {currentActive} question={questions.investmentQuestions}/>
	<TechnologyCalculator {currentActive}/>
	<div class="flex gap-3 justify-end">
		{#if currentActive != 0}
			<button class="btn btn-custom normal-case w-24" on:click|preventDefault={() => handleStep(-1)}
				>Previous</button
			>
		{/if}

		{#if currentActive < steps.length - 1}
			<button
				class="btn btn-custom normal-case w-24"
				on:click|preventDefault={() => handleStep(1)}
				type="submit"
				disabled={!formData.dataPrivacy}>Next</button
			>
		{:else}
			<button class="btn btn-primary btn-custom normal-case w-24" type="submit">Submit</button>
		{/if}
	</div>
	{#if form?.credentials}
		<p>all fields are required</p>
	{/if}
</form>
