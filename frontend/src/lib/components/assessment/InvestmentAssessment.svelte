<script lang="ts">
	import Icon from "../icons/icon.svelte";
	export let response: any;
	export let access: string;
	let check2 = true;
	const handleClick2 = () => {
		check2 = !check2;
	};

	const irl: number[] = response.irl.split(',').map(Number);

	const handleClick = async (payload: string) => {
		const x = await fetch(`http://127.0.0.1:8000/initial-readiness-levels/${response.id}/`, {
			method: 'put',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${access}`
			},
			body: JSON.stringify({
				irl: payload
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
			<p class="text-lg">Investment</p>
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
							What are your startup's funding goals, and what is your plan to achieve them?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3">
					<p>{response.irl_response[0].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="investmentRating"
							class="mask mask-star"
							checked={irl[0] === 1}
							on:click={() => {
								irl[0] = 1;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating"
							class="mask mask-star"
							checked={irl[0] === 2}
							on:click={() => {
								irl[0] = 2;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating"
							class="mask mask-star"
							checked={irl[0] === 3}
							on:click={() => {
								irl[0] = 3;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating"
							class="mask mask-star"
							checked={irl[0] === 4}
							on:click={() => {
								irl[0] = 4;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating"
							class="mask mask-star"
							checked={irl[0] === 5}
							on:click={() => {
								irl[0] = 5;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
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
							Have you prepared an investment proposal or pitch for potential investors?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3"><p>{response.irl_response[1].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="investmentRating1"
							class="mask mask-star"
							checked={irl[1] === 1}
							on:click={() => {
								irl[1] = 1;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating1"
							class="mask mask-star"
							checked={irl[1] === 2}
							on:click={() => {
								irl[1] = 2;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating1"
							class="mask mask-star"
							checked={irl[1] === 3}
							on:click={() => {
								irl[1] = 3;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating1"
							class="mask mask-star"
							checked={irl[1] === 4}
							on:click={() => {
								irl[1] = 4;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating1"
							class="mask mask-star"
							checked={irl[1] === 5}
							on:click={() => {
								irl[1] = 5;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
					</div></div>
			</div>
			<div class="collapse">
				<input type="checkbox" checked={check2} />
				<div class="collapse-title text-xl font-semibold">
					<div class="flex gap-3 items-center">
						<p class="text-base">
							What steps have you taken to understand and engage with potential investors?
						</p>
						<Icon
							data1={check2 ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
							data2={null}
						/>
					</div>
				</div>
				<div class="collapse-content flex flex-col gap-3"><p>{response.irl_response[2].trim()}</p>
					<div class="rating">
						<input
							type="radio"
							name="investmentRating2"
							class="mask mask-star"
							checked={irl[2] === 1}
							on:click={() => {
								irl[2] = 1;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating2"
							class="mask mask-star"
							checked={irl[2] === 2}
							on:click={() => {
								irl[2] = 2;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating2"
							class="mask mask-star"
							checked={irl[2] === 3}
							on:click={() => {
								irl[2] = 3;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating2"
							class="mask mask-star"
							checked={irl[2] === 4}
							on:click={() => {
								irl[2] = 4;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
						<input
							type="radio"
							name="investmentRating2"
							class="mask mask-star"
							checked={irl[2] === 5}
							on:click={() => {
								irl[2] = 5;
								handleClick(`${irl[0]},${irl[1]},${irl[2]}`);
							}}
						/>
					</div></div>
			</div>
		</div>
	</div>
</div>
