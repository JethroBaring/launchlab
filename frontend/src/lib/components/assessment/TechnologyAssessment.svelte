<script lang="ts">
	import Icon from '../icons/icon.svelte';
	export let response: any;
	export let access: string;
	let check2 = true;
	const handleClick2 = () => {
		check2 = !check2;
	};

	const trl: number[] = response.trl.split(',').map(Number);

	const handleClick = async (payload: string) => {
		const x = await fetch(`http://127.0.0.1:8000/initial-readiness-levels/${response.id}/`, {
			method: 'put',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${access}`
			},
			body: JSON.stringify({
				trl: payload
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
			<p class="text-lg">Technology</p>
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
						<p class="text-base">
							Describe the current stage of your technology development. Has it been validated in a
							lab or relevant environment?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.trl_response[0].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="technologyRating"
							class="mask mask-star"
							checked={trl[0] === 1}
							on:click={() => {
								trl[0] = 1;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating"
							class="mask mask-star"
							checked={trl[0] === 2}
							on:click={() => {
								trl[0] = 2;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating"
							class="mask mask-star"
							checked={trl[0] === 3}
							on:click={() => {
								trl[0] = 3;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating"
							class="mask mask-star"
							checked={trl[0] === 4}
							on:click={() => {
								trl[0] = 4;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating"
							class="mask mask-star"
							checked={trl[0] === 5}
							on:click={() => {
								trl[0] = 5;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
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
							What evidence can you provide of your technology's functionality and feasibility?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.trl_response[1].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="technologyRating1"
							class="mask mask-star"
							checked={trl[1] === 1}
							on:click={() => {
								trl[1] = 1;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating1"
							class="mask mask-star"
							checked={trl[1] === 2}
							on:click={() => {
								trl[1] = 2;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating1"
							class="mask mask-star"
							checked={trl[1] === 3}
							on:click={() => {
								trl[1] = 3;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating1"
							class="mask mask-star"
							checked={trl[1] === 4}
							on:click={() => {
								trl[1] = 4;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating1"
							class="mask mask-star"
							checked={trl[1] === 5}
							on:click={() => {
								trl[1] = 5;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
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
							How does your current technology development align with your product roadmap and
							market goals?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.trl_response[2].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="technologyRating2"
							class="mask mask-star"
							checked={trl[2] === 1}
							on:click={() => {
								trl[2] = 1;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating2"
							class="mask mask-star"
							checked={trl[2] === 2}
							on:click={() => {
								trl[2] = 2;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating2"
							class="mask mask-star"
							checked={trl[2] === 3}
							on:click={() => {
								trl[2] = 3;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating2"
							class="mask mask-star"
							checked={trl[2] === 4}
							on:click={() => {
								trl[2] = 4;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="technologyRating2"
							class="mask mask-star"
							checked={trl[2] === 5}
							on:click={() => {
								trl[2] = 5;
								handleClick(`${trl[0]},${trl[1]},${trl[2]}`);
							}}
						/>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
