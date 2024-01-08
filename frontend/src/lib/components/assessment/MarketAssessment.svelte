<script lang="ts">
	import Icon from '../icons/icon.svelte';
	export let questions: any;
	export let answers: any;
	export let access: string;
	let check2 = true;
	const handleClick2 = () => {
		check2 = !check2;
	};

	const updateScore = async (
		id: number,
		newScore: number,
		startupId: number,
		urat_question_id: number,
		answers: string,
		readiness_type: string
	) => {
		const d = await fetch(`http://127.0.0.1:8000/urat-question-answers/${id}/`, {
			method: 'put',
			headers: {
				'Content-type': 'application/json',
				Authorization: `Bearer ${access}`
			},
			body: JSON.stringify({
				startup_id: startupId,
				urat_question_id: urat_question_id,
				response: answers,
				readiness_type: readiness_type,
				score: newScore
			})
		});

		if (d.ok) {
			console.log('ok');
		}
	};
</script>

<div class="collapse">
	<input type="checkbox" checked={check2} on:click={handleClick2} />
	<div class="collapse-title text-xl font-semibold">
		<div class="flex gap-3 items-center">
			<p class="text-lg">Market</p>
			<Icon
				data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
				data2={null}
			/>
		</div>
	</div>
	<div class="collapse-content flex flex-col gap-3">
		<div class="collapse-content flex flex-col gap-3">
			{#each questions as question, i}
				<div class="collapse">
					<input type="checkbox" checked={check2} />
					<div class="collapse-title text-xl font-semibold">
						<div class="flex gap-3 items-center">
							<p class="text-base">
								{question.question}
							</p>
							<Icon
								data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
								data2={null}
							/>
						</div>
					</div>
					<div class="collapse-content flex flex-col gap-3">
						<p>{answers[i].response}</p>
						<div class="flex gap-2">
							<div class="flex flex-col items-center gap-1">
								<input
									type="radio"
									name={`technology${answers[i].urat_question_id}`}
									class="radio"
									checked={answers[i].score === 1}
									on:click={() =>
										updateScore(
											answers[i].id,
											1,
											answers[i].startup_id,
											answers[i].urat_question_id,
											answers[i].response,
											answers[i].readiness_type
										)}
								/>
								<p class="text-xs">1</p>
							</div>
							<div class="flex flex-col items-center gap-1">
								<input
									type="radio"
									name={`technology${answers[i].urat_question_id}`}
									class="radio"
									checked={answers[i].score === 2}
									on:click={() =>
										updateScore(
											answers[i].id,
											2,
											answers[i].startup_id,
											answers[i].urat_question_id,
											answers[i].response,
											answers[i].readiness_type
										)}
								/>
								<p class="text-xs">2</p>
							</div>
							<div class="flex flex-col items-center gap-1">
								<input
									type="radio"
									name={`technology${answers[i].urat_question_id}`}
									class="radio"
									checked={answers[i].score === 3}
									on:click={() =>
										updateScore(
											answers[i].id,
											3,
											answers[i].startup_id,
											answers[i].urat_question_id,
											answers[i].response,
											answers[i].readiness_type
										)}
								/>
								<p class="text-xs">3</p>
							</div>
							<div class="flex flex-col items-center gap-1">
								<input
									type="radio"
									name={`technology${answers[i].urat_question_id}`}
									class="radio"
									checked={answers[i].score === 4}
									on:click={() =>
										updateScore(
											answers[i].id,
											4,
											answers[i].startup_id,
											answers[i].urat_question_id,
											answers[i].response,
											answers[i].readiness_type
										)}
								/>
								<p class="text-xs">4</p>
							</div>
							<div class="flex flex-col items-center gap-1">
								<input
									type="radio"
									name={`technology${answers[i].urat_question_id}`}
									class="radio"
									checked={answers[i].score === 5}
									on:click={() =>
										updateScore(
											answers[i].id,
											5,
											answers[i].startup_id,
											answers[i].urat_question_id,
											answers[i].response,
											answers[i].readiness_type
										)}
								/>
								<p class="text-xs">5</p>
							</div>
						</div>
					</div>
				</div>
			{/each}

		</div>
	</div>
</div>
