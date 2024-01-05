<script lang="ts">
	import Chart from 'chart.js/auto';
	import { browser } from '$app/environment';
	import { onMount } from 'svelte';
	import Icon from '../icons/icon.svelte';
	let m = 9;
	export let readiness: any;
	
	const trl = readiness.filter((d) => d.readiness_type === "Technology").reduce((accumulator: any, currentValue: any) =>  {
		return	accumulator + currentValue.score
	}, 0)
	const orl = readiness.filter((d) => d.readiness_type === "Organizational").reduce((accumulator: any, currentValue: any) =>  {
		return	accumulator + currentValue.score
	}, 0)
	const mrl = readiness.filter((d) => d.readiness_type === "Market").reduce((accumulator: any, currentValue: any) =>  {
		return	accumulator + currentValue.score
	}, 0)
	const rrl = readiness.filter((d) => d.readiness_type === "Regulatory").reduce((accumulator: any, currentValue: any) =>  {
		return	accumulator + currentValue.score
	}, 0)
	const arl = readiness.filter((d) => d.readiness_type === "Acceptance").reduce((accumulator: any, currentValue: any) =>  {
		return	accumulator + currentValue.score
	}, 0)
	const irl = readiness.filter((d) => d.readiness_type === "Investment").reduce((accumulator: any, currentValue: any) =>  {
		return	accumulator + currentValue.score
	}, 0)

	const redrawChart = () => {
		let x = 65;
		let ctx: HTMLCanvasElement;
		const d = {
			labels: ['Technology', 'Organizational', 'Market', 'Regulatory', 'Acceptance', 'Investment'],
			datasets: [
				{
					label: 'Readiness Levels',
					data: [trl, orl, mrl, rrl, arl, irl],
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

		if (browser) {
			ctx = document.getElementById('chart') as HTMLCanvasElement;
			const chart = new Chart(ctx, {
				type: 'radar',
				data: d,
				options: {
					scales: {
						r: {
							min: 1,
							max: 16
						}
					},
					responsive: true,
					maintainAspectRatio: false,
					plugins: {
						legend: {
							display: false
						}
					}
				}
			});
		}
	};
	onMount(() => {
		redrawChart();
	});

    let check = false;

	const handleClick = () => {
		check = !check;
	};
</script>

<div class="collapse">
	<input type="checkbox" checked={check} on:click={handleClick} />
	<div class="collapse-title text-xl font-semibold">
		<div class="flex gap-3 items-center">
			<p>URAT Questionnaire Readiness Levels</p>
			<Icon
				data1={check ? 'M4.5 15.75l7.5-7.5 7.5 7.5' : 'M19.5 8.25l-7.5 7.5-7.5-7.5'}
				data2={null}
			/>
		</div>
	</div>
	<div class="collapse-content flex flex-col gap-3">
		<canvas id="chart"></canvas>
	</div>
</div>
