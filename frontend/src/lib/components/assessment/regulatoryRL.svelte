<script lang="ts">
	import { regulatoryReadinessLevel } from '$lib/constants';
	export let currentActive: any, handleLevel: Function;
	let answers = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'];

	let currentAnswer = '';
	let level = 0
	const handleAnswer = (index: number, answer: string) => {
		answers[index] = answer;
		if (answer === 'Yes') {
			level = 9 - index;
			currentAnswer = 'Yes';
			for (let i = index + 1; i < answers.length; i++) {
				answers[i] = 'Yes';
			}
			handleLevel('rrl', level)
		} else {
			currentAnswer = 'No';
		}
	};
</script>

<div class:hidden={currentActive !== 2}>
	{#each regulatoryReadinessLevel as question, i}
		<div class="bg-slate-100 p-10 rounded-lg" class:hidden={answers[i - 1] !== 'No' && i !== 0}>
			<p class="text-lg">
				{question.question}
			</p>
			<div class="form-control w-20">
				<label class="label cursor-pointer" for="dataPrivacyAgree">
					<input
						type="radio"
						name={`regulatory${i}`}
						id="dataPrivacyAgree"
						class="radio"
						value="true"
						on:click={() => handleAnswer(i, 'Yes')}
					/>
					<span class="label-text">Yes</span>
				</label>
			</div>
			<div class="form-control w-20">
				<label class="label cursor-pointer" for="dataPrivacyDisagree">
					<input
						type="radio"
						name={`regulator${i}`}
						id="dataPrivacyDisagree"
						class="radio"
						value="false"
						on:click={() => handleAnswer(i, 'No')}
					/>
					<span class="label-text">No</span>
				</label>
			</div>
		</div>
	{/each}
</div>
