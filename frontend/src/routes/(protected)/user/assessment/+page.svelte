<script lang="ts">
	import PostCard from '$lib/components/shared/PostCard.svelte';
	import { technologyReadinessLevel } from '$lib/constants';
	let answers = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes']

	let level = 0;
	let currentAnswer = ''
	console.log(currentAnswer)
	const handleAnswer = (index: number, answer: string) => {
		answers[index] = answer
		if(answer === 'Yes') {
			level = 9 - index
			currentAnswer = 'Yes'
		} else {
			currentAnswer = 'No'
		}
		console.log(level, currentAnswer)
	}
</script>

<svelte:head>
	<title>Tasks</title>
</svelte:head>
{#if true}
<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 items-center gap-10 overflow-scroll py-10 px-5 md:px-8 lg:p-14">
		<div class="max-w-screen-sm flex flex-col items-center w-full gap-6 md:gap-9">
			<h2 class="text-xl font-bold text-left w-full">Assessment</h2>
			{#each technologyReadinessLevel as item, i}
				<div class:hidden={answers[i-1] !== 'No' && i !== 0}>
					<PostCard question={item.question}/>
					<input type="radio" name={`answer${i}`} on:click={() => handleAnswer(i, 'Yes')}/>Yes
					<input type="radio" name={`answer${i}`} on:click={() => handleAnswer(i, 'No')}/>No
				</div>
			{/each}
			<button class="btn btn-primary btn-custom" disabled={currentAnswer !== 'Yes'}>Next</button>
		</div>
	</div>
</div>
{:else}
	You have already taken the assessment
{/if}
