<script lang="ts">
	import { technologyReadinessLevel } from '$lib/constants';
	import { Questions } from '$lib/utils';
	import TechnologyAssessment from '../assessment/TechnologyAssessment.svelte';

	export let currentActive: number, calculatorQuestions: any
	
</script>

<div class="flex-1 overflow-scroll mb-5 px-6" class:hidden={currentActive !== 10}>
	<div class="h-0 flex flex-col gap-3">
		{#each calculatorQuestions as category}
		<div class="form-control">
			<label class="label" for="projectTitle">
				<span class="label-text text-base">{category.category}</span>
			</label>
			{#each category.questions as question, i}
			<div class="form-control">
				<label class="label justify-normal gap-3 cursor-pointer" for="eligibilityAgree">
					<input
						type="radio"
						name={category.category}
						class="radio"
						value={question.id}
						checked={i === 0}
					/>
					<span class="label-text"
						>{question.question}</span
					>
				</label>
			</div>
			{/each}
		</div>
		{/each}
	</div>
</div>
