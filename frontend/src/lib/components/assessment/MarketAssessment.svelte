<script lang="ts">
	import Icon from '../icons/icon.svelte';
	export let response: any;
	export let access: string;
	let check2 = true;
	const handleClick2 = () => {
		check2 = !check2;
	};

	const mrl: number[] = response.mrl.split(',').map(Number);

	const handleClick = async (payload: string) => {
		const x = await fetch(`http://127.0.0.1:8000/initial-readiness-levels/${response.id}/`, {
			method: 'put',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${access}`
			},
			body: JSON.stringify({
				mrl: payload
			})
		});

		if (x.ok) {
			console.log(x);
		} else {
			console.log(x);
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
			<div class="collapse">
				<input type="checkbox" checked={check2} />
				<div class="collapse-title text-xl font-semibold">
					<div class="flex gap-3 items-center">
						<p class="text-base">Have you identified your target market and customer base?</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.mrl_response[0].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="marketRating"
							class="mask mask-star"
							checked={mrl[0] === 1}
							on:click={() => {
								mrl[0] = 1;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating"
							class="mask mask-star"
							checked={mrl[0] === 2}
							on:click={() => {
								mrl[0] = 2;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating"
							class="mask mask-star"
							checked={mrl[0] === 3}
							on:click={() => {
								mrl[0] = 3;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating"
							class="mask mask-star"
							checked={mrl[0] === 4}
							on:click={() => {
								mrl[0] = 4;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating"
							class="mask mask-star"
							checked={mrl[0] === 5}
							on:click={() => {
								mrl[0] = 5;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
					</div>
				</div>
			</div>
			<div class="collapse">
				<input type="checkbox" checked={check2} />
				<div class="collapse-title text-xl font-semibold">
					<div class="flex gap-3 items-center">
						<p class="text-base">
							What market research have you conducted, and what are the key insights?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.mrl_response[1].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="marketRating1"
							class="mask mask-star"
							checked={mrl[1] === 1}
							on:click={() => {
								mrl[1] = 1;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating1"
							class="mask mask-star"
							checked={mrl[1] === 2}
							on:click={() => {
								mrl[1] = 2;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating1"
							class="mask mask-star"
							checked={mrl[1] === 3}
							on:click={() => {
								mrl[1] = 3;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating1"
							class="mask mask-star"
							checked={mrl[1] === 4}
							on:click={() => {
								mrl[1] = 4;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating1"
							class="mask mask-star"
							checked={mrl[1] === 5}
							on:click={() => {
								mrl[1] = 5;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
					</div>
				</div>
			</div>
			<div class="collapse">
				<input type="checkbox" checked={check2} />
				<div class="collapse-title text-xl font-semibold">
					<div class="flex gap-3 items-center">
						<p class="text-base">
							How are you planning to address the market needs and challenges identified in your
							research?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.mrl_response[2].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="marketRating2"
							class="mask mask-star"
							checked={mrl[2] === 1}
							on:click={() => {
								mrl[2] = 1;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating2"
							class="mask mask-star"
							checked={mrl[2] === 2}
							on:click={() => {
								mrl[2] = 2;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating2"
							class="mask mask-star"
							checked={mrl[2] === 3}
							on:click={() => {
								mrl[2] = 3;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating2"
							class="mask mask-star"
							checked={mrl[2] === 4}
							on:click={() => {
								mrl[2] = 4;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="marketRating2"
							class="mask mask-star"
							checked={mrl[2] === 5}
							on:click={() => {
								mrl[2] = 5;
								handleClick(`${mrl[0]},${mrl[1]},${mrl[2]}`);
							}}
						/>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
