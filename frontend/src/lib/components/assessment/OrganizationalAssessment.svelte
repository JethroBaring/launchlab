<script lang="ts">
	import Icon from '../icons/icon.svelte';
	export let response: any;
	export let access: string;
	let check2 = true;
	const handleClick2 = () => {
		check2 = !check2;
	};

	const orl: number[] = response.orl.split(',').map(Number);

	const handleClick = async (payload: string) => {
		const x = await fetch(`http://127.0.0.1:8000/initial-readiness-levels/${response.id}/`, {
			method: 'put',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${access}`
			},
			body: JSON.stringify({
				orl: payload
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
			<p class="text-lg">Organizational</p>
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
							Describe your organizational structure and the roles of your team members.
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.orl_response[0].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="organizationalRating"
							class="mask mask-star"
							checked={orl[0] === 1}
							on:click={() => {
								orl[0] = 1;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating"
							class="mask mask-star"
							checked={orl[0] === 2}
							on:click={() => {
								orl[0] = 2;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating"
							class="mask mask-star"
							checked={orl[0] === 3}
							on:click={() => {
								orl[0] = 3;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating"
							class="mask mask-star"
							checked={orl[0] === 4}
							on:click={() => {
								orl[0] = 4;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating"
							class="mask mask-star"
							checked={orl[0] === 5}
							on:click={() => {
								orl[0] = 5;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
					</div>
				</div>
			</div>
			<div class="collapse">
				<input type="checkbox" checked={check2} />
				<div class="collapse-title text-xl font-semibold">
					<div class="flex gap-3 items-center">
						<p class="text-base">How are internal processes managed within your startup?</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.orl_response[1].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="organizationalRating1"
							class="mask mask-star"
							checked={orl[1] === 1}
							on:click={() => {
								orl[1] = 1;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating1"
							class="mask mask-star"
							checked={orl[1] === 2}
							on:click={() => {
								orl[1] = 2;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating1"
							class="mask mask-star"
							checked={orl[1] === 3}
							on:click={() => {
								orl[1] = 3;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating1"
							class="mask mask-star"
							checked={orl[1] === 4}
							on:click={() => {
								orl[1] = 4;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating1"
							class="mask mask-star"
							checked={orl[1] === 5}
							on:click={() => {
								orl[1] = 5;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
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
							What strategies do you have in place for team development and operational efficiency?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3"><p>{response.orl_response[2].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="organizationalRating2"
							class="mask mask-star"
							checked={orl[2] === 1}
							on:click={() => {
								orl[2] = 1;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating2"
							class="mask mask-star"
							checked={orl[2] === 2}
							on:click={() => {
								orl[2] = 2;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating2"
							class="mask mask-star"
							checked={orl[2] === 3}
							on:click={() => {
								orl[2] = 3;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating2"
							class="mask mask-star"
							checked={orl[2] === 4}
							on:click={() => {
								orl[2] = 4;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="organizationalRating2"
							class="mask mask-star"
							checked={orl[2] === 5}
							on:click={() => {
								orl[2] = 5;
								handleClick(`${orl[0]},${orl[1]},${orl[2]}`);
							}}
						/>
					</div></div>
			</div>
		</div>
	</div>
</div>
