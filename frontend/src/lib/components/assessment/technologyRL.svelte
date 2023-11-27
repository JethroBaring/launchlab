<script lang="ts">
	import { technologyReadinessLevel } from '$lib/constants';
	export let currentActive: any, handleLevel: Function
	let answers = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'];
	let currentAnswer = '';
	let level = 0;
	const handleAnswer = (index: number, answer: string) => {
		answers[index] = answer;
		if (answer === 'Yes') {
			level = 9 - index;
			currentAnswer = 'Yes';
			for (let i = index + 1; i < answers.length; i++) {
				answers[i] = 'Yes';
			}
			handleLevel('trl', level)
		} else {
			currentAnswer = 'No';
		}
	};
</script>

<div class:hidden={currentActive !== 0}>
	{#each technologyReadinessLevel as question, i}
		<div class="bg-slate-100 p-10 rounded-lg" class:hidden={answers[i - 1] !== 'No' && i !== 0}>
			<p class="text-lg">
				{question.question}
			</p>
			<div class="form-control w-20">
				<label class="label cursor-pointer" for="dataPrivacyAgree">
					<input
						type="radio"
						name={`technology${i}`}
						id={`technology${i}`}
						class="radio"
						on:click={() => handleAnswer(i, 'Yes')}
						checked={false}
					/>
					<span class="label-text">Yes</span>
				</label>
			</div>
			<div class="form-control w-20">
				<label class="label cursor-pointer" for="dataPrivacyDisagree">
					<input
						type="radio"
						name={`technology${i}`}
						id={`technology${i}`}
						class="radio"
						on:click={() => handleAnswer(i, 'No')}
						checked={false}
					/>
					<span class="label-text">No</span>
				</label>
			</div>
		</div>
	{/each}
</div>
