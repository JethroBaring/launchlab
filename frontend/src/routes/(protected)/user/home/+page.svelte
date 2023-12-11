<script lang="ts">
	import { browser } from '$app/environment';
	import ApplicantReadinessLevel from '$lib/components/applicant/ApplicantReadinessLevel.svelte';
	import Icon from '$lib/components/icons/icon.svelte';
	import { Chart } from 'chart.js/auto';
	import { onMount } from 'svelte';
	export let data;
	const readiness = data.readiness.initial_readiness_level;

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
</script>

<svelte:head>
	<title>Overview</title>
</svelte:head>

<div class="flex flex-1 flex-col">
	<div class="flex flex-col flex-1 gap-10">
		<div class="flex flex-col gap-3 overflow-scroll h-full w-full mx-auto">
			<h2 class="text-2xl font-bold text-left">Readiness Level</h2>
			<div class="flex-1 overflow-scroll flex flex-col gap-5">
				<div class="flex-1 flex items-center justify-center p-14">
					<canvas id="chart"></canvas>
				</div>
			</div>
		</div>
	</div>
</div>
