<script lang="ts">
	import Icon from '../icons/icon.svelte';
	export let response: any;
	export let access: string;

	let check2 = true;
	const handleClick2 = () => {
		check2 = !check2;
	};

	const rrl: number[] = response.rrl.split(',').map(Number);

	const handleClick = async (payload: string) => {
		const x = await fetch(`http://127.0.0.1:8000/initial-readiness-levels/${response.id}/`, {
			method: 'put',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${access}`
			},
			body: JSON.stringify({
				rrl: payload
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
			<p class="text-lg">Regulatory</p>
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
							Are you aware of the regulatory requirements relevant to your product or service?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.rrl_response[0].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="regulatoryRating"
							class="mask mask-star"
							checked={rrl[0] === 1}
							on:click={() => {
								rrl[0] = 1;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating"
							class="mask mask-star"
							checked={rrl[0] === 2}
							on:click={() => {
								rrl[0] = 2;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating"
							class="mask mask-star"
							checked={rrl[0] === 3}
							on:click={() => {
								rrl[0] = 3;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating"
							class="mask mask-star"
							checked={rrl[0] === 4}
							on:click={() => {
								rrl[0] = 4;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating"
							class="mask mask-star"
							checked={rrl[0] === 5}
							on:click={() => {
								rrl[0] = 5;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
					</div>
				</div>
			</div>
			<div class="collapse">
				<input type="checkbox" checked={check2} />
				<div class="collapse-title text-xl font-semibold">
					<div class="flex gap-3 items-center">
						<p class="text-base">Have you begun planning or implementing compliance strategies?</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.rrl_response[1].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="regulatoryRating1"
							class="mask mask-star"
							checked={rrl[1] === 1}
							on:click={() => {
								rrl[1] = 1;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating1"
							class="mask mask-star"
							checked={rrl[1] === 2}
							on:click={() => {
								rrl[1] = 2;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating1"
							class="mask mask-star"
							checked={rrl[1] === 3}
							on:click={() => {
								rrl[1] = 3;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating1"
							class="mask mask-star"
							checked={rrl[1] === 4}
							on:click={() => {
								rrl[1] = 4;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating1"
							class="mask mask-star"
							checked={rrl[1] === 5}
							on:click={() => {
								rrl[1] = 5;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
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
							How do you manage and stay updated with changes in regulatory requirements?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.rrl_response[2].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="regulatoryRating2"
							class="mask mask-star"
							checked={rrl[2] === 1}
							on:click={() => {
								rrl[2] = 1;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating2"
							class="mask mask-star"
							checked={rrl[2] === 2}
							on:click={() => {
								rrl[2] = 2;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating2"
							class="mask mask-star"
							checked={rrl[2] === 3}
							on:click={() => {
								rrl[2] = 3;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating2"
							class="mask mask-star"
							checked={rrl[2] === 4}
							on:click={() => {
								rrl[2] = 4;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="regulatoryRating2"
							class="mask mask-star"
							checked={rrl[2] === 5}
							on:click={() => {
								rrl[2] = 5;
								handleClick(`${rrl[0]},${rrl[1]},${rrl[2]}`);
							}}
						/>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
