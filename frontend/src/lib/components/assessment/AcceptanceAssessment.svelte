<script lang="ts">
	import Icon from '../icons/icon.svelte';
	export let response: any;
	export let access: string;
	let check2 = true;
	const handleClick2 = () => {
		check2 = !check2;
	};

	const arl: number[] = response.arl.split(',').map(Number);

	const handleClick = async (payload: string) => {
		const x = await fetch(`http://127.0.0.1:8000/initial-readiness-levels/${response.id}/`, {
			method: 'put',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${access}`
			},
			body: JSON.stringify({
				arl: payload
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
			<p class="text-lg">Acceptance</p>
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
							Have you received feedback from potential users or stakeholders about your
							product/service?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.arl_response[0].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="acceptanceRating"
							class="mask mask-star"
							checked={arl[0] === 1}
							on:click={() => {
								arl[0] = 1;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating"
							class="mask mask-star"
							checked={arl[0] === 2}
							on:click={() => {
								arl[0] = 2;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating"
							class="mask mask-star"
							checked={arl[0] === 3}
							on:click={() => {
								arl[0] = 3;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating"
							class="mask mask-star"
							checked={arl[0] === 4}
							on:click={() => {
								arl[0] = 4;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating"
							class="mask mask-star"
							checked={arl[0] === 5}
							on:click={() => {
								arl[0] = 5;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
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
							How have you integrated this feedback into your development process?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.arl_response[1].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="acceptanceRating1"
							class="mask mask-star"
							checked={arl[1] === 1}
							on:click={() => {
								arl[1] = 1;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating1"
							class="mask mask-star"
							checked={arl[1] === 2}
							on:click={() => {
								arl[1] = 2;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating1"
							class="mask mask-star"
							checked={arl[1] === 3}
							on:click={() => {
								arl[1] = 3;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating1"
							class="mask mask-star"
							checked={arl[1] === 4}
							on:click={() => {
								arl[1] = 4;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating1"
							class="mask mask-star"
							checked={arl[1] === 5}
							on:click={() => {
								arl[1] = 5;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
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
							What steps have you taken to gauge and build market acceptance for your offering?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.arl_response[2].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="acceptanceRating2"
							class="mask mask-star"
							checked={arl[2] === 1}
							on:click={() => {
								arl[2] = 1;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating2"
							class="mask mask-star"
							checked={arl[2] === 2}
							on:click={() => {
								arl[2] = 2;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating2"
							class="mask mask-star"
							checked={arl[2] === 3}
							on:click={() => {
								arl[2] = 3;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating2"
							class="mask mask-star"
							checked={arl[2] === 4}
							on:click={() => {
								arl[2] = 4;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="acceptanceRating2"
							class="mask mask-star"
							checked={arl[2] === 5}
							on:click={() => {
								arl[2] = 5;
								handleClick(`${arl[0]},${arl[1]},${arl[2]}`);
							}}
						/>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
