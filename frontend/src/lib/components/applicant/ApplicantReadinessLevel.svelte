<script lang="ts">
	import Chart from 'chart.js/auto';
	import { browser } from '$app/environment';
	import { onMount } from 'svelte';
	import Icon from '../icons/icon.svelte';
	let m = 9;
	export let readiness: any;
	
	const trl = readiness.trl.split(",").map(Number);
	const orl = readiness.orl.split(",").map(Number);
	const mrl = readiness.mrl.split(",").map(Number);
	const rrl = readiness.rrl.split(",").map(Number);
	const arl = readiness.arl.split(",").map(Number);
	const irl = readiness.irl.split(",").map(Number);
	let trlSum:number = 0,orlSum:number = 0,mrlSum:number = 0,rrlSum: number = 0,arlSum: number = 0,irlSum: number = 0;

	trl.forEach((element:number) => {
		trlSum+=element
	});

	orl.forEach((element:number) => {
		orlSum+=element
	});

	mrl.forEach((element:number) => {
		mrlSum+=element
	});

	rrl.forEach((element:number) => {
		rrlSum+=element
	});

	arl.forEach((element:number) => {
		arlSum+=element
	});

	irl.forEach((element:number) => {
		irlSum+=element
	});


	const redrawChart = () => {
		let x = 65;
		let ctx: HTMLCanvasElement;
		const d = {
			labels: ['Technology', 'Organizational', 'Market', 'Regulatory', 'Acceptance', 'Investment'],
			datasets: [
				{
					label: 'Readiness Levels',
					data: [trlSum, orlSum, mrlSum, rrlSum, arlSum, irlSum],
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
			<p>Readiness Levels</p>
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
