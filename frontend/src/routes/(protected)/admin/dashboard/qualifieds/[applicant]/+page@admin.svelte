<script lang="ts">
	import Chart from 'chart.js/auto';
	import { browser } from '$app/environment';
	import { onMount } from 'svelte';
	let m = 9;
	export let data;
	const redrawChart = () => {
		let readiness = data.info.readiness_levels[data.info.readiness_levels.length - 1];
		let x = 65;
		let ctx: HTMLCanvasElement;
		const d = {
			labels: ['Technology', 'Organizational', 'Market', 'Regulatory', 'Acceptance', 'Investment'],
			datasets: [
				{
					label: 'Readiness Levels',
					data: [readiness.trl, readiness.orl, readiness.mrl, readiness.rrl, readiness.arl, 7],
					fill: true,
					backgroundColor: 'rgba(54, 162, 235, 0.2)',
					borderColor: 'rgb(54, 162, 235)',
					pointBackgroundColor: 'rgb(54, 162, 235)',
					pointBorderColor: '#fff',
					pointHoverBackgroundColor: '#fff',
					pointHoverBorderColor: 'rgb(54, 162, 235)'
				}
			]
		};

		const config = {
			type: 'radar',
			data: d,
			options: {
				elements: {
					line: {
						borderWidth: 3
					}
				}
			}
		};

		if (browser) {
			ctx = document.getElementById('chart') as HTMLCanvasElement;
			const chart = new Chart(ctx, {
				type: 'radar',
				data: d,
				options: {
					scales: {
						r: {
							min: 0,
							max: 9
						}
					}
				}
			});
		}
	};
	onMount(() => {
		redrawChart();
	});
</script>

<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-3 overflow-scroll h-full">
			<div class="flex gap-5 items-center">
				<a href="/admin/dashboard/qualifieds"
					><svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke-width="1.5"
						stroke="currentColor"
						class="w-6 h-6"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18"
						/>
					</svg>
				</a>
				<h2 class="text-xl font-bold text-left">X</h2>
			</div>
			<div class="flex-1 overflow-scroll">
				<h1>{data.info.name}'s Readiness Levels</h1>
			</div>
		</div>
	</div>
</div>
<div class="flex justify-center items-center w-full p-20">
	<canvas id="chart" class="h-96 w-96" />
</div>
